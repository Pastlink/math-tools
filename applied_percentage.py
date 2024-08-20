from typing import Literal
from common_tools import cprint, is_int, get_data_list, clean_array_data_strict


def format_data(data: list[str]) -> str:
    for keyword in data:
        match keyword:
            case "rise":
                return increase_decrease_percent(data)
            case "percent":
                return percent_of(data)
            case "add":
                return add_percent(data)
            case "tax":
                return tax_calculator(data)
            case "discount":
                return discount(data)
            case _:
                return calculate_percentage(data)
    return "No data found."


def increase_decrease_percent(data: list[str]) -> str:
    ## USAGE: rise {original} to {new}
    original, new, money = is_money(data)

    percent = is_int(((new - original) / original) * 100, 1)

    if percent > 0:
        in_or_de = "an increase"
    elif percent < 0:
        percent *= -1
        in_or_de = "a decrease"
    else:
        return "No change."

    return f"{money}{new} is {in_or_de} of {percent}% to {money}{original}"


def percent_of(data: list[str]) -> str:
    ## USAGE: percent of {T} (total) is {R} (result)
    T, R, money = is_money(data)

    P = is_int((R / T) * 100, 2)

    return f"{P}% of {money}{T} is {money}{R}"


def add_percent(data: list[str]) -> str:
    ## USAGE: add {%} to {total}
    percent, total, money = is_money(data)

    result = total + is_int((percent / 100) * total, 2)

    return f"{money}{total} plus {percent}% is {money}{result}"


# Get relevant values and calculate percent based on wording
def calculate_percentage(data: list[str]) -> str:
    ## USAGE: {%} 'of' {value} or {value} 'is' {%}
    percent, value, money = is_money(data)
    invert_flag = False

    if "is" in data: # Invert values if first value 'is' the total'
        percent, value = value, percent
        invert_flag = True

    decimal = is_int(percent / 100, 4)

    if invert_flag:
        total = value
    else:
        total = is_int(decimal * value, 4)

    result = is_int(total / decimal, 2)
    return f"{percent}% of {money}{result} is {money}{total}"


def tax_calculator(data: list[str]) -> str:
    ## USAGE: tax is {%} of {purchase price}
    data = calculate_percentage(data).split(" ")

    tax_rate, purchase_price, sale_tax = tuple(clean_array_data_strict(data))
    total_cost = purchase_price + sale_tax

    return f"Tax rate:   {tax_rate}%\nSales tax:  ${sale_tax:.2f}\nTotal cost: ${total_cost:.2f}"


def discount(data: list[str]) -> str:
    ## USAGE: discount {%} of {price}
    # amount of discount = discount rate * original price
    # sale price = original price - discount
    discount_or_sale_price, original_price = tuple(clean_array_data_strict(data))
    percent_flag = False

    for i in data:
        if "%" in i:
            percent_flag = True

    if percent_flag:
        discount_rate = discount_or_sale_price / 100
    else:  # Most likely it is sale price
        discount_rate = (original_price - discount_or_sale_price) / original_price

    amount_of_discount = is_int(discount_rate * original_price, 2)
    sale_price = original_price - amount_of_discount

    return f"Discounted: ${amount_of_discount}\nTotal to pay: ${sale_price} ({is_int(discount_rate * 100, 2)}% off)"


def is_money(data: list[str]) -> tuple[float, float, Literal["", "$"]]:
    money = ""

    for i in data:
        if "$" in i:
            money = "$"

    val1, val2 = tuple(clean_array_data_strict(data))

    return val1, val2, money


def print_result(data) -> None:
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
        ["rise", "190", "to", "114"],
        ["rise", "15.50", "to", "17.55"],
        ["tax", "6.25%", "of", "$724"],
        ["tax", "8.2%", "of", "$250"],
        ["discount", "35%", "of", "$140"],
        ["discount", "$13.95", "of", "$31"],
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
        "114 is a decrease of 40% to 190",
        "17.55 is an increase of 13.2% to 15.5",
        "Tax rate:   6.25%\nSales tax:  $45.25\nTotal cost: $769.25",
        "Tax rate:   8.2%\nSales tax:  $20.50\nTotal cost: $270.50",
        "Discounted: $49\nTotal to pay: $91 (35% off)",
        "Discounted: $17.05\nTotal to pay: $13.95 (55% off)",
    ]

    test_all(format_data, to_test, to_expect)
