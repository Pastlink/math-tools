from common_tools import cprint, is_int, to_num
from ratios_rate import ratio, rate


# If data is a mixed number, convert data into an improper fraction,
# else convert data into decimal number.
# With this we get an equivalent for the percentage.
def is_mixed_number(data: str) -> str:
    if "(" in data:
        opn = data.index("(")
        div = data.index("/")
        cls = data.index(")")

        whl = float(data[:opn])
        num = float(data[opn + 1 : div])
        den = float(data[div + 1 : cls])

        num = is_int((whl * den) + num)
        den = is_int(den * 100)

        if data[cls + 1 :] == "%":
            data = f"{num}/{den}"
        else:
            data = f"{is_int((num / den) * 100)}"

    return data


# Convert data to percent.
def percent(data: str) -> float | int:
    fraction = "/" in data
    percentage = "%" in data

    if fraction and percentage:  # Check if data is a fraction of a percent.
        num, den = data.split("/")
        as_percent = float(num) / float(den[:-1])
    elif fraction:  # Check if data is just a fraction.
        num, den = to_num(*data.split("/"))
        as_percent = (num / den) * 100
    elif not percentage:  # Check if data is a decimal.
        as_percent = float(data) * 100
    else:  # We can conclude that data is in fact a percent already.
        as_percent = float(data[:-1])

    return is_int(round(as_percent, 2))


# Use ratio() to get the ratio per cent.
def percent_to_ratio(percent_data: float | int) -> str:
    return ratio(percent_data, 100)


# Use rate() to divide the fraction.
def ratio_to_decimal(ratio_data: str) -> float | int:
    return is_int(round(rate(ratio_data), 5))


# Calculate percentage, ratio and decimal values
def format_data(data: str) -> tuple[float | int, str, float | int]:
    data = is_mixed_number(data)
    as_percent = percent(data)
    if "%" not in data:
        as_ratio = ratio(*to_num(*data.split("/")))
    else:
        as_ratio = percent_to_ratio(as_percent)

    as_decimal = ratio_to_decimal(as_ratio)

    return as_percent, as_ratio, as_decimal


def print_result(data: str) -> None:
    as_percent, as_ratio, as_decimal = format_data(data)

    cprint("As Percent:", "BLUE", f"{as_percent}%")
    cprint("As Ratio:", "GREEN", as_ratio)
    cprint("As Decimal:", "RED", as_decimal)


def main() -> None:
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
        "5(1/3)%",
        "6(2/3)",
        "6(2/3)%",
        "6(4/5)",
        "6(4/5)%",
    ]

    to_expect = [
        (100, "1/1", 1),
        (4, "1/25", 0.04),
        (17, "17/100", 0.17),
        (52, "13/25", 0.52),
        (125, "5/4", 1.25),
        (37.5, "3/8", 0.375),
        (18.4, "23/125", 0.184),
        (950, "19/2", 9.5),
        (850, "17/2", 8.5),
        (533.33, "16/3", 5.33333),
        (5.33, "4/75", 0.05333),
        (666.67, "20/3", 6.66667),
        (6.67, "1/15", 0.06667),
        (680, "34/5", 6.8),
        (6.8, "17/250", 0.068),
    ]

    test_all(format_data, to_test, to_expect)
