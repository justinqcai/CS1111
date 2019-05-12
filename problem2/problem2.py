def count_sum(l):
    count = 0
    for x in range(0, len(l)-1):
        if l[x] + l[x+1] == 10:
            count += 1
    return count
print(count_sum([]))                                  #  0
print(count_sum([1]))                                 #  0
print(count_sum([5, 5]))                              #  1
print(count_sum([5, 5, 6, 4, 8]))                     #  2
print(count_sum([2, 7, 3, 1, 9, 5, 5, 4, 6, 8]))      #  4
