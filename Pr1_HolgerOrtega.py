# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:23:11 2019
PRACTICAL 1. MATRICES IN PYTHON
@author: hortega
"""
import numpy as np
import fMLW

B = mPr1['B']
C = mPr1['C']
D = mPr1['D']
M = mPr1['M']
G = mPr1['G']
A = np.zeros((100, 21))
A[84][11]=-100
for i in range(100):
    A[i][0]=i+1
    for j in range(21):
        if j>17:
            A[i][j]=8
            
#bc = np.vstack((B,C))
bc = np.concatenate((B,C),axis=0)
E = np.concatenate((D.T,bc),axis=1)
# 5. MATRIX MULTIPLICATION *****************************
F = np.matmul(A,E)
# 6. SEARCH FOR ELEMENT (54,374)******************
ele = F[53][373]
# 7. TEST MYTRIPLICATOR 1 ******************
M1 = np.array([[1, 0, 0],[0, 1, 1]])
A1 = np.array([[1, 2, 3],[4, 5, 6]])
#A1 = np.array([1, 2, 3])
X1 = fMLW.myTriplicator(M1,A1)
# 8. TEST MYTRIPLICATOR 2 ******************
X_8 = fMLW.myTriplicator(M,F)
# 9. SUM ELEMENTS ******************
suma = np.sum(X_8)
# 10. TEST extractEquals 1 ******************
M2 = np.array([[1, 2, 3],[4, 5, 6]])
A2 = np.array([[1, 8, 9],[7, 5, 4]])
X2 = fMLW.extractEquals(M2,A2)
# 11. TEST extractEquals 2 ******************
X_11 = fMLW.extractEquals(F,G)
# 12. SUM ******************
suma2 = np.sum(X_11)
nnz = np.count_nonzero(X_11)