# -*- coding: utf-8 -*-
"""
A polynomial optimization problem of commutative variables. It is mentioned in
Section 5.12 of the following paper:

Henrion, D.; Lasserre, J. & Löfberg, J. GloptiPoly 3: moments, optimization and
semidefinite programming. Optimization Methods & Software, 2009, 24, 761-779

Created on Thu May 15 12:12:40 2014

@author: wittek
"""
import numpy as np
from ncpol2sdpa import SdpRelaxation, generate_variables

W = np.diag(np.ones(8), 1) + np.diag(np.ones(7), 2) + np.diag([1, 1], 7) + \
    np.diag([1], 8)
W = W + W.T
n = len(W)
e = np.ones(n)
Q = (np.diag(np.dot(e.T, W)) - W) / 4

x = generate_variables(n, commutative=True)
equalities = [xi ** 2 - 1 for xi in x]

objective = -np.dot(x, np.dot(Q, np.transpose(x)))

level = 1

sdpRelaxation = SdpRelaxation(x)
sdpRelaxation.get_relaxation(level, objective=objective, equalities=equalities,
                             removeequalities=True)
sdpRelaxation.write_to_file("max_cut.dat-s")
