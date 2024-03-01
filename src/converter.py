VAL = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
SYB = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


def decimal_to_roman(num: int) -> str:
    if num <= 0:
        raise ValueError("Input must be a positive integer")

    roman_num = ""
    i = 0

    while num > 0:
        for _ in range(num // VAL[i]):
            roman_num += SYB[i]
            num -= VAL[i]
        i += 1

    return roman_num
