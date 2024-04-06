# Python program to print prime factors
from math import sqrt
from common_tools import colorize
from tester import test_all


# A function to print all prime factors of
# a given number n
def prime_factorization(n: int):
    prime_factors = []
    exponents = []

    # Handle 1 and 0, plus negative numbers
    if n == 1 or n == 0:
        return "None", "None"
    elif n <= -1:
        n *= -1
        exponents.append("-1¹")
    # Print the number of two's that divide n
    expo = 0
    while n % 2 == 0:
        expo += 1
        prime_factors.append("2")
        n = n // 2

    if n % 2 and expo != 0:
        exponents.append(f"{2}{get_super(str(expo))}")

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            expo = 0
            # while i divides n , print i and divide n
            while n % i == 0:
                expo += 1
                prime_factors.append(str(i))
                n //= i
            exponents.append(f"{i}{get_super(str(expo))}")

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        prime_factors.append(str(n))
        exponents.append(f'{n}{get_super("1")}')

    return f'{", ".join(prime_factors)}', f'{" × ".join(exponents)}'


def prime_numbers(n: int):
    MAX = 10000

    if n > MAX:
        ans = input(
            colorize(
                f"""Your input goes over {MAX}!
Calculating its primes might take a long time.
Type 'YES, PRINT THEM' if you want to print them anyway. """,
                "YELLOW",
            )
        )
        if ans != "YES, PRINT THEM":
            return "Skipped."

    primes = []

    if n < 2:
        return "None"

    for i in range(2, n + 1):
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break
        else:
            primes.append(str(i))

    return ", ".join(primes)


def get_super(x):
    normal = "123456789"
    super_s = "¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans("".join(normal), "".join(super_s))
    return x.translate(res)


def print_result(n: int):
    factors, exponents = prime_factorization(n)
    print(colorize("Factors:", "BLUE"), factors)
    print(colorize("Exponents:", "GREEN"), exponents)
    # print(colorize("Primes:", "RED"), prime_numbers(n))


# Driver Program to test above function
def main():
    while True:
        n = input("Find factors of: ").strip()
        if n:
            try:
                print_result(int(n))
            except ValueError:
                print("Invalid input.")
                continue
        else:
            print("Back...")
            break


if __name__ == "__main__":
    to_test = [
        276,
        7000,
        1151,
        1705542,
        1411137,
        1715,
        1575,
        284,
        393,
        7084,
        5595,
        23356,
        50034,
        3487,
        18720,
    ]
    to_expect = [
        ("2, 2, 3, 23", "2² × 3¹ × 23¹"),
        ("2, 2, 2, 5, 5, 5, 7", "2³ × 5³ × 7¹"),
        ("1151", "1151¹"),
        ("2, 3, 17, 23, 727", "2¹ × 3¹ × 17¹ × 23¹ × 727¹"),
        ("3, 3, 7, 13, 1723", "3² × 7¹ × 13¹ × 1723¹"),
        ("5, 7, 7, 7", "5¹ × 7³"),
        ("3, 3, 5, 5, 7", "3² × 5² × 7¹"),
        ("2, 2, 71", "2² × 71¹"),
        ("3, 131", "3¹ × 131¹"),
        ("2, 2, 7, 11, 23", "2² × 7¹ × 11¹ × 23¹"),
        ("3, 5, 373", "3¹ × 5¹ × 373¹"),
        ("2, 2, 5839", "2² × 5839¹"),
        ("2, 3, 31, 269", "2¹ × 3¹ × 31¹ × 269¹"),
        ("11, 317", "11¹ × 317¹"),
        ("2, 2, 2, 2, 2, 3, 3, 5, 13", "2⁵ × 3² × 5¹ × 13¹"),
    ]

    test_all(prime_factorization, to_test, to_expect)

    # main()

# This code is contributed by Harshit Agrawal
# Code Improved by Sarthak Shrivastava
# Code modified for personal use by PastLink
