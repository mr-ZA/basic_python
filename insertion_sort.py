
def findSmallest(arr):
    smallest = arr[0]       # default - 4
    smallest_index = 0      # default - arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    newArr = []

    # 0..4 < 5
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))        # pop delete element by index, and return it to append method.

    return newArr

def main ():
    mass = [4, 1, 9, 24, 2]

    print(selectionSort(mass))

if __name__ == '__main__':
    main()