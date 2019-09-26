import cv2
import PIL
import pytesseract
import numpy
from sklearn.externals import joblib
from statistics import mode

# -*- coding: utf-8 -*-

# получение тестовой и проверка на ней
def get_values(raw_image):
    mass = []   # массив для вырез букв
    coord = []  # координаты изображений во всей картинке

    # open in format for PIL
    img = PIL.Image.open(raw_image)

    # resized the image
    newsize = tuple (2*x for x in img.size)

    # write back resized image to PIL format
    img = img.resize(newsize, PIL.Image.ANTIALIAS)
    img.save('out.png')

    # open and read imge
    img2 = cv2.imread ('out.png')

    # grayed the garbage inform like another color letters
    gray = cv2.cvtColor (img2, cv2.COLOR_BGR2GRAY)

    # set the limit for black - white bukva
    ret, tresh = cv2.threshold (gray, 127, 255, 0)

    # array of one's in matrix for make letter BOLD
    kernel = numpy.ones((3,3))

    # Make letter BOLD with matrix
    edged = cv2.erode(tresh, kernel)

    # поиск контура методом поиска соседних единиц толстой буквы и выстраивания контура + иерархия(h)
    contours, h = cv2.findContours (edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # убираем контур листа вокруг всего текста выстраиванием от самого большого контура до меньшего
    sorted (contours, key = cv2.contourArea, reverse = True)

    # для каждого контура из массива кроме контура листа[1:]
    i = 0
    for c in contours[1:]:

        #выстраивание квадратов вокруг каждого (получение координат)
        [x, y, w, h] = cv2.boundingRect(c)

        #дубликат для прямоугольников [строка-2]
        r = cv2.boundingRect(c)

        # возьми картинку контура и вырежи его из общей картинки (от координаты вверхней-левой и нижней правой - вектор)
        roi = tresh[y:y+h, x:x+w]

        # показать название картинки
        cv2.imshow (f"Тестовая {i}", roi)
        i += 1
        key = cv2.waitKey()

        # enter
        if key == 13:
            mass.append(roi)
            coord.append([x, y, w, h])
        # escape
        elif key == 27:
            break

    return  mass, coord


# Обучение knearest
def get_num_rects (chrims, s_list, r_list):
    knn = cv2.ml.KNearest_create()

    print(len(s_list))
    print(len(r_list))

    # обучение и сравнение
    knn.train(s_list, cv2.ml.ROW_SAMPLE, r_list)
    coord = []

    for i, chrim in enumerate(chrims):
        roismall = cv2.resize(chrim, (15, 10))
        smpl = roismall.reshape((1, 150))
        smpl = smpl.astype('float32')
        ret, results, neighbours, dist = knn.findNearest(smpl, 3)

        print(chr(results))
    return chr(results)     # возврат букв после обучения

# Обучение на изображении
def number_of_pages_determination (raw_image):
    mass = []

    # open in format for PIL
    img = PIL.Image.open(raw_image)

    # resized the image
    newsize = tuple (2*x for x in img.size)

    # write back resized image to PIL format
    img = img.resize(newsize, PIL.Image.ANTIALIAS)
    img.save('out.png')

    # open and read imge
    img2 = cv2.imread ('out.png')

    # grayed the garbage inform like another color letters
    gray = cv2.cvtColor (img2, cv2.COLOR_BGR2GRAY)

    # set the limit for black - white bukva
    ret, tresh = cv2.threshold (gray, 127, 255, 0)

    # array of one's in matrix for make letter BOLD
    kernel = numpy.ones((3,3))

    # Make letter BOLD with matrix
    edged = cv2.erode(tresh, kernel)

    # поиск контура методом поиска соседних единиц толстой буквы и выстраивания контура + иерархия(h)
    contours, h = cv2.findContours (edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # убираем контур листа вокруг всего текста выстраиванием от самого большого контура до меньшего
    sorted (contours, key = cv2.contourArea, reverse = True)

    # проверка
    print(len(contours))

    # для каждого контура из массива кроме контура листа[1:]
    for c in contours[1:]:
        #выстраивание квадратов вокруг каждого (получение координат)
        [x, y, w, h] = cv2.boundingRect(c)
        print(x, y, w,h)

        #дубликат для прямоугольников [строка-2]
        r = cv2.boundingRect(c)

        # возьми картинку контура и вырежи его из общей картинки (от координаты вверхней-левой и нижней правой - вектор)
        roi = tresh[y:y+h, x:x+w]

        # вокруг каждого контура рисуем квадрат
        cv2.rectangle(img2, r, (255,100,0), 1)
        mass.append(roi)

    # инициализация
    try:
        temp_r = joblib.load("keyboard.pkl")
        temp_s = joblib.load("letter.pkl")

    except:
        temp_r = []  # для ввода
        temp_s = numpy.empty((1, 150))  # для изображений

    # обучение выборкой
    i = 0
    for m in mass:
        cv2.imshow(f'Обучающая {i}', m)
        i += 1
        key = cv2.waitKey()
        if key == 27:
            break
        else:
            temp_r.append(key)
            roismall = cv2.resize(m, (15, 10))
            smpl = roismall.reshape((1, 150))
            temp_s = numpy.append(temp_s, smpl, 0)  # библиотекой берем список и записываем туда smpl = матрцца буква в строку
    temp_s = temp_s[1:].astype("float32")
    temp_r = numpy.array(temp_r)
    temp_r = temp_r.astype("float32")

    print(temp_s)
    print(temp_r)

    for r in temp_r:
        print(chr(r))

    # get_num_rects(temp_s, temp_r)   #learn

    # запись в файл
    joblib.dump(temp_r, "keyboard.pkl")
    joblib.dump(temp_s, "letter.pkl")

def main():
    raw_image = "e.png"
    number_of_pages_determination(raw_image)

    # получение из фотографии вырезанные буквы в
    test_imgs, coordin = get_values (raw_image)

    r_list = joblib.load("keyboard.pkl")
    s_list = joblib.load("letter.pkl")

    bukv = get_num_rects(test_imgs, s_list, r_list)        # передача эскизов всех букв (test_imgs), s_list (матрицы букв),

    # create_text(coordin, bukv)

if __name__ == '__main__':
    main()
