# -*- coding: utf-8 -*-

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return fib(n-1) + fib(n-2)

def main():
    n = input()
    print (fib (int(n)))

if __name__ == '__main__':
    main()