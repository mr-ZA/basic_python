class Stack():
    def __init__(self, stack):
        self.stack = stack
        self.length = 0

    def pop(self):
        self.length = len(self.stack) - 1
        if self.length == 0: return

        del (self.stack[self.length])

        return self.stack

    def push(self, x):
        length = len(self.stack)     # 10 elem -> 0..9

        self.stack.append(" ")       # allocate the space [0..10]
        self.stack[length] = x       # set element on last index

        return self.stack

    def peek(self):
        self.length = len(self.stack) -1

        return self.stack[self.length]

def main():
    stack = [None] * 10

    s = Stack (stack)

    print("Function push()")
    print (s.push(4))

    print("\nFunction pop()")
    print (s.pop())

    print("\nFunction peek()")
    s.push(123)
    print(s.peek())

if __name__ == '__main__':
    main()