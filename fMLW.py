# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:12:40 2019

@author: hortega
"""
import numpy as np

def myTriplicator(M,A):
    if np.shape(M)==np.shape(A):
        return A + 2*np.multiply(M,A)
    else:
        print("Matriz dimensions inconsistent!")

def extractEquals(A,B):
    if np.shape(A)==np.shape(B):
        X = A.copy()
        n_rows = A.shape[0]
        n_col = A.shape[1]
        for i in range(n_rows):
            for j in range(n_col):
                if A[i][j] != B[i][j]:
                    X[i][j]=0
        return X
    else:
        print("Matriz dimensions inconsistent!")