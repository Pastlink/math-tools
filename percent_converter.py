from common_tools import cprint, is_int, to_num
from ratios_rate import simplify, ratio, rate


def input_to_fraction(data):
    # Convert data into a fraction, with this we get an equivalent for a
    # percentage.

    if "(" in data:
        pos = data.index("(")
        div = data.index("/")
        end = data.index(")")

        asd = float(data[:pos])
        num = float(data[pos + 1 : div])
        den = float(data[div + 1 : end])

        num = is_int((asd * den) + num)
        den = is_int(den * 100)

        data = f"{num}/{den}"

    return data


# Convert data to percent.
def percent(data):
    if "/" in data:
        num, den = to_num(*data.split("/"))
        data = num / den
    elif "%" in data:
        data = is_int(float(data[:-1])) / 100

    if not isinstance(data, float):
        data = float(data) / 100

    as_percent = is_int(round(data * 100, 2))

    return as_percent


# Use ratios() to get the ratio per cent.
def percent_to_ratio(percent_data, original_data=None):
    as_ratio = ratio(percent_data, 100)

    if as_ratio == "1/1" and original_data == "100":
        as_ratio = "100/100"

    return as_ratio


# Use rate() to divide the fraction.
def ratio_to_decimal(ratio_data):
    return is_int(round(float(rate(ratio_data)), 4))


def format_data(data):
    try:
        as_ratio = input_to_fraction(data)
        data = as_ratio
        as_percent = percent(data)
        as_ratio = simplify(*to_num(*as_ratio.split("/")))
    except TypeError:
        as_percent = percent(data)
        as_ratio = percent_to_ratio(as_percent, data)

    as_decimal = ratio_to_decimal(as_ratio)

    return as_percent, as_ratio, as_decimal


def print_result(data):
    as_percent, as_ratio, as_decimal = format_data(data)

    cprint("As Percent:", "GREEN", f"{as_percent}%")
    cprint("As Ratio:", "BLUE", as_ratio)
    cprint("As Decimal:", "RED", as_decimal)


def main():
    while True:
        data = input("Data: ")
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
    from tester import test_all

    to_test = [
        "100%",
        "4%",
        "17%",
        "52%",
        "125%",
        "37.5%",
        "18.4%",
        "9(1/2)",
        "8(1/2)",
        "5(1/3)",
        "6(2/3)",
    ]

    to_expect = [
        (100, "1/1", 1),
        (4, "1/25", 0.04),
        (17, "17/100", 0.17),
        (52, "13/25", 0.52),
        (125, "5/4", 1.25),
        (37.5, "3/8", 0.375),
        (18.4, "23/125", 0.184),
        (9.5, "19/200", 0.095),
        (8.5, "17/200", 0.085),
        (5.33, "4/75", 0.0533),
        (6.67, "1/15", 0.0667),
    ]

    test_all(format_data, to_test, to_expect)
