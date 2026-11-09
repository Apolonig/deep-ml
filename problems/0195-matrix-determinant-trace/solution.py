import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	determinant = np.linalg.det(matrix)

	trace = np.trace(matrix)

	return determinant, trace