def get_secret(list, secret):

    low = step = 0
    high = len(list) - 1       # 0..4      # 0..6

    while low <= high:
        index = int((low + high) / 2)
        guess = list[index]

        if guess == secret:
            return guess, step

        if guess > secret:        #если guess уже больше secret, а массив отсортирован(следующие числа больше чем текущее и они никак не могут быть меньше)
            high = index - 1
            step = step + 1

        else:
            low = index + 1
            step = step + 1

    return "Error"


my_list = [1, 3, 5, 7, 9, 10, 11]
print(get_secret(my_list, 5))
