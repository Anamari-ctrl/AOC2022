stack = [["N", "Z"][::-1], ["D", "C", "M"][::-1], ["P"]]

stack1 = [["P", "V", "Z", "W", "D", "T"][::-1],
          ["D", "J", "F", "V", "W", "S", "L"][::-1],
          ["H", "B", "T", "V", "S", "L", "M", "Z"][::-1],
          ["J", "S", "R"][::-1],
          ["W", "L", "M", "F", "G", "B", "Z", "C"][::-1],
          ["B", "G", "R", "Z", "H", "V", "W", "Q"][::-1],
          ["N", "D", "B", "C", "P", "J", "V"][::-1],
          ["Q", "B", "T", "P"][::-1],
          ["C", "R", "Z", "G", "H"][::-1]
          ]

data = open("input.txt").readlines()
# n = list(map(lambda x: list(filter(lambda y: y.isdigit(), x.strip())), data))
# n = list(map(lambda x: list(filter(lambda y: y.isdigit(), x.split(" "))), data))
n = list(map(lambda x: list(map(lambda y: list(filter(lambda z: z.isdigit(), y.split(" "))), x.split("\n"))), data))

for instruction in n:
    n_crates = int(instruction[0][0])
    old_stack = int(instruction[0][1])
    new_stack = int(instruction[0][2])
    for i in range(n_crates):
        if stack1[old_stack - 1]:
            removed = stack1[old_stack - 1].pop()
            stack1[new_stack - 1].append(removed)

message = ""
for i in stack1:
    if i:
        message += i.pop()

print("PART1:", message)
stack = [["N", "Z"][::-1], ["D", "C", "M"][::-1], ["P"]]
stack1 = [["P", "V", "Z", "W", "D", "T"][::-1],
          ["D", "J", "F", "V", "W", "S", "L"][::-1],
          ["H", "B", "T", "V", "S", "L", "M", "Z"][::-1],
          ["J", "S", "R"][::-1],
          ["W", "L", "M", "F", "G", "B", "Z", "C"][::-1],
          ["B", "G", "R", "Z", "H", "V", "W", "Q"][::-1],
          ["N", "D", "B", "C", "P", "J", "V"][::-1],
          ["Q", "B", "T", "P"][::-1],
          ["C", "R", "Z", "G", "H"][::-1]
          ]


def order_crates(n_c, o_s, n_s):
    r_n = []
    j = 0
    while j < n_c:
        if stack1[o_s - 1]:
            r = stack1[o_s - 1].pop()
            r_n.append(r)
        j += 1
    for item in r_n[::-1]:
        stack1[n_s - 1].append(item)
    return stack1


# PART 2
for instruction in n:
    n_crates = int(instruction[0][0])
    old_stack = int(instruction[0][1])
    new_stack = int(instruction[0][2])
    if n_crates > 1:
        stack1 = order_crates(n_crates, old_stack, new_stack)
    else:
        if stack1[old_stack - 1]:
            removed = stack1[old_stack - 1].pop()
            stack1[new_stack - 1].append(removed)


message = ""
for i in stack1:
    if i:
        message += i.pop()

print("PART2: ", message)
