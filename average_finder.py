from common_tools import get_data_list, clean_array_data, check_if_int, colorize


def mean(array: list):
    return check_if_int(round(sum(array) / len(array), 2))


# Array should always be sorted, else result could be wrong.
def median(array: list):
    median_array = len(array) // 2
    if len(array) % 2 == 0:
        med = (array[median_array] + array[median_array - 1]) / 2
    else:
        med = array[median_array]

    return check_if_int(med)


def mode(array: list):
    freq = {}
    mod = []

    for i in array:
        freq[i] = freq.get(i, 0) + 1

    max_freq = max(freq.values())
    for key in freq:
        if freq[key] == max_freq:
            mod.append(str(check_if_int(key)))

    if len(freq) == len(mod):
        return None
    else:
        return " ".join(mod)


def print_result(values: list):
    if len(values) == 0:
        print("List is empty!")
    else:
        values.sort()
        print(colorize("Mean:", "BLUE"), mean(values))
        print(colorize("Median:", "GREEN"), median(values))
        print(colorize("Mode:", "RED"), mode(values))


def main():
    while True:
        values = get_data_list("Find average of: ")
        if values:
            print_result(clean_array_data(values))
            continue
        else:
            print("Back...")
            break


if __name__ == "__main__":
    main()
