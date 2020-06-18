class Human():

    def __init__(self, name = "Default_name", age = "Default_age", gender = "Defailt_gender"):                  #self here means that, we import the link to instance of the Human class in Carl's and Anna's way (spec. descriptor)
        self.name = name                                                                                        #setting the parameters, to specific instance variables
        self.age = age
        self.gender = gender

def main():
    carl = Human ("Carl", 22, "male")
    anna = Human ("Anna", 35, "female")

    print("\n")
    print("{} name = {}, age = {}, gender = {}".format("Carl attributes: ", carl.name, carl.age, carl.gender))
    print("{} name = {}, age = {}, gender = {}".format("Anna attributes: ", anna.name, anna.age, anna.gender))
    print("\n")

if __name__ == '__main__':
    main()
