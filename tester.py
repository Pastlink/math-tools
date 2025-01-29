from typing import Any, Callable
from common_tools import colorize, cprint


def test(function_data: Any, expected_data: str, test_name: str, test_num=0):
    GOOD = "GREEN"
    BAD = "RED"

    print(f"TEST {test_num+1}: {colorize(test_name, 'BLUE')} ", end="")

    if function_data == expected_data:
        print(f"{colorize('PASSED!', GOOD)}")
        success = 1
        DATA = GOOD
    else:
        print(f"{colorize('FAILED!', BAD)}")
        success = 0
        DATA = BAD

    cprint("RECEIVED:", DATA, function_data)
    cprint("EXPECTED:", "YELLOW", expected_data)

    return success


def test_all(func: Callable[..., Any], param: list[Any], expected: list[Any]):
    FUNC_TESTED = func.__name__
    TEST_LENGTH = len(param)
    test_passed = 0

    print(f'DEBUG: {colorize(FUNC_TESTED, "BLUE")} TESTMODE\n')

    for i in range(TEST_LENGTH):
        if isinstance(param[i], tuple):
            test_passed += test(func(*param[i]), expected[i], f"{FUNC_TESTED}{param[i]}", i)
        else:
            test_passed += test(func(param[i]), expected[i], f"{FUNC_TESTED}({param[i]})", i)

    test_failed = TEST_LENGTH - test_passed
    total_tests = colorize(f"TOTAL TESTS: {TEST_LENGTH}", "BLUE")
    test_passed = colorize(f"TEST PASSED: {test_passed}", "GREEN")
    test_failed = colorize(f"TEST FAILED: {test_failed}", "RED")

    print(f"\n{total_tests} | {test_passed} | {test_failed}")
