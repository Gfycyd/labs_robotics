import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from math import atan2, sqrt, asin, cos, sin

#данные для l и q
def l():
    return [
    670,
    312,
    1075,
    225,
    155.5,
    1025.5,
    215
 ]
def q():
    # q = [370, 136, 312, 720, 250, 720]
    # q = [130, 115, 125, 180, 180, 260]  # max speed

    return [10, 115, 12, 18, 18, 26]

class Formulas:

    def T_z(self, l):
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, l],
                         [0, 0, 0, 1]
                         ])

    def T_x(self, l):
        return np.array([[1, 0, 0, l],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]
                         ])

    def T_y(self, l):
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, l],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]
                         ])

    def R_x(self, q):
        return np.array([[1, 0, 0, 0],
                         [0, np.math.cos(q), -np.math.sin(q), 0],
                         [0, np.math.sin(q), np.math.cos(q), 0],
                         [0, 0, 0, 1]
                         ])

    def R_y(self, q):
        return np.array([[np.math.cos(q), 0, np.math.sin(q), 0],
                         [0, 1, 0, 0],
                         [-np.math.sin(q), 0, np.math.cos(q), 0],
                         [0, 0, 0, 1]
                         ])

    def R_z(self, q):
        return np.array([[np.math.cos(q), -np.math.sin(q), 0, 0],
                         [np.math.sin(q), np.math.cos(q), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]
                         ])


def FK(q, l):

    f = Formulas()
    T = np.dot(f.T_y(l[6]), f.R_y(q[5]))
    T = np.dot(f.R_x(q[4]), T)
    T = np.dot(f.T_y(l[5]), T)

    T = np.dot(f.R_y(q[3]), T)
    T = np.dot(f.T_y(l[4]), T)
    T = np.dot(f.T_z(l[3]), T)
    T = np.dot(f.R_x(q[2]), T)

    T = np.dot(f.T_z(l[1]), T)
    T = np.dot(f.R_x(q[1]), T)
    T = np.dot(f.T_y(l[1]), T)
    T = np.dot(f.T_z(l[0]), T)
    T = np.dot(f.R_z(q[0]), T)

    return T
#тут запускаем нашу FK
T = FK(q(), l())
print(T)
