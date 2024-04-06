from common_tools import colorize


def test(function_data, expected_data, test_name: str, test_num=0):
    GOOD = "GREEN"
    BAD = "RED"

    print(f'TEST {test_num+1}: {colorize(test_name, "BLUE")} ', end="")

    if function_data == expected_data:
        print(f"{colorize("PASSED!", GOOD)}")
        success = 1
        DATA = GOOD
    else:
        print(f"{colorize("FAILED!", BAD)}")
        success = 0
        DATA = BAD

    print(colorize("RECEIVED:", DATA), function_data)
    print(colorize("EXPECTED:", "YELLOW"), expected_data)

    return success


def test_all(func, param: list, expected: list):
    FUNC_TESTED = func.__name__
    TEST_LENGTH = len(param)
    passed = 0

    print(f'DEBUG: {colorize(FUNC_TESTED, "BLUE")} TESTMODE\n')

    for i in range(0, TEST_LENGTH):
        if isinstance(param[i], tuple):
            passed += test(func(*param[i]), expected[i], f"{FUNC_TESTED}{param[i]}", i)
        else:
            passed += test(func(param[i]), expected[i], f"{FUNC_TESTED}({param[i]})", i)

    failed = TEST_LENGTH - passed
    total_tests = colorize(f"TOTAL TESTS: {TEST_LENGTH}", "BLUE")
    test_passed = colorize(f"TEST PASSED: {passed}", "GREEN")
    test_failed = colorize(f"TEST FAILED: {failed}", "RED")

    print(f"\n{total_tests} | {test_passed} | {test_failed}")
