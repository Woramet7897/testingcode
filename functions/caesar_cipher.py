def caesarCipher(s, k):
    result = []
    for i in s:
        if i.isalpha():
            base = ord("a") if i.islower() else ord("A")
            result.append(chr((ord(i) - base + k) % 26 + base))
        else:
            result.append(i)
    return "".join(result)
