# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

data = open("input.txt").read().split("\n\n")
part1 = max(map(lambda x: sum(map(int, x.split("\n"))), data))
print(part1)

part2 = sum(sorted(map(lambda x: sum(map(int, x.split("\n"))), data), reverse=True)[:3])
print(part2)