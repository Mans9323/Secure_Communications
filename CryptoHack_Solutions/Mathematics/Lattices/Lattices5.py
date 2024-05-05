import numpy as np

u = np.array((87502093, 123094980))
v = np.array((846835985, 9834798552))

while True:
    if np.linalg.norm(v) < np.linalg.norm(u):
        u, v = v, u
    m = u.dot(v) // u.dot(u)
    if m == 0:
        break
    v = v - m * u

print(u)
print(v)
print(u.dot(v))