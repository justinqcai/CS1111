# Justin Cai, jc5pz

tGPA = 0.0
creds = 0


def add_course(gp, cred = 3):
    global tGPA
    global creds
    oGPA = tGPA * creds
    creds += cred
    tGPA = (oGPA + gp*cred)/creds


def gpa():
    global tGPA
    return tGPA


def credit_total():
    global creds
    return creds
