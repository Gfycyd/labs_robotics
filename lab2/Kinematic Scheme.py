import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle








H = np.array([[5.00459689e-01, 1.22176036e-01, -8.57095745e-01, 1.80197736e+03],
              [0.00000000e+00, -9.89992497e-01, -1.41120008e-01, 0.00000000e+00],
              [-8.65759839e-01, 7.06248753e-02, -4.95451337e-01, -1.44239936e+03],
              [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
#print(IK(H))


V = np.array([[-2.5, -1.5],
              [ 3,    0],
              [ 0,    3]])
X, Y = -10, 0
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((X - .1, Y - .1), 20, 30, fill=None, alpha=1))

X, Y = 200, 145
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((X - .1, Y - .1), 30, 10, fill=None, alpha=1))

X, Y = 100, 145
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((X - .1, Y - .1), 30, 10, fill=None, alpha=1))

plt.quiver([0], [0], V[:, 0], V[:, 1], color=['r', 'b', 'g'], scale=40)
plt.plot([0, 0], [0, 50])

V1 = np.array([[2.5, 1.5],
              [ 3,    0],
              [ 0,    3]])
plt.quiver([0], [50], V[:, 1], V1[:, 0], color=['b', 'g', 'r'], scale=40)
plt.plot([0, 50], [50,50])

V2 = np.array([[2.5, 1.5],
              [ 3,    0],
              [ 0,    3]])
plt.quiver([50], [50], V1[:, 1], V2[:, 0], color=['b', 'r', 'g'], scale=40)
plt.plot([50, 50], [50 ,100])


plt.quiver([50], [100], V[:, 1], V1[:, 0], color=['b', 'g', 'r'], scale=40)
plt.plot([50, 50], [100, 150])


plt.quiver([50], [150], V[:, 1], V1[:, 0], color=['b', 'g', 'r'], scale=40)
plt.plot([50, 110], [150,150])

plt.quiver([110], [150], V[:, 0], V[:, 1], color=['g', 'r', 'b'], scale=40)
plt.plot([110, 160], [150, 150])
V3 = np.array([[-2.5, -1.5],
              [ -3,    0],
              [ 0,    3]])
plt.quiver([160], [150], V[:, 1], V3[:, 0], color=['g', 'r', 'b'], scale=40)
plt.plot([160, 220], [150, 150])

plt.quiver([220], [150], V[:, 1], V1[:, 0], color=['r', 'b', 'g'], scale=40)

circle1 = plt.Circle((50, 50), 10, color='b', fill=False)
plt.gcf().gca().add_artist(circle1)

circle2 = plt.Circle((50, 100), 10, color='b', fill=False)
plt.gcf().gca().add_artist(circle2)

circle3 = plt.Circle((160, 150), 10, color='b', fill=False)
plt.gcf().gca().add_artist(circle3)

V2 = np.array([[-2.5, -1.5], [3, 0], [0, 3]])

plt.xlim(-30, 300)
plt.ylim(-30, 200)


plt.legend(["Начальные условия:  красная - Y; голубая - X; зеленая - Z."])
plt.show()
