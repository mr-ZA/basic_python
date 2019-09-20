def sort(mass):
    for m in range (1, len (mass)):
        insertion_value = mass[m]   # value for insert in the beginning
        j = m - 1       # link on previous element

        # if previous elements from the beggining are larger
        while j >= 0 and mass[j] > insertion_value:
            mass[j + 1] = mass[j]       # [9, 9, 5, 22, 4], j= 0, insertion_value = mass[m]

            j = j - 1
        mass[j + 1] = insertion_value   # [1, 9, 5, 22, 4]

    return mass

if __name__ == '__main__':

    mass = [9, 1, 5, 22, 4]