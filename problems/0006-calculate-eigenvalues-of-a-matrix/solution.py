from math import sqrt


def calcucalte_trace(matrix: list[list[int | float]]) -> int | float:
    trace = matrix[0][0] + matrix[1][1]

    return trace


def calculate_determiner(matrix: list[list[int | float]]) -> int | float:
    determiner = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    return determiner


def solve_quadratic_quation(trace_matrix: int | float, determiner: int | float) -> tuple[float,...]:
    trace_matrix = -trace_matrix

    eigenvalue_1 = (-trace_matrix + sqrt(trace_matrix ** 2 - 4 * 1 * determiner)) / 2
    eigenvalue_2 = (-trace_matrix - sqrt(trace_matrix ** 2 - 4 * 1 * determiner)) / 2
    
    return eigenvalue_1, eigenvalue_2


def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    trace_matrix = calcucalte_trace(matrix=matrix)
    determiner = calculate_determiner(matrix=matrix)
    eigenvalue_1, eigenvalue_2 = solve_quadratic_quation(trace_matrix=trace_matrix, determiner=determiner)

    eigenvalues = [eigenvalue_1, eigenvalue_2]

    return eigenvalues