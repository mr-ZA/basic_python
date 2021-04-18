import numpy as np

# нормализация вектора, компенсация разности и-ду весами
def find_normal(vec):
    return vec / len(vec)

# [] - вектор, [[]] - матрица

R = np.random.rand(12, 3)   # матрица весов (менчется в процессе подстройки вычислений)

vec1 = np.array([[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])     # политика_вектор ()
vec2 = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])     # экономика_вектор
vec3 = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]])     # спорт_вектор

# категории для поиска принадлежности результата к ней
polit_category_vec = [1, 0, 0]
econom_category_vec = [0, 1, 0]
sport_category_vec = [0, 0, 1]

# нормализация векторов 
vec1_normal = find_normal(vec1)
vec2_normal = find_normal(vec2)
vec3_normal = find_normal(vec3)

# исправления весов, правка сгенерированой матрицы для приближения к искомой категории

for i in range(500):
    # превращение матрицы 3-строки X 12 столбцов в матрицу искомую 1 Х 3
    res_1 = vec1_normal.dot(R)
    res_2 = vec2_normal.dot(R)
    res_3 = vec3_normal.dot(R)

    # отклонения от искомой категории (величина ошибки)
    error_cat_1 = pow(res_1 - polit_category_vec, 2)
    error_cat_2 = res_2 - econom_category_vec
    error_cat_3 = res_3 - sport_category_vec

    R = R - (0.1 * np.transpose(vec1_normal) * error_cat_1)
    if i % 1000 == 0:
        pass
    print(error_cat_1)

pass