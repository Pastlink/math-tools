from common_tools import cprint, is_int

def percent_uncertainty(measure: int | float, uncertainty: int | float):
    return is_int(round((uncertainty/measure) * 100, 2))

measure = float(input("Measure: "))
uncertainty = float(input("Uncertainty: "))

cprint(f'{percent_uncertainty(measure, uncertainty)}%', "GREEN")
    
