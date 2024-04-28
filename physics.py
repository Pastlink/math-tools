from common_tools import cprint, clean_string, is_int
from square_root import square_root


def landscaping(n: int) -> int | float:
    return is_int(round(square_root(n), 1))


def basic_grav(n: int) -> int | float:
    return is_int(round(square_root(n / 4), 1))


def car_speed(n: int) -> int | float:
    return is_int(round(square_root(24 * n), 1))


def print_result(data):
    if len(data) == 0:
        cprint("No valid parameters!", "RED")
    else:
        data = int(data)
        cprint("Landscaping:", "BLUE", f"{landscaping(data)} feet!")
        cprint("Gravity:", "GREEN", f"{basic_grav(data)} seconds!")
        cprint("Speed:", "RED", f"{car_speed(data)} mph!")


def main():
    while True:
        data = input("Data: ")
        if data:
            try:
                print_result(clean_string(data))
            except ValueError:
                cprint("Invalid input.", "RED")
                continue
        else:
            cprint("Back...", "YELLOW")
            break
