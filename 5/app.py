
filelist = open("input.txt", "r").readlines()

stacklist  = []

for line in filelist:
    if line[1].isdigit():
        break
    else:
        stacklist.append(line.removesuffix('\n'))

stacklist.reverse()
stacks = []

for line in stacklist:
    for c in line:
        if c.isalpha():
            
