def mymap(f, initial):
    end = []
    for a in initial:
        end.append(f(a))
    return end
def myreduce(f, initial):
    end = initial[0]
    for a in range(1, len(initial)):
        end = f(end, initial[a])
    return end