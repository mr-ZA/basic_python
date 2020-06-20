import pygame
import random
from pprint import pprint as pp
import numpy
import threading

class hThread (threading.Thread):
    def __init__(self, name, counter, flag_f, obj_game):
        threading.Thread.__init__(self)

        self.threadID = counter
        self.name = name
        self.counter = counter
        self.flag_function = flag_f
        self.obj_game = obj_game
        self.threadLock = threading.Lock()

    def run(self):
        # Получить блокировку для синхронизации потока
        self.threadLock.acquire()
        print("Starting " + self.name + str(self.counter))
        self.obj_game.re_gen_matrix(self.flag_function)

        # Снять блокировку для следующего потока
        self.threadLock.release()
        print("Exiting " + self.name + str(self.counter))

class Game():
    def __init__(self, width: int=640, height: int=480, cz: int=10, speed: int=100) -> None:
        self.width = width
        self.height = height
        self.cell_size = cz
        self.speed = speed  # speed of simulation

        # Main window
        self.screen = pygame.display.set_mode(size=[self.width, self.height])

        # Quantity of cells in hor and vert
        self.cell_width = self.width // self.cell_size      # кол-во клеток в ширину
        self.cell_height = self.height // self.cell_size    # кол-во клеток в длину

        # Coordinates of neighbours for update in next generation
        self.coord_update_dead = []
        self.coord_update_reborn = []

    def draw_lines(self) -> None:
        self.screen.fill(pygame.Color("white"))
        #pygame.display.flip()       # flip (updating screen) everywhere for debug purposes

        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))      # (0,0) = [X,Y]; (0,480) = [0,480] in coordinates
                                                            # (10,0) = [x,y]; (10,480) = [10,480] draw vertically(x ↑ y) by [x and y]
            #pygame.display.flip()

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))       # (0,0) = [x,y]; (640,0) = [640, 0] draw horizontally(y ← x)
                                                            # (0,10) = [x,y]; (640,10) = [10, 640] draw horizontally(y ← x)
            #pygame.display.flip()

    # надо учесть флаг randomize в будущем
    def create_grid(self, randomize: bool=False) -> list:
        """
            Создание списка клеток.

            Клетка считается живой, если ее значение равно 1, в противном случае клетка
            считается мертвой, то есть, ее значение равно 0.

            Parameters
            ----------
            randomize : bool
                Если значение истина, то создается матрица, где каждая клетка может
                быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

            Returns
            ----------
            out : Grid
                Матрица клеток размером `cell_height` х `cell_width`.
        """
        def get_number() -> int:
            numpy.random.seed()
            number = numpy.random.random()

            # округление (0 - клетка мертва, 1 - жива)
            if number > 0.4:
                number = 1
            else:
                number = 0
            return number

        matrix = []
        # 1 for -> заполнение столбцов = 0..длина поля по Y, шаг=10.
        # 2 for -> заполнение строки = 0..длина поля по X, шаг=10. 1 значение в строке = 1 клетка 10х10
        for i in range(0, self.cell_height):
            row = []     # временный массив для накопления строки с рандомами
            for z in range (0, self.cell_width):
                row.append(get_number())
            matrix.append(row)   # добавление в результирующ. матрицу строку с готовыми рандомными числами в ней

        return matrix

    # окрашивание ячеек 0 - мертвая = белая, 1 - живая = зеленая
    def draw_cells(self) -> None:
        for i in range(0, self.cell_height):
            for z in range(0, self.cell_width):
                if self.matrix[i][z] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('magenta'), (z * self.cell_size, i * self.cell_size, 9, 9))
                    pygame.display.flip()
                if self.matrix[i][z] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (z * self.cell_size, i * self.cell_size, 9, 9))
                    pygame.display.flip()

    def new_matrix_coord(self):
        self.matrix_new = []

        for num_y, column in enumerate(self.matrix):
            row2 = []

            for num_x, row in enumerate(column):
                row2.append([num_x, num_y])

            self.matrix_new.append(row2)

        print("New matrix of format: [\n\t\t\t\t\t\t[{номер_ЯЧ: [коордX, коордY]}]\n\t\t\t\t\t\t[{номер_ЯЧ: [коордX, коордY]}]\n\n\t\t\t\t\t]")

    def get_neighbours(self, arg_cell: list):
        """
            Вернуть список соседних клеток для клетки `cell`.

            Соседними считаются клетки по горизонтали, вертикали и диагоналям,
            то есть, во всех направлениях.

            Parameters
            ----------
            cell : Cell
                Клетка, для которой необходимо получить список соседей. Клетка
                представлена кортежем, содержащим ее координаты на игровом поле.

            Returns
            ----------
            out : Cells
                Список соседних клеток.
        """

        for string_matrix in self.matrix_new:
            for cell_one in string_matrix:
                if arg_cell == cell_one:
                    x = cell_one[0]
                    y = cell_one[1]
                
                    # частный случай левой верхней клетки:
                    if x == 0 and y == 0:
                        return [
                            [x + 0, y + (self.cell_height -1)],
                            [x, y + 1],
                            [x + (self.cell_width -1), y],
                            [x + 1, y],
                            [x + (self.cell_width -1), y + (self.cell_height -1)],
                            [x + 1, y + 1],
                            [999],
                            [999]
                        ]

                    # частный случай правой верхней клетки:
                    elif x == self.cell_width -1 and y == 0:
                        return [
                            [x, y + (self.cell_height -1)],
                            [x, y + 1],
                            [x - 1, y],
                            [x - (self.cell_width -1), y - 0],
                            [999],
                            [999],
                            [x - (self.cell_width -1), y + (self.cell_height -1)],
                            [x - 1, y + 1]
                        ]

                    # частный случай левой нижней клетки:
                    elif x == 0 and y == (self.cell_height - 1):
                        return [
                            [x, y - 1],
                            [x - 0, y - (self.cell_height -1)],
                            [x + (self.cell_width -1), y + 0],
                            [x + 1, y + 0],
                            [999],
                            [999],
                            [x + 1, y - 1],
                            [x + (self.cell_width -1), y - (self.cell_height -1)]
                        ]

                    # частный случай правой нижней клетки:
                    elif x == (self.cell_width -1) and y == (self.cell_height - 1):
                        return [
                            [x, y - 1],
                            [x - 0, y - (self.cell_height - 1)],
                            [x - 1, y],
                            [x - (self.cell_width -1), y - 0],
                            [x - 1, y - 1],
                            [x - (self.cell_width -1), y - (self.cell_height -1)],
                            [999],
                            [999]
                        ]

                    # общий частный случай для левого стобца без 3 левых соседей (y = 0, y = cell_height - 1 -> частные случаи)
                    elif x == 0 and y > 0 and y < (self.cell_height - 1):
                        return [
                            [x, y -1],
                            [x, y +1],
                            [x + (self.cell_width -1), y - 0],
                            [x +1, y],
                            [999],
                            [x +1, y +1],
                            [x +1, y -1],
                            [999]
                        ]

                    # общий частный случай для верхнего столбца без верхних соседей
                    elif x > 0 and x < (self.cell_width - 1) and y == 0:
                        return [
                            [x, y + (self.cell_height -1)],
                            [x, y +1],
                            [x -1, y],
                            [x +1, y],
                            [999],
                            [x +1, y +1],
                            [999],
                            [x -1, y +1]
                        ]

                    # общий частный случай для правого столбца без правых соседей
                    elif x == (self.cell_width -1) and y > 0 and y < (self.cell_height -1):
                        return [
                            [x, y -1],
                            [x, y + 1],
                            [x - 1, y],
                            [x - (self.cell_width -1), y],
                            [x -1, y -1],
                            [999],
                            [999],
                            [x -1, y +1]
                        ]

                    # общий частный случай для нижнего  столбца без нижних соседей
                    elif y == (self.cell_height -1) and x > 0 and x < (self.cell_width -1):
                        return [
                            [x, y -1],
                            [x, y - (self.cell_height - 1)],
                            [x -1, y],
                            [x +1, y],
                            [x - 1, y - 1],
                            [999],
                            [x +1, y -1],
                            [999]
                        ]

                    # общий случай для основных клеток [наконец-то :)]
                    else:
                        return [
                            [x, y -1],
                            [x, y +1],
                            [x -1, y],
                            [x +1, y],
                            [x -1, y -1],
                            [x +1, y +1],
                            [x +1, y -1],
                            [x -1, y +1]
                        ]
                else:
                    pass


    def neighbours_handling(self):
        # ____DBG____
        #print(self.matrix_new[0])  # 0 строка
        #print(self.matrix_new[0][3])  # 0 строка, 3 ячейка
        #neighbours_dbg = self.get_neighbours(self.matrix_new[0][3])
        #print(neighbours_dbg)

        # for every cell in new coordinate type matrix (current entity, no matter alive or dead)
        for string_coord_matrix in range(len(self.matrix_new)):  # we need 47 strings, cause len of matrix = 48
            for cell in range(len(self.matrix_new[string_coord_matrix])):
                neighbours = self.get_neighbours(self.matrix_new[string_coord_matrix][cell])
                neigh_counter_dead = 0
                neigh_counter_reborn = 0

                for n in range(len(neighbours)):
                    if neighbours[n][0] == 999:
                        continue

                    # coordinates for getting state of the neighbour cell
                    x_cord, y_cord = neighbours[n][0], neighbours[n][1]

                    if self.matrix[string_coord_matrix][cell] == 1 and self.matrix[y_cord][x_cord] == 1:
                        neigh_counter_dead += 1

                    if self.matrix[string_coord_matrix][cell] == 0 and self.matrix[y_cord][x_cord] == 1:
                        neigh_counter_reborn += 1

                # accordance to rules of simulation for dead entity
                if neigh_counter_dead < 2 or neigh_counter_dead > 3:
                    self.coord_update_dead.append(self.matrix_new[string_coord_matrix][cell])
                    pygame.draw.rect(self.screen, pygame.Color('white'), (cell * 10, string_coord_matrix * 10, 9, 9))

                # accordance to rules of simulation for re-born entity
                if neigh_counter_reborn == 3:
                    self.coord_update_reborn.append(self.matrix_new[string_coord_matrix][cell])
                    pygame.draw.rect(self.screen, pygame.Color('magenta'), (cell * 10, string_coord_matrix * 10, 9, 9))

        return

    def re_gen_matrix(self, flag_priority):
        """
        flag_priority: divide call for threading
        """
        def re_gen_matrix_dead():
            for string_coord_matrix in range(len(self.matrix_new)):  # we need 47 strings, cause len of matrix = 48
                for cell in range(len(self.matrix_new[string_coord_matrix])):
                    for cud in self.coord_update_dead:
                        if self.matrix_new[string_coord_matrix][cell] == cud:
                            self.matrix[string_coord_matrix][cell] = 0
                            break


        def re_gen_matrix_reborn():
            for string_coord_matrix in range(len(self.matrix_new)):  # we need 47 strings, cause len of matrix = 48
                for cell in range(len(self.matrix_new[string_coord_matrix])):
                    for cur in self.coord_update_reborn:
                        if self.matrix_new[string_coord_matrix][cell] == cur:
                            self.matrix[string_coord_matrix][cell] = 1
                            break

        if flag_priority == 1:
            re_gen_matrix_dead()

        if flag_priority == 2:
            re_gen_matrix_reborn()

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Life simulation")

        running = True

        self.draw_lines()
        pygame.display.flip()
        self.matrix = self.create_grid(True)
        self.draw_cells()
        self.new_matrix_coord()
        clock.tick(self.speed)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # if [x] pressed
                    running = False

                self.neighbours_handling()
                pygame.display.flip()

                # ____old way to re-generate(update) entity states in self.matrix structure
                self.re_gen_matrix(1)
                self.re_gen_matrix(2)
                clock.tick(self.speed)

                # re-generate Matrix in Threads (optimize)
                # obj_with_attrs = self
                # threads_list = []
                #
                # thread1 = hThread("Thread", 1, 1, obj_with_attrs)
                # thread2 = hThread("Thread", 2, 2, obj_with_attrs)
                #
                # thread1.start()
                # thread2.start()
                #
                # threads_list.append(thread1)
                # threads_list.append(thread2)
                #
                # for t in threads_list:
                #     t.join()
                #
                # if threading.active_count() <= 1:
                #     clock.tick(self.speed)
                #     continue
                # else:
                #     break
                #_________________________________________#

        pygame.quit()

if __name__ == "__main__":
    obj = Game()
    obj.run()