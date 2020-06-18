class Info():
    # storage exactly
    def __init__(self, name, type_a, table):
        self.name = name        # name of animal
        self.type_a = type_a    # type of animal
        self.table = table      # global array

    def show(self):
        print(self.name, self.type_a)


def hash (name):
    word = list(name)

    for n in range(len(name)):
        word[n] = str (ord(name[n]) % 4)

    word = ''.join(word)    # list to str
    word = int(word)        # str to int

    return word

def push (name, type_a):
    hashNumber = hash(name)
    global table
    table[hashNumber] = [type_a]


def find(name):
    hash_f_Number = hash(name)
    result = table[hash_f_Number]   # find the type by name in array

    if not result:
        print("Element not found -> <{}>: ".format(hash_f_Number))
        return -1;
    else:
        print("I found the type of the animal by hashed name <{}> -> <{}>: ".format(name, hash_f_Number))
        print(result)

def main():
    global name, type_a, table
    table = [None] * 100000

    print("Enter name and type of the animal to hash it: ")
    name = input()
    type_a = input()

    push(name, type_a)
    find(name)

if __name__ == '__main__':
    main()