#Justin Cai, jc5pz
gb = {}
creds = {}
def assignment(kind, grade, weight=1):
    global gb
    global creds
    if kind not in gb:
        gb[kind] = grade
        creds[kind] = weight
    else:
        temp = gb[kind]* creds[kind]
        creds[kind] += weight
        gb[kind] = (temp+grade*weight)/creds[kind]
def total(proportions):
    grade = 0.0
    for x in proportions:
        if x in gb:
            grade += proportions[x]*gb[x]
    return grade