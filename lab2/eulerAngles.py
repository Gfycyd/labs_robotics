
from math import atan2, sqrt, acos
PI = 3.141592653589793


class task_1:

    def __init__(self):
        self.R = [
    [-1, 0.34, 1],
    [1, 0.90, 0],
    [1,- 0.3232, -0,2]
            ]
    #XYX
    def rad_angles(self, a,b,c):
        return str([a/PI * 180, b/PI * 180, c/PI * 180])[1:-1]
    def rot2eul(self):
        if self.R[0][0] != -1 and  self.R[0][0] != 1:
            print("--------------------------When sin(b) > 0 :  ----------------------------")
            a = atan2(self.R[1][0],-  self.R[2][0])
            c = atan2(self.R[0][1],  self.R[0][2])
            b = atan2(sqrt( self.R[1][0] * self.R[1][0] + self.R[2][0] * self.R[2][0]),  self.R[2][2])
            print(self.rad_angles(a,b,c))

            print("---------------------------When sin(b) < 0: -----------------------------")
            a = atan2(- self.R[1][0], self.R[2][0])
            c = atan2(- self.R[0][1], - self.R[0][2])
            b = atan2(-sqrt(self.R[1][0] * self.R[1][0] + self.R[2][0] * self.R[2][0]),  self.R[2][2])
            print(self.rad_angles(a, b, c))
        else:
            print("----------------------------When SINGULAR CASE--------------------------")
            b = acos(self.R[0][0])

            if (self.R[0][0] == 1):
                a = atan2(self.R[2][1], self.R[1][1])
                c = 0
            else:
                a = atan2(-self.R[2][1], -self.R[1][1])
                c = 0
            print(self.rad_angles(a, b, c))
        return a, b, c

#function,that implemets forward kinematics
#T – transformation matrix of current end-effector position (FK), or
#desired end-effector position (IK)
global T

#task_1
var_task_1 = task_1()
[a, b, c] = var_task_1.rot2eul()
#print([a,b,c])
