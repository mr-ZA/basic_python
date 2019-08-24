# def myFunc(n):
#     return lambda a: a * n

def myFunc(a, n):
    return a * n

def main():
    #var_x = myFunc(2)

    var_x = lambda a, b: myFunc(a, b)
    print (myFunc (var_x (10, 5), 2))

if __name__ == '__main__':
    main()
