def check(cc):
    temp = str(cc)
    sum = 0
    lsum = []
    for x in range(len(temp)):
        if len(temp)%2==1:
            if x%2 == 0:
                sum+=int(temp[x])
            else:
                lsum.append(str(int(temp[x])*2))
        else:
            if x%2 != 0:
                sum+=int(temp[x])
            else:
                lsum.append(str(int(temp[x])*2))
    sum2 = 0

    for x in lsum:
        for y in x:
            sum2 +=int(y)
    if (sum+sum2) % 10 == 0:
        return True
    return False