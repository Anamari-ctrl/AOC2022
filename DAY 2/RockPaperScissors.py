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

