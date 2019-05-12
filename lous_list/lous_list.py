#justin Cai, jc5pz

import urllib.request


def instructors(department):
    """
    This function loops through each class in the given department and will add the teacher for the class in its
    if the teacher is not already in the master list "ins". It then sorts and returns "ins" at
    the very end.
    :param department: department name
    :return: returns a list of all teachers in the department in alphabetical order
    """
    stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + department)
    ins = []
    for line in stream:
        decoded_data = line.decode("UTF-8").strip().split("|")
        if len(ins) == 0 or decoded_data[4].split("+")[0] not in ins:
            ins.append(decoded_data[4].split("+")[0])
            # for x in ins:
            #     if x > decoded_data[4].split("+")[0]:
            #         ins.insert(ins.index(x), decoded_data[4].split("+")[0])
            #         break
    ins.sort()
    return ins


def class_search(dept_name, has_seats_available=True, level=None, not_before = None, not_after = None):
    """
    This function looks through each class in the department given by dept_name and for each class, runs a series of
    tests (if-statements) where if each if-statement successfully passes (i.e. the class passes all the tests), the
    master list "classes" that's returned at the end will append the information for the class. The function then
    returns the list "classes."
    :param dept_name: department name
    :param has_seats_available: if seats are available in the class, if False then doesn't check
    :param level: what level class it is, if None then doesn't check
    :param not_before: what time is the earliest the class can be, if None then doesn't check
    :param not_after: what time is the latest the class can be, if None then doesn't check
    :return: returns a list "classes" of lists (all the information for each class that passes all the tests/parameters
    given in the function
    """
    classes = []
    stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/" + dept_name)
    for line in stream:
        decoded_data = line.decode("UTF-8").strip().split("|")
        if (int(decoded_data[15]) < int(decoded_data[16])) is has_seats_available or has_seats_available is False:
            if level is None or int(decoded_data[1])//1000 == level//1000:
                if not_before is None or int(decoded_data[12]) >= not_before:
                    if not_after is None or int(decoded_data[12]) <= not_after:
                        classes.append(decoded_data)
    return classes
