import numpy as np


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    matrix = np.array(matrix)

    determine = np.linalg.det(matrix)

    if determine == 0:
        return None

    return np.linalg.inv(matrix)

# def calculate_determine(matrix: list[list[float]]) -> float:
#     determine = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

#     return determine


# def change_el_and_sign(matrix: list[list[float]]) -> list[list[float]]:
#     changed_matrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

#     return changed_matrix


# def divide_matrix(matrix: list[list[float]], determine: float) -> list[list[float]]:
#     result_matrix = matrix[:]
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             result_matrix[i][j] *= (1 / determine)

#     return result_matrix


# def calculate_inverse_matrix(matrix: list[list[float]], determine: float) -> list[list[float]]:
#     changed_matrix = change_el_and_sign(matrix=matrix)
#     result_matrix = divide_matrix(matrix=changed_matrix, determine=determine)

#     return result_matrix


# def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
#     determine = calculate_determine(matrix=matrix)

#     if determine == 0:
#         return None

#     inverse_matrix = calculate_inverse_matrix(matrix=matrix, determine=determine)

#     return inverse_matrix