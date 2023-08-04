#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:25:50 2023

@author: nebiyousamuel
"""

import numpy as np

# Coefficient matrix A
A = np.array([[2, -1, 3],
              [-1, 3, -1],
              [4, -4, 3]])

# Constants matrix B
B = np.array([10, -1, 3])

# Solve the system of equations
X = np.linalg.solve(A, B)

print("Solution:")
print(f"x1 = {X[0]}")
print(f"x2 = {X[1]}")
print(f"x3 = {X[2]}")
