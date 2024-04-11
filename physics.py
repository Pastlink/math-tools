from common_tools import cprint, colorize as clr, clean_string, check_if_int
from square_root import square_root


def basic_grav(n: int) -> int | float:
    return check_if_int(round(square_root(n / 4), 1))

def car_speed(n: int) -> int | float:
    return check_if_int(round(square_root(24 * n), 1))

def print_result(data):
    if len(data) == 0:
        cprint("No valid parameters!", "RED")
    else:
        data = int(data)
        print(f'{clr("Gravity:", "BLUE")} {basic_grav(data)} seconds!')
        print(f'{clr("Speed:", "GREEN")} {car_speed(data)} mph!')


def main():
    while True:
        data = input("Find falling time from: ")
        if data:
            try:
                print_result(clean_string(data))
            except ValueError:
                cprint("Invalid input.", "RED")
                continue
        else:
            print("Back...")
            break