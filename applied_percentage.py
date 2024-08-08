from common_tools import cprint, is_int, to_num, get_data_list, clean_array_data, clean_array_data_strict


def format_data(data: str) -> str:
    if "rise" in data:
        return increase_decrease_percent(data)
    if "percent" in data:
        return percent_of(data)
    if "plus" in data:
        return plus_percent(data)
    if "tax" in data:
        return tax_calculator(data)
    else:
        return calculate_percentage(data)


def increase_decrease_percent(data):
    ## USAGE: rise original to new
    original, new, money = money_checker(data)

    percent = is_int(((new - original) / original) * 100, 1)

    if percent > 0:
        in_or_de = "an increase"
    else:
        percent *= -1
        in_or_de = "a decrease"

    return f"{money}{new} is {in_or_de} of {percent}% to {money}{original}"


def percent_of(data):
    ## USAGE: 'What ??% of T (total) is R (result)
    T, R, money = money_checker(data)

    P = is_int((R / T) * 100, 2)

    return f"{P}% of {money}{T} is {money}{R}"


def plus_percent(data):
    ## USAGE: total plus ??%
    total, percent, money = money_checker(data)

    result = total + is_int((percent / 100) * total, 2)

    return f"{money}{total} plus {percent}% is {money}{result}"


### Might rewrite this later, right now it looks like a mess.
def calculate_percentage(data):
    ## USAGE: ??% of ? is what
    money_flag = False
    percent_flag = False
    percent = ""
    total_value = 0
    percent_value = 0
    decimal = 0
    total = 0
    for i in data:
        if percent_flag and money_flag:
            break

        percentage: bool = "%" in i
        money: bool = "$" in i

        if percentage:
            percent: str = i
            percent_value: float | int = data.index(i)
            decimal: float | int = is_int(float(i[:-1]) / 100, 4)
            percent_flag = True
        elif money:
            total: float | int = is_int(float(i[1:]))
            total_value: int = data.index(i)
            money_flag = True
        else:  # No money
            try:
                total: float | int = is_int(float(i))
                total_value: int = data.index(i)
            except ValueError:
                continue

    if money_flag:
        dlls = " $"
    else:
        dlls = " "

    if total_value > percent_value:
        result = is_int(total * decimal, 2)
        return f"{percent} of{dlls}{total} is{dlls}{result}"
    else:
        result = is_int(total / decimal, 2)
        return f"{percent} of{dlls}{result} is{dlls}{total}"
        

def tax_calculator(data):
    ## USAGE: The sales tax is ??% of the purchase price
    data = calculate_percentage(data).split(" ")

    tax_rate, purchase_price, sale_tax = tuple(clean_array_data_strict(data))

    total_cost = purchase_price + sale_tax

    return f"Tax rate:   {tax_rate}%\nSales tax:  ${sale_tax:.2f}\nTotal cost: ${total_cost:.2f}"


def money_checker(data):
    total, percent = tuple(clean_array_data(data))
    money = ""
    if isinstance(total, str) and "$" in total:
        total = total[1:]
        if isinstance(percent, str) and "$" in percent:
            percent = percent[1:]
        money = "$"
    if isinstance(percent, str) and "%" in percent:
        percent = percent[:-1]

    total, percent = to_num(total, percent)

    return total, percent, money


def print_result(data):
    cprint(format_data(data), "Blue")


def main() -> None:
    while True:
        data = get_data_list("Data: ")
        if data:
            try:
                print_result(data)
            except ValueError:
                cprint("Invalid input.", "Red")
                continue
        else:
            cprint("Back...", "Yellow")
            break


if __name__ == "__main__":
    from tester import test_all

    to_test = [
        ["$1.95", "is", "7.5%"],
        ["35%", "of", "90"],
        ["125%", "of", "28"],
        ["36", "is", "75%"],
        ["$1.17", "is", "6.5%"],
        ["percent", "of", "36", "is", "9"],
        ["percent", "of", "96", "is", "144"],
        ["$16", "is", "20%"],
        ["$108.10", "is", "11.5%"],
    ]
    to_expect = [
        "7.5% of $26 is $1.95",
        "35% of 90 is 31.5",
        "125% of 28 is 35",
        "75% of 48 is 36",
        "6.5% of $18 is $1.17",
        "25% of 36 is 9",
        "150% of 96 is 144",
        "20% of $80 is $16",
        "11.5% of $940 is $108.1",
    ]

    test_all(format_data, to_test, to_expect)
