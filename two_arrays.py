def stupid_travers(arr_new, arr_system):
    arr_result = []

    # Stupid type of intersection finding..
    for a_1 in arr_new:
        for a_2 in arr_system:
            if a_1 == a_2:
                arr_result.append(a_2)

    print("\n")
    print(f"Traversal between two arrays = {arr_result} (stupid)")

class Node:
    def __init__(self, letter):
        self.val = letter
        self.children = []
        self.last = False

    def __str__(self):
        # Making node.val = type String for print_forward()
        return str(self.val)

def tries_travers(arr_new, arr_system):
    pass

# Функция создающая структуру дерева
def insert_in_tree():
    pass

def print_forward(node):
    print("________Structure of the tree:_________")
    while node:
        if node.next != None:
            print(node, end=" -> ")
        else:
            print(node, end="")
        node = node.next
    print("\n")

# Функция проверяющая на наличие ветки
def checker(node, k):
    pass

def main():
    arr_1 = ["mata121", "mata360", "ru06t02", "mata467n"]   # обновленные тресы
    arr_2 = ["agra045", "mata360", "mata101n", "ru09t02", "mata121"]    # из списка - все

    print("__________FIRST________")
    # First array prints
    for a_1 in arr_1:
        print(a_1)

    print("\n")

    print("__________SECOND________")
    # Second array prints
    for a_2 in arr_2:
        print(a_2)

    stupid_travers(arr_1, arr_2)

    root = Node()

if __name__ == '__main__':
    main()