import re
import urllib.request

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.php')

text = ''
def full_match(regex, text):
    '''Gives a list of all complete matches'''
   # ans = []
    for match in regex.finditer(text):
        print(match.group(0))
   # return ans

#email = re.compile('[\w\.-]+@\S+\.\w+')
email = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
for line in stream:
    decoded = line.decode('UTF-8').strip()
    text += decoded

full_match(email, text)


