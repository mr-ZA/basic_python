# выстраивание текста
def create_text (coordinates, bukv):
    new_mass = []

    sorted_coordinates = sorted(coordinates, key=lambda c: c[1])       # сортировка букв по [y]
    i = 0

    # разница в координатах м-ду двумя соседними в отсортированном массиве
    while i < len(sorted_coordinates):
        new_mass.append(sorted_coordinates[i+1][1] - sorted_coordinates[i][1])
        i += 1

    m = mode(new_mass)                  # нахождение повторяющегося числа в координатах [по Y]
    stroka = []     #
    stroki = []

    str_stroki = []
    str_stroka = []

    for k, n in enumerate(new_mass):
        # проверка по координатам переходов
        if n <= m * 1.2:
            stroka.append(sorted_coordinates[k][1])     # запись координат переходов

        else:
            stroki.append([min(stroka), max(stroka)])   # запись
            stroka.clear()

    print(stroki)

    for i, c in enumerate(coordinates):
        for s in stroki:
            if c[1] in range (s[0], s[1]):
                stroki.append(bukv[i])

cor = [[1, 2], [5, 10], [15, 3], [5, 10], [7, 2], [5, 10], [7, 6], [3, 20]]
buk = ["q", "a", "d", "e", "p", "a", "r", "t"]

create_text(cor, buk)