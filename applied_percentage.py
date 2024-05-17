from common_tools import cprint, is_int, get_data_list, clean_array_data


def format_data(data):
    if "percent" in data:
        of_value = data.index("of")
        is_value = data.index("is")
        total, result = tuple(clean_array_data(data))

        if of_value < is_value:
            percent = is_int(round(result / total * 100, 2))
            return f"{percent}% of {total} is {result}."
        else:
            percent = is_int(round(total / result * 100, 2))
            return f"{percent}% of {result} is {total}."

    for i in data:
        percentage = "%" in i
        money = "$" in i

        # print("Looking at:", i)

        if percentage:
            percent = i
            percent_value = data.index(i)
            decimal = is_int(round((float(i[:-1]) / 100), 4))
            # cprint("Percent:", "GREEN", percent)
            # cprint("Decimal:", "GREEN", decimal)
        elif money:
            total = is_int(float(i[1:]))
            total_value = data.index(i)
            # cprint("Total money:", "GREEN", total)
        elif not money and not percentage:
            try:
                total = is_int(float(i))
                total_value = data.index(i)
                # cprint("Total:", "GREEN", total)
            except ValueError:
                # cprint("Skipped.", "RED")
                continue

    if total_value > percent_value and not money:
        # cprint("Multiply!", "YELLOW")
        result = is_int(round(total * decimal, 2))
    else:
        # cprint("Divide!", "YELLOW")
        # print(f"{total} / {decimal} = {total / decimal}")
        result = is_int(round(total / decimal, 2))

    if money:
        return f"{percent} of ${result} is ${total}."
    elif total_value < percent_value:
        return f"{total} is {percent} of {result}."
    else:
        return f"{percent} of {total} is {result}."


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
        ["6.5%", "of", "what", "number", "is", "$1.17"],
        ["What", "number", "is", "35%", "of", "90"],
        ["125%", "of", "28", "is", "what", "number"],
        ["36", "is", "75%", "of", "what", "number"],
        ["6.5%", "of", "what", "number", "is", "$1.17"],
        ["What", "percent", "of", "36", "is", "9"],
        ["144", "is", "what", "percent", "of", "96"],
        ["20%", "of", "what", "number", "is", "$16"]
    ]
    to_expect = [
        "6.5% of $18 is $1.17.",
        "35% of 90 is 31.5.",
        "125% of 28 is 35.",
        "36 is 75% of 48.",
        "6.5% of $18 is $1.17.",
        "25% of 36 is 9.",
        "150% of 96 is 144.",
        "20% of $80 is $16."
    ]

    test_all(format_data, to_test, to_expect)
