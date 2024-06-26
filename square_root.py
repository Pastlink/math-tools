from common_tools import is_int, clean_string, cprint
from math import sqrt
from tester import test_all


def square(n) -> int | float:
    return n * n


def square_root(n) -> int | float:
    if n < 0:
        return is_int(sqrt(n * -1)) * -1

    return is_int(sqrt(n))


def print_result(data):
    if len(data) == 0:
        cprint("No valid parameters!", "RED")
    else:
        data = is_int(float(data))
        sq_root = round(square_root(data), 2)

        if isinstance(sq_root, float):
            equal = "≈"
        else:
            equal = "="

        cprint(f"{data}²", "BLUE", f"= {square(data)}")
        if data < 0:
            cprint(f"-√{data * -1}", "GREEN", f"{equal} {sq_root}")
        else:
            cprint(f"√{data}", "GREEN", f"{equal} {sq_root}")


def perfect_square_roots():
    perfect_squares = []

    while True:
        n = input("Number of perfect squares: ")
        if n:
            try:
                n = int(n)
                for i in range(1, n + 1):
                    perfect_squares.append((square(i), i))
                print_square_roots(perfect_squares)
                continue
            except ValueError:
                cprint("Invalid input!", "RED")
                continue
        break


def print_square_roots(array: list):
    for i, j in array:
        spacei, spacej = " ", " "
        if len(str(i)) == 1:
            spacei = "   "
        elif len(str(i)) == 2:
            spacei = "  "
        if len(str(j)) == 1:
            spacej = "  "
        length = len(f"|{spacei}{i} |{spacej}{j} |")

        print("|-" + f'{"-" * (length - 4)}' + "-|")
        print(f"|{spacei}{i} |{spacej}{j} |")
    print("-" * length)


def main():
    while True:
        data = input("Find square and square root of: ")
        if data == "perfect":
            perfect_square_roots()
        elif data:
            try:
                print_result(clean_string(data))
            except ValueError:
                cprint("Invalid input.", "RED")
                continue
        else:
            cprint("Back...", "YELLOW")
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
