# -*- coding: utf-8 -*-

def desc_bubblesort(lst):
    for x in range (len (lst)):               # [0____], [1____]
        for j in range (x + 1, len(lst)):     # [1 - 4], [2 - 4]
            if lst[j] > lst[x]:
                temp = lst[j]
                lst[j] = lst[x]
                lst[x] = temp
    return lst

def asc_bubblesort(lst):
    for x in range (len (lst)):
        for z in range (x+1, len(lst)):
            if lst[z] < lst[x]:
                temp = lst[x]
                lst[x] = lst[z]
                lst[z] = temp
    return lst

def main():
    mass_1 = [i for i in range (0, 5)]      # generator of the list desc
    mass_2 = list (reversed(mass_1))        # for ascending method [4, 3, 2 ...]
    #print(type(mass_1))
    #print(type(mass_2))

    print (desc_bubblesort(mass_1))
    print(asc_bubblesort(mass_2))

if __name__ == '__main__':
    main()
