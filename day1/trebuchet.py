
f = open("input.txt", "r")

list=[]
check=0
for line in f:
    for c in line:
        if (c.isdigit() and check == 0):
            first = c
            check=1
        for k in line[::-1]:
            if k.isdigit():
                last=k
                break
    check = 0
    number = first + last
    list.append(int(number))

print(sum(list))

          


    