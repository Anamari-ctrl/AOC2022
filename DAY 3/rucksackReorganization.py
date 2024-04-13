data = open("input1.txt").read()

a = [list(set(list(x[:len(x) // 2])).intersection(set(list(x[len(x) // 2:]))))[0] for x in data.split("\n")]


def n(x: str):
    return ord(x.upper()) - ord('A') + (27 if x.isupper() else 1)


print(sum(map(n, a)))

data = open("input.txt").read().split("\n")

stickers = []
start = 0
stop = 3
while stop <= len(data):
    curr = data[start:stop]
    result = ((set(curr[0]).intersection(set(curr[1]))).intersection(set(curr[2])))
    stickers.append(list(result)[0])
    start += 3
    stop += 3
    curr.clear()

print(sum(map(n, stickers)))
