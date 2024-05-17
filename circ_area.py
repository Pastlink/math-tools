from common_tools import cprint, is_int, to_num


def circumference(data):
    return is_int(round(6.28 * data, 2))


def area(data):
    return is_int(round(3.14 * (data * data), 3))


def handle_fractions(data):
    if "/" in data:
        num, den = to_num(*data.split("/"))
        data = round(num / den, 5)
    
    return is_int(float(data))


def print_result(data):
    data = handle_fractions(data)

    if not isinstance(data, int | float):
        cprint("No valid parameters!", "RED")
    else:
        cprint("Circumference:", "BLUE", circumference(data))
        cprint("Area:", "GREEN", area(data))


def main():
    while True:
        data = input("Find circumference and area of: ")
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
    cprint("DEBUG: NOFUNC", "RED")
