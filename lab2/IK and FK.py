
import numpy as np
from math import atan2,atan, sqrt, asin, cos, sin, acos
PI = 3.141592653589793

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

    return [0.4, 0.4, 0.3, 1, 0.8, 0.9]
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
                         [0, cos(q), -sin(q), 0],
                         [0, sin(q), cos(q), 0],
                         [0, 0, 0, 1]
                         ])

    def R_y(self, q):
        return np.array([[cos(q), 0, sin(q), 0],
                         [0, 1, 0, 0],
                         [-sin(q), 0, cos(q), 0],
                         [0, 0, 0, 1]
                         ])

    def R_z(self, q):
        return np.array([[cos(q), -sin(q), 0, 0],
                         [sin(q), cos(q), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]
                         ])
def FK(q, l):
    from numpy.linalg import multi_dot

    f = Formulas()


    T = multi_dot([f.T_z(l[0]), f.R_z(q[0]), f.T_x(l[1]), f.R_y(q[1]),f.T_z(l[2]),
                f.R_y(q[2]),f.T_z(l[3]), f.T_x(l[4] + l[5]),f.R_x(q[3]),
                                            f.R_y(q[4]), f.T_x(l[6]),f.R_x(q[5])])
    return T
#тут запускаем нашу FK

def IK(T):
    f = Formulas()
    qr = q()
    L = l()
    x = T[0][3]
    y = T[1][3]
    z = T[2][3]
#calculate atan2
    q1 = atan2(y, x)
    print("Our Q1:")
    print(q1)
    ac = sqrt(y*y + x*x)
    dd = (L[4] + L[5])
    alpha = acos((L[2]*L[2] + ac*ac - dd*dd)/(2*L[2]*ac))
    q2 = 90/180 * PI - q1 -alpha
    beta = asin((ac*sin(alpha))/(dd))
    print("Our Q2:")
    print(q2)
    print("Our Q3:")
    q3 = PI - beta - PI/2
    print(q3)


    Rw = np.linalg.inv(np.dot(f.R_z(qr[0]), np.dot(f.R_y(qr[1]) , f.R_y(qr[2]) )) )
    Rw = np.dot(Rw, T)
    if Rw[0][0] != 1:
        q4 = atan2(Rw[1][0], -Rw[2][0])
        print("Our Q4:")
        print(q4)
        q6 = atan2(Rw[0][1], Rw[0][2])
        print("Our Q6:")
        print(q6)
        if Rw[0][2] != 0:
            q5 = atan2(Rw[0][2]/cos(q6), Rw[0][0])
        else:
            q5 = atan2(Rw[0][1]/cos(q6), Rw[0][0])
        print("Our Q5:")
        print(q5)




T = FK(q(), l())
print(T)
print(IK(T))
