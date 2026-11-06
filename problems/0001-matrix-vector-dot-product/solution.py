import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	a = np.array(a)
	b = np.array(b)

	if np.shape(a)[1] != np.shape(b)[0]:
		return -1

	return np.matvec(a, b)