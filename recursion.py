def rec(a,b):
    if b == 0:
        return 1
    else:
        return a * rec(a, b-1)

a, b = 2, 3
print(rec(a,b))