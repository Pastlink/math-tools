from typing import Literal
from common_tools import cprint, is_int, get_data_list, clean_array_data_strict, list_options

def format_data(function: str) -> None:
    try:
        function = int(function)
    except ValueError:
        pass

    match function:
        case 1:
            while True:
                data = ask_function_data(simple_interest.__name__, "Data: ")

                if data:
                    original, new, money, percent = increase_decrease_percent(data)
                    in_or_de = check_increase_decrease(percent)

                    if in_or_de == "No change.":
                        cprint(in_or_de)
                        continue
                else:
                    cprint("Back...", "yellow")
                    return

                cprint(f"{money}{new} is {in_or_de} of {percent}% to {money}{original}")
        case 2:
            cprint("Usage: percent of {T} (total) is {R} (result)", "YELLOW")
            while True:
                data = ask_function_data(percent_of.__name__, "Data: ")

                if data:
                    total, result, money, percent = percent_of(data)
                else:
                    cprint("Back...", "yellow")
                    return

                cprint(f"{percent}% of {money}{total} is {money}{result}")
        case 3:
            cprint("Usage: add {%} to {total}", "YELLOW")
            while True:
                data = ask_function_data(add_percent.__name__, "Data: ")

                if data:
                    percent, total, money, result = add_percent(data)
                else:
                    cprint("Back...", "yellow")
                    return

                cprint(f"{money}{total} plus {percent}% is {money}{result}")
        case 4:
            cprint("USAGE: tax is {%} of {purchase price}", "YELLOW")
            while True:
                data = ask_function_data(tax_calculator.__name__, "Data: ")

                if data:
                    tax_rate, sale_tax, total_cost = tax_calculator(data)
                else:
                    cprint("Back...", "yellow")
                    return

                cprint(f"Tax rate:   {tax_rate}%\nSales tax:  ${sale_tax:.2f}\nTotal cost: ${total_cost:.2f}")
        case 5:
            cprint("USAGE: discount {$/%} of {original_price} or discount {$/%} to {original_price}", "YELLOW")
            while True:
                data = ask_function_data(discount.__name__, "Data: ")

                if data:
                    discount_rate, amount_of_discount, sale_price = discount(data)
                else:
                    cprint("Back...", "yellow")
                    return

                f"Discounted: ${amount_of_discount}\nSale Price: ${sale_price} ({is_int(discount_rate * 100, 2)}% off)"
        case 6:
            cprint("Usage: {%} of {$} (wholesale price)", "YELLOW")
            while True:
                data = ask_function_data(mark_up.__name__, "Data: ")

                if data:
                    _, wholesale_price, amount_of_mark_up, list_price = mark_up(data)
                else:
                    cprint("Back...", "yellow")
                    return

                cprint("Wholesale Price:$", "blue", f"${wholesale_price:.2f}")
                cprint("Mark-up:", "blue", f"${amount_of_mark_up:.2f}")
                cprint("List Price:", "blue", f"${list_price:.2f}")
        case 7:
            cprint("Usage: {Interest} {Principal} {rate} {time} 'years' or 'months'", "YELLOW")
            while True:
                data = ask_function_data(simple_interest.__name__, "Data: ")

                if data:
                    if len(data) != 5:
                        cprint("Usage: {Interest} {Principal} {rate} {time} 'years' or 'months'", "red")
                        continue
                    interest, principal, rate = simple_interest(data)
                else:
                    cprint("Back...", "Yellow")
                    return

                cprint("Interest: ", "blue", f"${interest:.2f}")
                cprint("Principal:", "blue", f"${principal:.2f}")
                cprint("Rate:     ", "blue", f"{is_int(rate*100, 2)}%")
        case _:
            try:
                percent, money, decimal, total, result  = calculate_percentage(function.split(" "))
                cprint(f"{percent}% of {money}{result} is {money}{total}")
            except ValueError:
                cprint("Use the name of the function. Please try again.", "YELLOW")


def increase_decrease_percent(data: list[str]) -> tuple[float, float, Literal['', '$'], float | int]:
    ## USAGE: rise {original} to {new}
    original, new, money = is_money(data)

    percent = is_int(((new - original) / original) * 100, 1)

    return original, new, money, percent


def check_increase_decrease(percent_data: float) -> Literal['No change.', 'an increase', 'a decrease']:
    if percent_data > 0:
        in_or_de = "an increase"
    elif percent_data < 0:
        percent_data *= -1
        in_or_de = "a decrease"
    else:
        return "No change."

    return in_or_de


def percent_of(data: list[str]) -> tuple[float, float, Literal['', '$'], float | int]:
    ## USAGE: percent of {T} (total) is {R} (result)
    ## Also works to discover the 'commission rate'.
    total, result, money = is_money(data)

    percent = is_int((result / total) * 100, 2)

    return total, result, money, percent


def add_percent(data: list[str]) -> tuple[float, float, Literal['', '$'], float]:
    ## USAGE: add {%} to {total}
    percent, total, money = is_money(data)

    result = total + is_int((percent / 100) * total, 2)

    return percent, total, money, result


# Get relevant values and calculate percent based on wording
def calculate_percentage(data: list[str]) -> tuple[float, Literal['', '$'], float | int, float | int, float | int]:
    ## USAGE: {%} 'of' {value} or {value} 'is' {%}
    ## Also works for 'commissions' calculation.
    percent, value, money = is_money(data)
    substract_flag = False

    if "is" in data: # Invert values if first value 'is' the total
        percent, value = value, percent
        substract_flag = True

    decimal = is_int(percent / 100, 5)

    if substract_flag:
        total = value
    else:
        total = is_int(decimal * value, 4)

    result = is_int(total / decimal, 2)
    return percent, money, decimal, total, result

### Add way to know tax rate if one isn't given. tax_rate = sale_tax/purchase_price
## Could just use percent_of() instead
def tax_calculator(data: list[str]) -> tuple[float, float | int, float | int]:
    ## USAGE: tax is {%} of {purchase price}
    percent, _, decimal, total, result = calculate_percentage(data)

    tax_rate, purchase_price, sale_tax = percent, result, total
    total_cost = purchase_price + sale_tax

    return tax_rate, sale_tax, total_cost


def discount(data: list[str]) -> tuple[float, float | int, float | int]:
    ## USAGE: discount {$/%} of {original_price} or discount {$/%} to {original_price}
    # amount of discount = discount rate * original price
    # sale price = original price - discount
    discount_or_sale_price, original_price = tuple(clean_array_data_strict(data))
    percent_flag = False
    substract_flag = False

    for i in data:
        if "%" in i:
            percent_flag = True
        elif "to" == i and not percent_flag:
            substract_flag = True

    if percent_flag: # If working with percent
        discount_rate = discount_or_sale_price / 100
    elif substract_flag: # If substracting from {original_price}
        discount_rate = discount_or_sale_price / original_price
    else: # If paying {discount_or_sale_price} of {original_price}
        discount_rate = (original_price - discount_or_sale_price) / original_price

    amount_of_discount = is_int(discount_rate * original_price, 2)
    sale_price = is_int(original_price - amount_of_discount, 2)

    return discount_rate, amount_of_discount, sale_price


def mark_up(data: list[str]) -> tuple:
    ## USAGE: markup {%} of {$} (wholesale price)

    mark_up_rate, wholesale_price = tuple(clean_array_data_strict(data))

    amount_of_mark_up = is_int((mark_up_rate / 100) * wholesale_price, 2)
    list_price = wholesale_price + amount_of_mark_up

    return mark_up_rate, wholesale_price, amount_of_mark_up, list_price


def simple_interest(data: list[str]) -> tuple[float | int, float | int, float | int]:
        I, P, r, t = tuple(clean_array_data_strict(data))

        if t == 0:
            t = (I / P) / r

        if "m" in data:
            t = t / 12

        if r != 0:
            r = r/100
        else:
            r = I / (P * t)

        if I == 0:
            I = P * r * t
        if P == 0:
            P = is_int((I / r) / t)

        return I, P, r


def ask_function_data(func_name: str, prompt: str) -> list[str]:
    cprint(func_name, "MAGENTA", end=" ")

    data = get_data_list(prompt)

    return data


def is_money(data: list[str]) -> tuple[float, float, Literal["", "$"]]:
    money = ""

    for i in data:
        if "$" in i:
            money = "$"

    val1, val2 = tuple(clean_array_data_strict(data))

    return val1, val2, money


def main() -> None:
    fn = ["rise", "percent", "add", "tax", "discount", "markup", "interest"]

    print("\nApplied percentage functions available:")
    list_options(fn)

    while True:
        function_name = input("Function: ")
        
        if function_name:
            format_data(function_name)
        else:
            cprint("Back...", "Yellow")
            break


if __name__ == "__main__":
    # from tester import test_all

    cprint("TEST_MODE: UNAVAILABLE", "RED")
    exit(0)

    # to_test = [
    #     ["$1.95", "is", "7.5%"],
    #     ["35%", "of", "90"],
    #     ["125%", "of", "28"],
    #     ["36", "is", "75%"],
    #     ["$1.17", "is", "6.5%"],
    #     ["percent", "of", "36", "is", "9"],
    #     ["percent", "of", "96", "is", "144"],
    #     ["$16", "is", "20%"],
    #     ["$108.10", "is", "11.5%"],
    #     ["rise", "190", "to", "114"],
    #     ["rise", "15.50", "to", "17.55"],
    #     ["tax", "6.25%", "of", "$724"],
    #     ["tax", "8.2%", "of", "$250"],
    #     ["discount", "35%", "of", "$140"],
    #     ["discount", "$13.95", "of", "$31"],
    #     ["discount", "$13.95", "to", "$31"]
    # ]
    # to_expect = [
    #     "7.5% of $26 is $1.95",
    #     "35% of 90 is 31.5",
    #     "125% of 28 is 35",
    #     "75% of 48 is 36",
    #     "6.5% of $18 is $1.17",
    #     "25% of 36 is 9",
    #     "150% of 96 is 144",
    #     "20% of $80 is $16",
    #     "11.5% of $940 is $108.1",
    #     "114 is a decrease of 40% to 190",
    #     "17.55 is an increase of 13.2% to 15.5",
    #     "Tax rate:   6.25%\nSales tax:  $45.25\nTotal cost: $769.25",
    #     "Tax rate:   8.2%\nSales tax:  $20.50\nTotal cost: $270.50",
    #     "Discounted: $49\nTotal to pay: $91 (35% off)",
    #     "Discounted: $17.05\nTotal to pay: $13.95 (55% off)",
    #     "Discounted: $13.95\nTotal to pay: $17.05 (45% off)"
    # ]

    # test_all(format_data, to_test, to_expect)
