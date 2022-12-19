


file = open("input.txt", "r")

numlist = []
filelist = file.readlines()

file.close()

# fill 2d list with sets of numbers
temp = []
for line in filelist:
    if line != '\n':
        temp.append(int(line))
    else:
        numlist.append(temp)
        temp = []
numlist.append(temp)

# collapse numlist
sumlist = []
for numset in numlist:
    total = 0
    for num in numset:
        total += num
    sumlist.append(total)

# find greatest number
greatest = 0
for num in sumlist:
    if num > greatest:
        greatest = num

print("\ngreatest is...")
print(greatest)


# part 2
print("\ngreatest 3 are...")
total = 0
sortedlist = sorted(sumlist, reverse=True)
for i in range(3):
    total += sortedlist[i]
    print(sortedlist[i])

print("\ntotalled...")
print(total)

