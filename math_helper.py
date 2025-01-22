import average_finder
import prime_factorization
import ratios_rate
import square_root
import physics
import circ_area
import percent_converter
import applied_percentage
from common_tools import cprint, list_options


functions = [
    "Average",
    "Prime Factorization",
    "Ratio and Rate",
    "Square Root",
    "Basic Physics",
    "Circumference and Area",
    "Percent",
    "Applied Percentage",
]

print("Options available:")
while True:
    list_options(functions)
    option = input("What do you want to do? ").strip()
    if option:
        try:
            option = int(option)
        except ValueError:
            cprint("Invalid input. Select using numbers.", color="RED")
            continue
    match option:
        case 1:
            average_finder.main()
        case 2:
            prime_factorization.main()
        case 3:
            ratios_rate.main()
        case 4:
            square_root.main()
        case 5:
            physics.main()
        case 6:
            circ_area.main()
        case 7:
            percent_converter.main()
        case 8:
            applied_percentage.main()
        case _:
            cprint("Exit...", "GREEN")
            break
