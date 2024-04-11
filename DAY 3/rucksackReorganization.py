data = open("input.txt").read()

a = [list(set(list(x[:len(x) // 2])).intersection(set(list(x[len(x) // 2:]))))[0] for x in data.split("\n")]
print(a)


def n(x: str):
    return ord(x.upper()) - ord('A') + (27 if x.isupper() else 1)


print(sum(map(n, a)))
