#Justin Cai, jc5pz


def binop(x):
    if x.find("*") != -1:
        first = x[:x.index("*")].strip()
        second = x[x.index("*")+1:].strip()
        return int(first)*int(second)
    elif x.find("/") != -1:
        first = x[:x.index("/")].strip()
        second = x[x.index("/") + 1:].strip()
        return int(first) / int(second)
    if x.find("+") != -1:
        first = x[:x.index("+")].strip()
        second = x[x.index("+") + 1:].strip()
        return int(first) + int(second)
    if x.find("-") != -1:
        first = x[:x.index("-")].strip()
        second = x[x.index("-") + 1:].strip()
        return int(first) - int(second)

