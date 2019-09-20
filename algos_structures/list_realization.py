# реализация списков из статьи Хабра

class List():
    def __init__(self):
        self.memory = []
        self.length = 0

    # получение элемента
    def get (self, address):
        return self.memory[address]

    # добавление элемента в конец списка
    def push(self, value):
        self.length = len(self.memory)  #3

        self.memory.append(" ") # adding memory for new element
        self.memory[self.length] = value
        self.length += 1
        return self.memory

    def pop(self):
        self.length = len(self.memory)

        if self.length == 0: return
        lastAddress = self.length - 1
        value = self.memory[lastAddress] # get [2]

        del self.memory[lastAddress]
        self.length = self.length - 1
        return self.memory

    def unshift (self, value):
        # сохраняем значение которое надо добавить в начало
        previous = value

        # проходимся по каждому элементу
        address = 0
        for address in range(len(self.memory)):
            current = self.memory[address]  # get stock 0 value
            self.memory[address] = previous # store new value
            previous = current              # new = past for past in next iter

        self.push (previous)
        return self.memory

    def shift (self):
        mass_num = []
        mass_val = []

        self.unshift("x")

        for num, val in  enumerate(self.memory):
            mass_num.append(num)
            mass_val.append(val)

        for i in  range (len (mass_val) - 1):
            self.memory[i] = self.memory[i+1]

        self.pop()
        return self.memory

obj_1 = List()
obj_1.memory = ['one', 'two', 'three']

#print (obj_1.memory)

#print (obj_1.push ('NAME'))
# print (obj_1.get(3))

#print(obj_1.pop())

print (obj_1.unshift('NEW_NEW'))

#print (obj_1.shift())