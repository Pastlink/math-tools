from common_tools import cprint, is_int, get_data_list, clean_array_data


def format_data(data: str) -> str:
    if "percent" in data:
        of_value: int = data.index("of")
        is_value: int = data.index("is")
        total, result = tuple(clean_array_data(data))

        if of_value < is_value:
            percent = is_int(result / total * 100, 2)
            return f"{percent}% of {total} is {result}."
        else:
            percent = is_int(total / result * 100, 2)
            return f"{percent}% of {result} is {total}."

    money_flag: bool = False
    for i in data:
        percentage: bool = "%" in i
        money: bool = "$" in i

        if percentage:
            percent: str = i
            percent_value: int = data.index(i)
            decimal: float | int = is_int(float(i[:-1]) / 100, 4)
        elif money:
            total: float | int = is_int(float(i[1:]))
            total_value: int = data.index(i)
            money_flag = True
        elif not money and not percentage:
            try:
                total: float | int = is_int(float(i))
                total_value: int = data.index(i)
            except ValueError:
                continue

    if total_value > percent_value:
        result = is_int(total * decimal, 2)
    else:
        result = is_int(total / decimal, 2)

    if money_flag:
        dlls = " $"
    else:
        dlls = " "

    if total_value > percent_value:
        return f"{percent} of{dlls}{total} is{dlls}{result}."
    else:
        return f"{percent} of{dlls}{result} is{dlls}{total}."


def print_result(data):
    cprint(format_data(data), "Blue")


def main() -> None:
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


if __name__ == "__main__":
    from tester import test_all

    to_test = [
        ["$1.95", "is", "7.5%", "of", "what", "number"],
        ["What", "number", "is", "35%", "of", "90"],
        ["125%", "of", "28", "is", "what", "number"],
        ["36", "is", "75%", "of", "what", "number"],
        ["$1.17", "is", "6.5%", "of", "what", "number"],
        ["What", "percent", "of", "36", "is", "9"],
        ["144", "is", "what", "percent", "of", "96"],
        ["$16", "is", "20%", "of", "what", "number"],
        ["$108.10", "is", "11.5%", "of", "what", "number"],
    ]
    to_expect = [
        "7.5% of $26 is $1.95.",
        "35% of 90 is 31.5.",
        "125% of 28 is 35.",
        "75% of 48 is 36.",
        "6.5% of $18 is $1.17.",
        "25% of 36 is 9.",
        "150% of 96 is 144.",
        "20% of $80 is $16.",
        "11.5% of $940 is $108.1."
    ]

    test_all(format_data, to_test, to_expect)
