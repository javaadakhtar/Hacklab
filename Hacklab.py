def permutate(lst):
    if not lst:
        return [lst]  # is an empty sequence
    else:
        temp = []
        for k in range(len(lst)):
            part = lst[:k] + lst[k+1:]
            #print k, part  # test
            for m in permutate(part):
                temp.append(lst[k:k+1] + m)
        return temp

def final(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return permutate(lst)
