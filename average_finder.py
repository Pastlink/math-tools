from common_tools import cprint, get_data_list, clean_array_data, is_int


def mean(array: list) -> float | int:
    return is_int(round(sum(array) / len(array), 2))


# Array should always be sorted, else result could be wrong.
def median(array: list) -> float | int:
    median_array = len(array) // 2
    if len(array) % 2 == 0:
        med = (array[median_array] + array[median_array - 1]) / 2
    else:
        med = array[median_array]

    return is_int(med)


def mode(array: list) -> str:
    freq = {}
    mod = []

    for i in array:
        freq[i] = freq.get(i, 0) + 1

    max_freq = max(freq.values())
    for key in freq:
        if freq[key] == max_freq:
            mod.append(str(is_int(key)))

    if len(freq) == len(mod):
        return "None"
    else:
        return " ".join(mod)


def print_result(values: list) -> None:
    if len(values) == 0:
        cprint("List is empty!", "RED")
    else:
        values.sort()
        cprint("Mean:  ", "BLUE", mean(values))
        cprint("Median:", "GREEN", median(values))
        cprint("Mode:  ", "RED", mode(values))


def main() -> None:
    while True:
        values = get_data_list("Find average of: ")
        if values:
            print_result(clean_array_data(values))
            continue
        else:
            cprint("Back...", "YELLOW")
            break


if __name__ == "__main__":
    main()
