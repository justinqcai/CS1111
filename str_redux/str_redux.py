#Justin Cai, jc5pz


def myfind(word, l):
    if l in word:
        for x in range(len(word)-len(l)+1):
            if l in word[x:x+len(l)]:
                return x
    else:
        return -1

def mysplit(word):
    new_word = []
    pos = 0
    while " " in word[pos:]:
        first = myfind(word[pos:], ' ')
        new_word.append(word[pos:first+pos])
        pos += first+1
    new_word.append(word[pos:])
    return new_word

