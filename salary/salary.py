#Justin Cai, jc5pz
import re
import urllib.request
from urllib.error import URLError

def report(name):
    '''

    :param name: name given by assignment
    :return: the job name (string), how much money they make (float), and rank (int) if there is one, else returns 0
    This function first calls the name_to_url function I wrote, which takes the name given by the assignment and changes
    it to another string, but in url format. It then runs a try-except where it will attempt to open the url and returns
    None, 0, 0 if the url doesn't work. It then creates regex's that capture the job title, pay, and rank (if there is
    one). It then searches for the regex and creates variables equal to the captured groups. The job title variable then
    replaces miscellaneous text. The rank title variable then removes all commas. The function then returns job title,
    pay, and rank (as an integer). If there is no rank, it returns rank as 0.
    '''
    url = name_to_url(name)
    try:
        stream = str(urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + url).read())
        # text = ''
        # for line in stream:
        #     decoded = line.decode('UTF-8')
        #     text += decoded
    except URLError:
        return None, 0, 0
    job = re.compile('Job title: ([\w\-&;\s]+)')
    money = re.compile('paytype\.amount, ([\d\.]+)')
    rank = re.compile('([\d,]+) of [\d,]+')
    j = re.search(job, stream).group(1)
    j = j.replace('&amp;', '&')
    j = j.replace('&lt;', '<')
    j = j.replace('&gt;', '>')
    m = re.search(money, stream).group(1)
    r = re.search(rank, stream)
    if r is None:
        return j, float(m), 0
    else:
        r = r.group(1).replace(',', '')
    return j, float(m), int(r)


def name_to_url(name):
    '''

    :param name: the name being put into url format
    :return: string containing the name in url format
    This function first checks if comma is in the name, if it is then it rearranges the name, removes the comma and
    replaces spaces with hyphens, and makes it lowercase. It then returns the url. It then checks if spaces are in the
    name, if it is then it returns the name lowercase with hyphen instead of space. It returns the given name in
    lowercase letters at the very end.
    '''
    url = ''
    if ',' in name:
        url += name[name.index(',')+2:].lower()
        url += '-'
        url += name[:name.index(',')].lower()
        return url
    elif ' ' in name:
        for x in name:
            if x == ' ':
                url += '-'
            else:
                url += x.lower()
        return url
    else:
        return name.lower()