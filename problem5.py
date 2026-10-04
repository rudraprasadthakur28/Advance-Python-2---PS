from functools import reduce
l = [1, 2, 686446, 56, 6548666, 598565, 568496856]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))