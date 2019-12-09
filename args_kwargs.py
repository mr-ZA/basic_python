def myFunc_args (*args):
    zex = 1

    for a in args:
        zex *= a

    print (zex)

def myFunc_kwargs (**kwargs):
    if not kwargs:
        print (("В функцию <{}()>, {}\n").format("myFunc_kwargs", "не переданы аргументы"))
    else:
        print (("Функция <{}()>, {}: {}\n").format("myFunc_kwargs", "принимает словарь", kwargs))
        for k, v in kwargs.items():
            print (k + ",", v)

        print("\n")
        print ("{} {}".format("Первый элемент словаря: ", kwargs['kw_1']))

        print("\n")
        print (kwargs.keys())
        print(kwargs.values())

        print("\nЗамена первого элемента словаря:")
        kwargs["kw_1"] = "Elephant"
        for k, v in kwargs.items():
            print (k, v)

def main():
    print ("Функция myFunc_args: ")
    myFunc_args (3, 4, 10)
    print("\n")

    myFunc_kwargs()

    myFunc_kwargs(kw_1 = "Shark", kw_2 = "Lion")

if __name__ == '__main__':
    main()
