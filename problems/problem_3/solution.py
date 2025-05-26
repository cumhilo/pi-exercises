from problems.utils import in_between


def to_roman_numeral(number: int) -> str:
    if not in_between(number, 1, 3999):
        raise ValueError("out of range")

    conversor = {
        1000: "M",
        900: "CM", 500: "D", 400: "CD", 100: "C",
        90: "XC", 50: "L", 40: "XL", 10: "X",
        9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    roman = ""

    for k, v in conversor.items():
        appearances = number // k
        if appearances == 0: continue

        roman += v * appearances
        number -= (k * appearances)

    return roman
