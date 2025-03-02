def funny_string(s):
    ascii_values = [ord(c) for c in s]
    reversed_ascii_values = ascii_values[::-1]

    for i in range(len(s) - 1):
        if abs(ascii_values[i] - ascii_values[i + 1]) != abs(
            reversed_ascii_values[i] - reversed_ascii_values[i + 1]
        ):
            return "Not Funny"

    return "Funny"


def check_all(strings):
    return [funny_string(s) for s in strings]
