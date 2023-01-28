import math


def round_decimals_down(number: float, decimals: int = 2):
    if not isinstance(decimals, int):
        raise TypeError("integer decimals")
    elif decimals < 0:
        raise ValueError("must have decimal places")
    elif decimals == 0:
        return math.floor(number)

    factor = 10 ** decimals
    return math.floor(number * factor) / factor


def absolute_error(precise: float, approximate: float):
    sub_operation = precise - approximate
    return abs(sub_operation)


def relative_error(precise: float, approximate: float):
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise
    return div_operation


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


if __name__ == '__main__':
    # Question 1
    s = 0
    c = (1 * 2 ** 10) + (1 * 2 ** 2) + (1 * 2 ** 1) + (1 * 2 ** 0)
    f = (1 * (1 / 2) ** 1) + (1 * (1 / 2) ** 2) + (1 * (1 / 2) ** 3) + (1 * (1 / 2) ** 5) + (1 * (1 / 2) ** 7) \
        + (1 * (1 / 2) ** 8) + (1 * (1 / 2) ** 9) + (1 * (1 / 2) ** 12)
    formula = ((-1) ** s) * (2 ** (c - 1023)) * (1 + f)
    float_number = float(formula)
    print(float_number, "\n")

    # Question 2
    scientific_value = float_number * 10 ** -3
    chopping = round_decimals_down(scientific_value, 3)
    print(chopping, "\n")

    # Question 3
    rounding = round(scientific_value, 3)
    print(rounding, "\n")

    # Question 4
    precise_val: float = scientific_value
    abs_value = absolute_error(scientific_value, rounding)
    print(round(abs_value, 7))
    print(relative_error(scientific_value, rounding), "\n")

    # Question 5
    print("no answer", "\n")

    # Question 6
    # Part a
    # Using the number of iterations formula of the bisection method
    a = -4
    b = 7
    tol = 0.0001
    x = math.log(b - a)
    y = math.log(tol)
    z = math.log(2)
    iteration_num = (x - y) / z
    round_iter = round(iteration_num, 0)
    format_iter = format_number(round_iter)
    print(format_iter)
