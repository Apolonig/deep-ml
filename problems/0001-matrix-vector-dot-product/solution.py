def dot_product(row: list[int|float], b: list[int|float]) -> int|float:
    multiplication = 0

    for ind, el_row in enumerate(row):
        multiplication += el_row * b[ind]

    return multiplication


def is_valid_operation(a: list[list[int|float]], b: list[int|float]) -> bool:
    for el in a:
        if len(b) != len(el):
            return False

    return True


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    result_list = []

    if not is_valid_operation(a=a, b=b):
        return -1
    
    for el in a:
        new_el = dot_product(row=el, b=b)
        result_list.append(new_el)

    return result_list