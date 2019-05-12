def chop_list(l, w):
    new_l = [[]*len(l)//w+1]
    for x in l:
        new_l.append(x)