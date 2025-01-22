from typing import Any
import random

### TEXT PARSERS
# Format input data and return as list of relevant elements.

def get_data_list(prompt: str) -> list[str]:
    return list(filter(None, input(prompt).split(" ")))


# Change float to int if whole number.
def is_int(num: float, round_value=15) -> float | int:
    if num.is_integer():
        return int(num)
    else:
        num = round(num, round_value) # Rounded value might be int, so check again
        return int(num) if num.is_integer() else num


# Take strings and cast into float or int, return as tuple.
def to_num(*strings: str) -> tuple[int | float, ...]:
    new_nums = []
    for string in strings:
        try:
            new_nums.append(is_int(float(string)))
        except ValueError:
            continue

    return tuple(new_nums)


### DATA CLEANERS
# Iterate over array, return array of int or number strings.
def clean_array_data(array: list[str]) -> list[float | str]:
    clean_array = []
    for i in range(len(array)):
        try:  # Try to cast sub array into float or int.
            clean_array.append(is_int(float(array[i])))
        except ValueError:  # Clean sub array to extract possible numbers.
            new_value = clean_string(array[i])
            try:  # Try to append cleaned new float value.
                clean_array.append(is_int(float(new_value)))
            except ValueError:
                pass

    return clean_array


# Iterate over string's chars and return as strings with valid symbols.
def clean_string(sub_array: str) -> str:
    valid_symbols = ["-", ".", ":", "/", "%", "(", ")", "$"]
    clean_values = ""

    for i in range(len(sub_array)):
        try:  # If sub array's value can be cast into int, then it is a valid number.
            clean_values += str(int(sub_array[i]))
        except ValueError:  # Else try to extract the number checking for valid symbols.
            if sub_array[i] in valid_symbols and sub_array[i] not in clean_values:
                clean_values += sub_array[i]
            continue

    return clean_values

# Iterate over array, return array of floats or ints only.
def clean_array_data_strict(array: list[str]) -> list[float | int]:
    clean_array = []
    for i in range(len(array)):
        try:  # Try to cast sub array into float or int.
            clean_array.append(is_int(float(array[i])))
        except ValueError:  # Clean sub array to extract possible numbers.
            new_value = clean_string_strict(array[i])
            try:  # Try to append cleaned new float value.
                clean_array.append(is_int(float(new_value)))
            except ValueError:
                pass

    return clean_array

# Return strings of valid int or float only.
def clean_string_strict(sub_array: str) -> str:
    clean_values = ""

    for i in range(len(sub_array)):
        try:  # If sub array's value can be cast into int, then it is a valid number.
            clean_values += str(int(sub_array[i]))
        except ValueError:  # Else try to extract the number checking for float points.
            if sub_array[i] == "." and sub_array[i] not in clean_values:
                clean_values += sub_array[i]
            continue

    return clean_values


### BASH COLORS
class colors:
    BLACK        = "\033[30m"
    RED          = "\033[31m"
    GREEN        = "\033[32m"
    YELLOW       = "\033[33m"
    BLUE         = "\033[34m"
    MAGENTA      = "\033[35m"
    CYAN         = "\033[36m"
    LIGHTGRAY    = "\033[37m"
    GRAY         = "\033[90m"
    LIGHTRED     = "\033[91m"
    LIGHTGREEN   = "\033[92m"
    LIGHTYELLOW  = "\033[93m"
    LIGHTBLUE    = "\033[94m"
    LIGHTMAGENTA = "\033[95m"
    LIGHTCYAN    = "\033[96m"
    WHITE        = "\033[97m"
    ENDCOLOR     = "\033[0m"


# Add color to text in the terminal!
def colorize(data: Any, color: str) -> str:
    try:
        return f"{getattr(colors, color.upper())}{data}{colors.ENDCOLOR}"
    except AttributeError:
        print(f"Unknown color: '{color}'")
        return f"{colors.RED}ERROR{colors.ENDCOLOR}"


# Shorter syntax, color print for one liners.
def cprint(flavor_text: str, color: str = "BLUE", data: Any = "", end: str | None = "\n") -> None:
    if data:
        print(colorize(flavor_text, color), data, end=end)
    else:
        print(colorize(flavor_text, color), end=end)


### COMPARERS
# Compare inputs, return higher value
def cmp(a: float, b: float) -> float | None:
    if a > b:
        cprint(f"{a} is higher.", "GREEN")
        return a
    elif a < b:
        cprint(f"{b} is higher.", "GREEN")
        return b
    else:
        cprint(f"{a} and {b} are equal.", "RED")
        return a # Return {a} as both are the same.

### LISTERS
def list_options(func_list: list[str], enum = True) -> None:
    lst = []
    for i in range(0, len(func_list)):
        if i % 2 == 0 and i != 0:
            lst.append("\n")
        lst.append(f"{colorize(i + 1, "GREEN")}: {func_list[i]} ")

    print("".join(lst))
