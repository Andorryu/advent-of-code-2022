
from queue import LifoQueue

def lookatstack(stack):
    if stack.empty():
        return
    print(stack.get(), end='')
    lookatstack(stack)

def move(src, dest, num):
    if num == 0:
        return
    dest.put(src.get_nowait())
    move(src, dest, num - 1)

filelist = open("input.txt", "r").readlines()

stacklist  = []

for line in filelist:
    if line[1].isdigit():
        break
    else:
        stacklist.append(line.removesuffix('\n'))

stacklist.reverse()
stacks = []

# init list with stacks
for _ in range(10):
    stacks.append(LifoQueue())

for line in stacklist:
    i = 0
    spaces = 0
    for c in line:
        if c.isalpha():
            stacks[i].put(c)
            i += 1
        elif c == ' ':
            spaces += 1
            if spaces == 5:
                i += 1
                spaces = 0


for line in filelist:
    if line[0] == 'm':
        j = 0
        skip = False
        for i in range(len(line)):
            if skip:
                skip = False
            else:
                if line[i].isdigit():
                    if j == 0:
                        if line[i+1].isdigit():
                            num = int(line[i]+line[i+1])
                            skip = True
                        else:
                            num = int(line[i])
                        j += 1
                        print("num = " + str(num))
                    elif j == 1:
                        src = int(line[i])
                        j += 1
                        print("src = " + str(src))
                    else:
                        dest = int(line[i])
                        print("dest = " + str(dest))
        move(stacks[src-1], stacks[dest-1], num)
for stack in stacks:
    lookatstack(stack)
    print("")
