#Justin Cai, jc5pz
""" The purpose of this program is to check user-entered text for misspelled words while disregarding punctuation
(except for specific cases involving apostrophes. My code first loops through the dictionary given in the link
 and adds every word in lower-case form (to simplify the capitalization requirement for me later on in the code) to a
 list I named dic. My code then runs a while-loop that keeps asking the user to input text until they input a blank
 line, and my code will loop through the inputted text word-by-word, automatically taking out all punctuation besides
 apostrophes. It then checks the word for apostrophes and will remove all apostrophes at either the front or end of the
 word. It then checks if the lower-case version of the word word is a valid word in the dictionary, if it isn't then
 it'll print that the word is misspelled. """
import urllib.request

stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/words.txt")
dic = []
user = input("Type text; enter a blank line to end. \n")
for line in stream:
    decoded_data = line.decode("utf-8").strip()
    dic.append(decoded_data.lower())

while user != "":
    new_user = "".join(c for c in user if c not in ('!', '.', ',', ':', '?', '(', ')', '"', ",")).split()
    for x in new_user:
        while "'" in x:
            ind = x.index("'")
            if ind == 0:
                x = x[1:]
            elif ind == len(x)-1:
                x = x[:-1]
            else:
                break
        if x.lower() not in dic:
            print(" MISSPELLED: " + x)
    user = input()

