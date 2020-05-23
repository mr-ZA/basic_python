from Python.tries.file_handler.file_handling import *
import time

class Trie_main:

    class Node:
        def __init__(self, letter):
            self.val = letter
            self.children = []
            self.last = False

        def __str__(self):
            # Making node.val = type String for prin\t_forward()
            return str(self.val)

    def __init__(self):
        self.root = self.Node('*')

    # Функция отвечающая за обработку структуры дерева
    def insert_in_tree(self, word: str) -> None:
        """
        Inserts data into the trie
        """

        # Создание ветки в дереве из слова
        def create_tree(word, iter):
            # инициализация структуры
            n = self.Node(word[iter])

            if iter + 1 < len(word):
                n.children = [create_tree(word, iter + 1)]      # FAQ на строке 102 [↓↓↓]
            else:
                n.last = True

            return n

        # проверка на отличающиеся разветвления и склейка веток (новой <-> от корня текущей)
        def merge_tree(root_children, new_first_children):
            for child in root_children:
                if child.val == new_first_children[0].val:
                    if not new_first_children[0].children:
                        child.last = True
                        return
                    return merge_tree(child.children, new_first_children[0].children)   # итератор в данном случае <.children>, у <new_first> берем только 1 ветку, тк не предполагается разветвлений

            # root children после определенной итерации (ex. mata360, a.children =[3] [val=3, 6, 0]) при несходимости с mata120, a.children =[1] [val=1, 2, 0] =>
            # 3 != 1 и при отсутствии разветвления => mata360 -> a.child = 3 (еще нету второй ветки a.children = [3, 1]) ... (<a> здесь указана для удобства восприятия, на деле -> 0.child = ['3'])
            # добавляет к <root_children> => MAT.x.360 -> A.children = [3, +1] --> 0.children = [0.val='3', 1.val='1'] это структуры <Node> под индексом в массиве детей от элемента!

            # PS если ветки равные то программа дойдет до этой строки, если новая ветка короче (apple, app), то python выпадет в list index out of range при отсутствии 50-52 строк
            # 50-52 строка делает в дереве отметку что есть слово 'app' добавляя в ветку 'apple' флаг на [2].last = 'True' ([2].val = 'p') -> app.children['l'].children['e']
            root_children.append(new_first_children[0])

        new_branch = create_tree(word, 0)  # старт apple, a = 0 .. p = 1 ..
        merge_tree(self.root.children, [new_branch])

    # Функция осуществляющая поиск по дереву
    def search(self, word: str) -> bool:

        def checker(word, child_list, iter, stopper):
            if iter < len(word):
                for c in child_list:
                    if c.val == word[iter]:
                        return checker(word, c.children, iter+1, c.last)   # c.last = bool ветки, если mata360 -> 0.last = True тк последний элемент
                return False    # попадет сюда в случае, если есть ветка 'apple', а мы передали на вход -> 'applebanana'
            else:
                # если последняя буква сошлась и флаг последней буквы в слове выставлен
                if stopper:
                    return True
                return False

        node_list = self.root.children  # Вся структура дерева
        return checker(word, node_list, 0, False)

#___________[TRIES]____________________________________________________
t = Trie_main()
start_time = time.time()
#______________________________________________________________________

#___________[filling tree block]_______________________________________
for filename in fullArray:
    t.insert_in_tree(filename)
#______________________________________________________________________

#__________[searching]_________________________________________________
print("Travers files (tries): ")
for userfiles in userArray:
    if t.search(userfiles) == True:
        print(userfiles)
#______________________________________________________________________

#_______________[time]_________________________________________________
print(f"Searched by <tries> structure: {time.time() - start_time}sec.")
#______________________________________________________________________

# agra -> *.children[0.val = 'a', 0.children ->
#                                                0.val = 'g', 0.children ->
#                                                                            0.val = 'r', 0.children ->
#                                                                                                       0.val = 'a', 0.children -> x, 0.last = 'True']