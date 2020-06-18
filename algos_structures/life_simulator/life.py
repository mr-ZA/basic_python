import pygame
import random
from pprint import pprint as pp
import numpy
import time

class Game():
    def __init__(self, width: int=640, height: int=480, cz: int=10, speed: int=10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cz
        self.speed = speed  # speed of simulation

        # Main window
        self.screen = pygame.display.set_mode(size=[self.width, self.height])

        # Quantity of cells in hor and vert
        self.cell_width = self.width // self.cell_size      # кол-во клеток в ширину
        self.cell_height = self.height // self.cell_size    # кол-во клеток в длину

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
                    pygame.draw.rect(self.screen, pygame.Color('magenta'), (z * 10, i * 10, 9, 9))
                    pygame.display.flip()
                if self.matrix[i][z] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (z * 10, i * 10, 9, 9))
                    pygame.display.flip()
        time.sleep(1)

    def new_matrix_coord(self):
        self.matrix_new = []
        number_of_cell = 0      # 640x480 -> 64x48 = 3072(cells)

        for num_y, column in enumerate(self.matrix):
            row2 = []

            for num_x, row in enumerate(column):
                row2.append([num_x, num_y])

            self.matrix_new.append(row2)

        try:
            if self.matrix_new[3072]:
                print(self.matrix_new[3072])
        except:
            print("[ERROR] such element doesn't exist in matrix of elements..")

        print("New matrix of format: [\n\t\t\t\t\t\t[{номер_ЯЧ: [коордX, коордY]}]\n\t\t\t\t\t\t[{номер_ЯЧ: [коордX, коордY]}]\n\n\t\t\t\t\t]")

    def get_neighbours(self):
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

        for matn in self.matrix_new:
            for x, y in matn:

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
                        [x - (self.cell_width -1), y + (self.cell_height -1)],
                        [999],
                        [999]
                    ]

                # общий частный случай для левого стобца без 3 левых соседей (y = 0, y = cell_height - 1 -> частные случаи)
                elif x == 0 and y > 0 and y < (self.cell_height - 1):
                    return [
                        [x, y -1],
                        [x, y +1],
                        [x - (self.cell_width -1), y - 0],
                        [x +1, y],
                        
                    ]



    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Life simulation")

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == False:
                    running = False

            self.draw_lines()
            pygame.display.flip()
            self.matrix = self.create_grid(True)
            self.draw_cells()
            self.new_matrix_coord()
            clock.tick(self.speed)

            self.get_neighbours()

        pygame.quit()

if __name__ == "__main__":
    obj = Game()
    obj.run()