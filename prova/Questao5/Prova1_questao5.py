import cv2
import numpy as np
from numpy.linalg import inv
import math

p3d = np.array([[0, 1000, 200,1],[600,1000,400,1],[1000,800,400,1],[1000,400,600,1],[1000,1000,600,1],[1000,800,0,1]])
p2d = np.array([[5,3,1],[3,4,1],[2,4,1],[1,2,1],[2,3,1],[2,5,1]])

# A = C⁻¹ * P
C = []
for i in range(5):
  C.append([p3d[i][0],p3d[i][1],p3d[i][2],1,0,0,0,0, -p2d[i][0]*p3d[i][0], -p2d[i][0]*p3d[i][1], -p2d[i][0]*p3d[i][2]])
  C.append([0,0,0,0,p3d[i][0],p3d[i][1],p3d[i][2],1, -p2d[i][1]*p3d[i][0], -p2d[i][1]*p3d[i][1], -p2d[i][1]*p3d[i][2]])
C.append([p3d[5][0],p3d[5][1],p3d[5][2],1,0,0,0,0,   -p2d[5][0]*p3d[5][0], -p2d[5][0]*p3d[5][1], -p2d[5][0]*p3d[5][2]])
C = np.array(C)

P = []
for i in range(5):
  P.append([p2d[i][0]])
  P.append([p2d[i][1]])
P.append([p2d[5][0]])
P = np.array(P)

Cinv = np.linalg.inv(C)
A =  np.matmul(Cinv, P)

#transformando A em Mproj: uma matriz 3x4
Mproj = np.array([
    [A[0][0], A[1][0], A[2][0], A[3][0]],
    [A[4][0], A[5][0], A[6][0], A[7][0]],
    [A[8][0], A[9][0], A[10][0], 1]
])

# Ph = (c1, c2, c3) = Mproj * Q
# Pc = (xc, yc) = (c1/c3, c2/c3)
Q = np.array(p3d).T
Ph = np.matmul(Mproj, Q)
Ph = np.array(Ph).T
Pc = np.array([Ph[i]/Ph[i][-1] for i in range(len(Ph))])


accuracy = 0
for i in range (len(Pc)):
  x1 = Pc[i][0]
  y1 = Pc[i][1]
  x2 = p2d[i][0]
  y2 = p2d[i][1]
  accuracy+=math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2,2))

np.set_printoptions(suppress=True)
print("Mproj: \n", Mproj)
print("\nPoints: \n", Pc)
print("\nAccuracy: ", accuracy/6)


