def check_name(n):
    if n == "KATE":
        return True

# Deque method from Queue realization on the knees
def deque(elems):
    frst = elems[0]

    for e in range(len(elems) - 1):
        elems[e] = elems[e+1]

    del (elems[len(elems) - 1])

    # print(elems)          #returns : ['ALICE', 'BOB', 'KATE']
    return frst, elems

def search_people(names):
    searched = []
    search_queue = []       # no need of class here, simplified
    search_queue += names

    # print(next_queue)     #returns : TOM
    # print(search_queue)

    while search_queue:
        person, n_list = deque(search_queue)    # full analog of special function popleft() in book
        if not person in searched:
            if check_name(person):
                print("Found")
                return True
            else:
                search_queue = n_list       # just check, that del() from deque function deletes value globally
                searched.append(person)
                print(searched)

def main():
    graph = {}
    graph["ME"] = ["TOM", "ALICE", "TOM", "BOB", "KATE"]

    search_people(graph["ME"])

if __name__ == '__main__':
    main()
