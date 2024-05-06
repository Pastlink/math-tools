from common_tools import get_data_list, clean_array_data, is_int, cprint
from fractions import Fraction
from tester import test_all


def simplify(numerator, denominator):
    num, den = Fraction(numerator), Fraction(denominator)

    return str(Fraction(num, den).limit_denominator(max_denominator=1000000))


def ratio(numerator, denominator=1.0):
    ratio = simplify(numerator, denominator)

    if "/" not in ratio:
        ratio += "/1"

    return ratio


def rate(ratio):
    num, den = ratio.split("/")

    return is_int(float(num) / float(den))


def print_result(data):
    params = tuple(clean_array_data(data))
    if len(params) == 0:
        cprint("No valid parameters!", "RED")
    elif len(params) > 2:
        cprint("No more than 2 parameters!", "RED")
    else:
        ratios = ratio(*params)
        rates = round(rate(ratios), 3)
        cprint("Ratio:", "BLUE", ratios)
        cprint("Rate: ", "GREEN", f"{rates}/1")


def main():
    while True:
        data = get_data_list("Find ratio and rate of: ")
        if data:
            try:
                print_result(data)
            except ValueError:
                cprint("Invalid input.", "RED")
                continue
        else:
            cprint("Back...", "YELLOW")
            break


if __name__ == "__main__":
    to_test = [
        ("5/4", "19/8"),
        (249, 39),
        (48, 32),
        (27, 72),
        (51, 34),
        (1.5, 2.75),
        (0.8, 0.05),
        (4.8, 11.2),
        (2.7, 0.54),
        (4.6, 11.5),
        (2.3, 0.69),
        (3.4, 15.3),
        (3.4, 0.68),
        (1.75, 2.625),
        (1.125, 2.75),
    ]
    to_expect = [
        "10/19",
        "83/13",
        "3/2",
        "3/8",
        "3/2",
        "6/11",
        "16/1",
        "3/7",
        "5/1",
        "2/5",
        "10/3",
        "2/9",
        "5/1",
        "2/3",
        "9/22",
    ]

    test_all(ratio, to_test, to_expect)

    to_test = [ratio(3.99, 24)]
    to_expect = ["0.166/1"]

    test_all(rate, to_test, to_expect)
