def get_secret(list, secret):

    low = 0
    step = 0
    high = len(list) - 1       # 0..4      # 0..6

    while low <= high:
        print("\n")
        print(list)
        print(f"Нижняя граница: {low}")
        print(f"Верхняя граница: {high}")
        index = int((low + high) / 2)
        print(f"Промежуточный индекс (половина бинарная от массива list): {index}")
        guess = list[index]
        print(f"Предполагаемое загаданное число list[{index}] = {guess}")

        if guess == secret:
            print(f"Предполагаемое число [{guess}] = [{secret}] загаданному")
            return guess, step

        if guess > secret:        #если guess уже больше secret, а массив отсортирован(следующие числа больше чем текущее и они никак не могут быть меньше)
            print(f"Предполагаемое число [{guess}] > [{secret}] загаданного")
            print("Убираю предполагаемое загаданное число > загаданного, и числа больше предполагаемого")   # если промежуточное уже больше загаданного, то числа которые > промежуточного автоматически не подходят
            high = index - 1
            step = step + 1

        else:
            print(f"Предполагаемое число [{guess}] < [{secret}] загаданного")
            print("Убираю предполагаемое загаданное число < загаданного, и числа меньше предполагаемого")    # происходит сдвиг нижней границы на позицию > загаданного
            low = index + 1
            step = step + 1

    return "Error"


my_list = [1, 3, 5, 7, 9, 10, 11]
print(get_secret(my_list, 5))
