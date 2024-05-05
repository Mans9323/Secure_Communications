import numpy as np

# Define the vectors
v = np.array([2, 6, 3])
w = np.array([1, 0, 0])
u = np.array([7, 7, 2])

# Calculate 3*(2*v - w)
result_vector = 3 * (2*v - w)

# Calculate 2*u
u_vector = 2 * u

# Calculate the dot product
dot_product = np.dot(result_vector, u_vector)

print(dot_product)