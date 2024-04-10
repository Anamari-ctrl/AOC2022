pairs = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

data = open("input.txt").read().split("\n")
part1 = sum([pairs.get(x) for x in data if x in pairs.keys()])
print(part1)

pairs2 = {
    "A A": 4,
    "A B": 8,
    "A C": 3,
    "B A": 1,
    "B B": 5,
    "B C": 9,
    "C A": 7,
    "C B": 2,
    "C C": 6
}

pairs21 = {
    "A X": "C",
    "A Y": "A",
    "A Z": "B",
    "B X": "A",
    "B Y": "B",
    "B Z": "C",
    "C X": "B",
    "C Y": "C",
    "C Z": "A"
}

data = open("input.txt").read().split("\n")

result = [f"{x[0]} {pairs21.get(x)}" for x in data if x in pairs21.keys()]
l = sum([pairs2.get(x) for x in result])
print(l)
