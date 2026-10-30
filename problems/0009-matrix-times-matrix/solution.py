import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    a_matrix = np.array(a)
    b_matrix = np.array(b)

    if a_matrix.shape[1] != b_matrix.shape[0]:
        return -1

    return np.matmul(a_matrix, b_matrix)
