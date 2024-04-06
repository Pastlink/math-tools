from common_tools import check_if_int, clean_string, colorize
from math import sqrt
from tester import test_all


def square(n):
    return n * n


def square_root(n):
    if n < 0:
        return check_if_int(sqrt(n)) * -1

    return check_if_int(sqrt(n))


def print_result(data):
    if len(data) == 0:
        print(colorize("No valid parameters!", "RED"))
    else:
        data = check_if_int(float(data))
        print(f'{colorize(f'{data}²', "BLUE")} =', square(data))
        print(f'{colorize(f'√{data}', "GREEN")} =', square_root(data))


def main():
    while True:
        data = input("Find square and square root of: ")
        if data:
            try:
                print_result(clean_string(data))
            except ValueError:
                print("Invalid input.")
                continue
        else:
            print("Back...")
            break


if __name__ == "__main__":
    ### TEST square
    to_test = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]
    to_expect = [
        1,
        4,
        9,
        16,
        25,
        36,
        49,
        64,
        81,
        100,
        121,
        144,
        169,
        196,
        225,
    ]

    test_all(square, to_test, to_expect)

    ### TEST square_root
    to_test = [
        1,
        4,
        9,
        16,
        25,
        36,
        49,
        64,
        81,
        100,
        121,
        144,
        169,
        196,
        225,
    ]
    to_expect = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]

    test_all(square_root, to_test, to_expect)
