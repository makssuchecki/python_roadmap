import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A + B
A - B
A @ B 
A * B

A.T
np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eig(A)

np.eye(3)
np.zeros((3,3))
np.ones((2, 4))
np.random.rand(3, 3)
