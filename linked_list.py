class Node:
    def __init__(self, current = None, next = None):

        # Defining Node type properties for all nodes in intialize of every node (node -> node.current + node.next)
        self.current = current
        self.next = next

    def __str__(self):
        # Making node.current = type String
        return str(self.current)

# Вывод элементов связного списка по ссылкам от первого элемента
def print_forward(node):
    while node:
        print(node, end=" ")
        node = node.next
    print("\n")

# Печать элементов в обратном порядке
def print_backward(list):
    if list == None : return

    # First element
    head = list

    # Element after first
    tail = list.next

    print_backward(tail)

    # After last iteration (head = 3, last = None) stack unloaded from stack
    print(head, end=" ")

def remove_second(list):
    if list == None: return

    first = list
    second = list.next

    # Make first element refer to third.current (second.next)
    first.next = second.next

    # Separate second node from the list
    second.next = None

    # Print None in stdout because of print_forward() return nothing
    # return print_forward(list)

    # Print renewed nodes list
    print_forward(list)


# Creating Node structure
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Creating connexions
node1.next = node2
node2.next = node3

# Infinite list
# node3.next = node1

print("\n")
print("Forward list of nodes: ")
print_forward(node1)

print("Backward list of nodes: ")
print_backward(node1)
print("\n")

print("Remove second element from the list of nodes: ")
# Print None in stdout because of print_forward() return nothing
# print(remove_second(node1))

remove_second(node1)

# Translate Node undefined type to concrete <str> thx to __str__
node1.next = node2.current
node2.next = node3.current

# Links from the nodes, array. Last node -> NULL
node_full = [node1.next, node2.next, 0]

# Here was some messy-skills, briefly we cannot print [ node1, node2, node3 ] if 1,2,3 is ints from for cycle. node - <variable>, 1-2-3 is an <int>
print("| Node | Next |")
for i in range(1, 4):
    exec('print (\"%4d %6d\" % (node{}.current, node_full[{}]))'.format(i, i-1), locals(), globals())