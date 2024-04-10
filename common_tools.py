# Format input data and return list
def get_data_list(prompt: str):
    return list(filter(None, input(f"{prompt}").split(" ")))


# Change float to int if it is a whole number.
def check_if_int(num: float):
    if num.is_integer():
        return int(num)
    else:
        return num


### DATA CLEANERS
# Iterate over array, return array of floats only.
def clean_array_data(array, index=0) -> list[float]:
    if index >= len(array):
        return array

    try:
        array[index] = float(array[index])
    except ValueError:
        array[index] = clean_string(array[index])
        if array[index] is None:
            array.pop(index)
            index -= 1

    clean_array_data(array, index + 1)

    return array


# Iterate over sub-array of array, return floats only.
def clean_string(sub_array: str):
    valid_symbols = [".", ":", "/"] # Keep negative, float, time and ratios. 
    clean_values = ""

    for i in range(0, len(sub_array)):
        try:
            clean_values += str(int(sub_array[i]))
        except ValueError:
            if sub_array[i] in valid_symbols and clean_values != "" or sub_array[i] == "-":
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


def colorize(data, color: str):
    try:
        return f"{getattr(colors, color.upper())}{data}{colors.ENDCOLOR}"
    except AttributeError:
        print(f"Unknown color: '{color}'")
        return f"{colors.RED}ERROR{colors.ENDCOLOR}"
