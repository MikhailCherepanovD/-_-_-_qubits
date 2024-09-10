from Qubit import *
import numpy as np
KET_0 = np.array([[1], [0]], dtype = complex)
KET_1 = np.array([[0], [1]], dtype = complex)
H = np.array( [[1,1],[1,-1]], dtype = complex)/np.sqrt(2)   # матрица Адамара

class SimulatedQubit(Qubit):
    #  для хранения состояния кубита
    state: np.ndarray

    def __init__(self):
        self.reset()

    def h(self):
        self.state = H @ self.state

    def measure(self) -> bool:
        pr = np.abs(self.state[0, 0]) ** 2 # квадрат модуля амплитуды состояния числа состояния
        sample = np.random.random() <= pr
        return bool(sample)

    def reset(self):
        self.state = KET_0.copy()

#qsim = SimulatedQubit()
#print(qsim.measure)