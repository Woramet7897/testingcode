from itertools import combinations


def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for char1, char2 in combinations(unique_chars, 2):
        filtered_string = [c for c in s if c == char1 or c == char2]

        if all(
            filtered_string[k] != filtered_string[k + 1]
            for k in range(len(filtered_string) - 1)
        ):
            max_length = max(max_length, len(filtered_string))

    return max_length
