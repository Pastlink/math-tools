from common_tools import cprint, is_int, to_num, clean_array_data, get_data_list
from ratios_rate import ratio, rate


# Convert data to percent.
def percent(data):
    data = is_int(float(data))
    if not isinstance(data, float):
        data /= 100

    as_percent = is_int(round(data * 100, 2))

    return as_percent


# Use ratios() to get the ratio per cent.
def percent_to_ratio(percent_data, clean_data):
    num, den = ratio(percent_data, 100).split("/")
    num, den = to_num(num, den)

    if den > 100:
        cut = den / 100
        num /= cut
        den /= cut

    as_ratio = f"{is_int(num)}/{is_int(den)}"

    if as_ratio == "1/1" and clean_data == "100":
        as_ratio = "100/100"

    return as_ratio


# Use rate() to divide the fraction.
def ratio_to_decimal(ratio_data):
    return is_int(round(float(rate(ratio_data)), 4))


def clean_data(data):
    data = tuple(clean_array_data(data))
    if len(data) > 1:
        data = f"{data[0]}/{data[1]}"
    else:
        data = str(data[0])

    return data


def format_data(data):
    try:
        data = float(data[0]) / float(data[1])
    except ValueError:
        if "%" in data[0]:
            data = float(clean_data(data)) / 100
        else:
            data = clean_data(data)
            num, den = data.split("/")
            if not float(num) >= 100:
                data = ratio_to_decimal(data)
            else:
                data = num

    return data


def print_result(data):
    data = format_data(data)

    as_percent = percent(data)
    as_ratio = percent_to_ratio(as_percent, data)
    as_decimal = ratio_to_decimal(as_ratio)

    cprint("As Percent:", "GREEN", f"{as_percent}%")
    cprint("As Ratio:", "BLUE", as_ratio)
    cprint("As Decimal:", "RED", as_decimal)


def main():
    while True:
        data = get_data_list("Data: ")
        if data:
            try:
                print_result(data)
            except ValueError:
                cprint("Invalid input.", "RED")
                continue
        else:
            cprint("Back...", "YELLOW")
            break
