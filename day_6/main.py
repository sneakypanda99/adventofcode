

input = ""
with open("input", "r") as f:
    input = f.read()


def findMark(length):
    parsed = []
    for x in input:
        parsed.append(x)
        if (len(parsed) >= length and len(set(parsed[-length:])) == len(parsed[-length:])):
            return len(parsed)
            break


print(findMark(4))
print(findMark(14))
