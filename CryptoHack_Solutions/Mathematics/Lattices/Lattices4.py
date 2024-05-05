import numpy as np

A = np.array(
    [
        np.array((6, 2, -3)),
        np.array((5, 1, 4)),
        np.array((2, 7, 1)),
    ]
)

print("{0:.5f}".format(abs(np.linalg.det(A))))