import numpy as np

ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

ket_plus = (ket0 + ket1) / np.sqrt(2)


H  = np.array( [[1,1],[1,-1]])/np.sqrt(2)   # матрица Адамара

# преобразование ket0 в ket1 -  поворот на 180.

X = np.array([[0, 1], [1, 0]])    # соответсвует обычной операции NOT
# @ - матричное умножение

print( (X @ ket0 == ket1).all())       # .all() - проверит - являются ли все элементы массива true
