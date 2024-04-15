stack1 = [["N", "Z"][::-1], ["D", "C", "M"][::-1], ["P"]]

stack = [["P", "V", "Z", "W", "D", "T"][::-1],
         ["D", "J", "F", "V", "W", "S", "L"][::-1],
         ["H", "B", "T", "V", "S", "L", "M", "Z"][::-1],
         ["J", "S", "R"][::-1],
         ["W", "L", "M", "F", "G", "B", "Z", "C"][::-1],
         ["B", "G", "R", "Z", "H", "V", "W", "Q"][::-1],
         ["N", "D", "B", "C", "P", "J", "V"][::-1],
         ["Q", "B", "T", "P"][::-1],
         ["C", "R", "Z", "G", "H"][::-1]
         ]

data = open("input1.txt").readlines()
# n = list(map(lambda x: list(filter(lambda y: y.isdigit(), x.strip())), data))
# n = list(map(lambda x: list(filter(lambda y: y.isdigit(), x.split(" "))), data))
n = list(map(lambda x: list(map(lambda y: list(filter(lambda z: z.isdigit(), y.split(" "))), x.split("\n"))), data))

for instruction in n:
    n_crates = int(instruction[0][0])
    old_stack = int(instruction[0][1])
    new_stack = int(instruction[0][2])
    for i in range(n_crates):
        if stack1[old_stack-1]:
            removed = stack1[old_stack - 1].pop()
            stack1[new_stack - 1].append(removed)

message = ""
for i in stack1:
    if i:
        message += i.pop()

print(message)


