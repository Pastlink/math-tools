from common_tools import get_data_list, clean_array_data, check_if_int, colorize, cprint
from fractions import Fraction
from tester import test_all


def ratios(numerator, denominator=1.0):
    num, den = Fraction(numerator), Fraction(denominator)
    ratio = str(Fraction(num, den).limit_denominator(max_denominator=1000000))

    if "/" not in ratio:
        ratio += "/1"

    return ratio


def rate(ratio):
    num, den = ratio.split("/")

    result = check_if_int(round(int(num) / int(den), 3))

    return f"{result}/1"


def print_result(data):
    params = tuple(clean_array_data(data))
    ratio = ratios(*params)

    if len(params) == 0:
        cprint("No valid parameters!", "RED")
    else:
        print(colorize("Ratio:", "BLUE"), ratio)
        print(colorize("Rate:", "GREEN"), rate(ratio))


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
            print("Back...")
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

    test_all(ratios, to_test, to_expect)

    to_test = [ratios(3.99, 24)]
    to_expect = ["0.166/1"]

    test_all(rate, to_test, to_expect)
