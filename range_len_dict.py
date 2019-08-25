
mass = ['one', 'two', 3]

if isinstance(mass, list):
    # перебираем элементы
    for m in mass:
        print(m)

    print("\n")
    #print(range(mass))         # ошибка тк конечное число диапазона не может быть буквой
    print (list(range(10)))     # список значений от 0 до 10
    a = []

    # перебираем индексы
    print("\n")
    for x in range(len(mass)):
        print(x)
        a.append(x)

    print("\n")
    print(a)
    print("\n")

    for num, value in enumerate(mass):
        print(num, value)

    print("\n")

    dictd={}
    for x, z in enumerate(mass):
        print("Индекс: {}".format(x))
        print("Значение: {}\n".format(z))
        dictd.update({x : z})               #один словарь в другой

        if x == 2:
            print("По индексу <{}> находится элемент <{}>\n".format(x,z))

    print(dictd)    # весь словарь

    print("\n")

    dict = {'Имя': 'Alex', 'Возраст': 18}
    dict2 = {'Пол': 'Мужской'}

    dict.update(dict2)
    print("Обновление словаря : ", dict)
