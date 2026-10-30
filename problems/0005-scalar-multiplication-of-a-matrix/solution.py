import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	atrix = np.array(matrix)

	return np.multiply(matrix, scalar)