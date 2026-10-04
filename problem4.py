def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 686446, 56, 6548666, 598565, 568496856]

f = list(filter(divisible5, a))

print(f)