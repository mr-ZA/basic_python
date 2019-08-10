# -*- coding: utf-8 -*-

class Own_Iter:

    def __iter__(self):
        return self

    def iter_2 (self):
        print(self.mass[self.counter])

    def __init__(self, limit):
        self.limit = len(limit)
        self.mass = limit
        self.counter = 0

    def __next__(self):                        #redef method that counts
        if self.counter < self.limit:
            self.iter_2()
            self.counter += 1
            self.__next__()

def main():
    mass_1 = [1, 2, 3, 4, 5]

    obj_own = Own_Iter(mass_1)

    print ("\n++++++++++++++++++++++++++\n Обработка внутри класса\n++++++++++++++++++++++++++")

    next (obj_own)

    print ("\n+++++++++++++++++++++++++++++++\n Возвращается объект итератора\n+++++++++++++++++++++++++++++++")

    for i in mass_1:
        print(i)

if __name__ == '__main__':
    main()
