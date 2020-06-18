class Queue:
    def __init__(self, data):
        self.data = data

    # add to the end
    def enqueue (self, elem):
        self.length = len(self.data)
        self.data.append(' ')

        self.data[self.length] = elem

        return self.data

    # del from the head
    def dequeue (self):
        mass_n = []
        mass_val = []

        for i in  range (len (self.data) - 1):
            self.data[i] = self.data[i+1]

        del (self.data[len(mass_val) - 1])      # [20, 30, 40, 5, ->5]

        return self.data

    def peek (self):
        return self.data[0]

def main():
    data = [10, 20, 30, 40]
    q = Queue(data)

    print (q.enqueue(5))
    print(q.peek())
    print (q.dequeue())

if __name__ == '__main__':
    main()