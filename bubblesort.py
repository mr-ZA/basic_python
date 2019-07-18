# -*- coding: utf-8 -*-

def bubblesort(lst):
    for x in range (len (lst)):               # 0 - 4
        for j in range (x + 1, len(lst)):     # 1 - 4
            if lst[j] > lst[x]:
                temp = lst[j]
                lst[j] = lst[x]
                lst[x] = temp
    return lst

def main():
    mass_1 = [i for i in range (0, 5)]      #generator of the list
    print(type(mass_1))

    print (bubblesort(mass_1))

if __name__ == '__main__':
    main()
