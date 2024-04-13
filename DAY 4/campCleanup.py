data = open("input.txt").read().split("\n")

# '2-4,6-8'
# ['2-4', '6-8']
# [['2', '4'] , ['6', '8']]
# [[2, 4] , [6, 8]]
# 1
# 0
# max prvih minimum drugih


l = list(map(lambda x: list(map(lambda y: list(map(int, y.split("-"))), x.split(","))), data))


def fully_contains(a, b):
    range = [max(a[0], b[0]), min(a[1], b[1])]
    return range == a or range == b


fc = sum(map(lambda x: 1 if fully_contains(x[0], x[1]) else 0, l))
print(fc)


def overlap(a, b):
    return not (a[0] > b[1] or b[0] > a[1])


fc = sum(map(lambda x: 1 if overlap(x[0], x[1]) else 0, l))
print(fc)
