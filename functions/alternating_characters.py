def check_all(lst):
    def alternating_characters(s):
        deletions = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                deletions += 1
        return deletions

    return [alternating_characters(s) for s in lst]
