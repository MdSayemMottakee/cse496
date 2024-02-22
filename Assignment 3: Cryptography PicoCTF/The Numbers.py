import string

alphabet = string.ascii_uppercase[:]

inp = input()


tokens = inp.split()

result = ""

for token in tokens:

    if token.isdigit():
        result += alphabet[int(token) - 1]

print(result)
