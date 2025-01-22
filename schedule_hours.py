from pomodoro_app.clock_func import format_time, time_adder
from common_tools import to_num

print("To calculate how long a task take, please input first the start time of said task and press enter. After that input the end time. The difference will be then printed.")

start = input("Start time: ")
end = input("End time: ")

hours_start, minutes_start = to_num(*start.split(":"))
hours_end, minutes_end = to_num(*end.split(":"))

total_minutes = minutes_start - minutes_end
hours_difference = hours_end - hours_start


hours_difference, total_minutes = time_adder(hours_difference, total_minutes)
print(f"Time difference: {format_time(hours_difference, total_minutes)} hours")
