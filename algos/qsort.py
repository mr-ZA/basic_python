def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]            # p = 12                    # p = 4
        for x in array:
            if x < pivot:
                less.append(x)      # [4, 5, 6, 7, 3, 1]        # [3, 1]
            if x == pivot:
                equal.append(x)     # [12]                      # [4]
            if x > pivot:
                greater.append(x)   # [15]                      # [5, 6, 7]

        return sort(less) + equal+ sort(greater)

    else:
        return array

array = [12, 4, 5, 6, 7, 3, 1, 15]
print (sort(array))

                                # [ [4, 5, 6, 7, 3, 1], [12], [15] ]
# less                                                                      # greater
# [ [3, 1], 4, 5, 6, 7]                                                     # 15
#    /           \
# less           greater
# [ 1, 3 ]   4   [5, 6, 7]
