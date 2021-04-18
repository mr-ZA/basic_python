def rotate(s):
    return list(zip(*s[::-1]))

j=0
for angle in range(4):
    for i in range(3):
        print()     