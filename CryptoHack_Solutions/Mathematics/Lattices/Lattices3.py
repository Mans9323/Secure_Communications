#!/usr/bin/env python3
import numpy as np
v = [
    np.array([4,1,3,-1]), 
    np.array([2,1,-3,4]), 
    np.array([1,0,-2,7]), 
    np.array([6,2,9,-5]),
]

"""
u1 = v1
Loop i = 2,3...,n
   Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
   Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
End Loop
"""
u = [v[0]]
for vi in v[1:]:
    mi = [np.dot(vi, uj) / np.dot(uj, uj) for uj in u]
    u += [vi - sum([mij * uj for (mij, uj) in zip(mi,u)])]

print(round(u[3][1], 5))