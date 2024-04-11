import average_finder
import prime_factorization
import ratios_rate
import square_root
import physics
from common_tools import colorize


def print_options(func_list: list):
    lst = []
    for i in range(0, len(func_list)):
        if i % 2 == 0 and i != 0:
            lst.append("\n")
        lst.append(f'{colorize(i + 1, "GREEN")}: {func_list[i]} ')

    print("".join(lst))


functions = ["Average", "Prime Factorization", "Ratio and Rate", "Square Root", "Basic Physics"]

print("Options available:")
while True:
    print_options(functions)
    option = input("What do you want to do? ").strip()
    if option:
        try:
            option = int(option) - 1
        except ValueError:
            print(colorize("Invalid input. Select using numbers.", "RED"))
            continue
    match option:
        case 0:
            average_finder.main()
        case 1:
            prime_factorization.main()
        case 2:
            ratios_rate.main()
        case 3:
            square_root.main()
        case 4:
            physics.main()
        case _:
            print("Exit...")
            break
