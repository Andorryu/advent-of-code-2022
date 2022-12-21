
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

def move2(src, dest, num):
    stack = LifoQueue() # intermediary stack
    move(src, stack, num)
    move(stack, dest, num)

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
for _ in range(9):
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
            if spaces == 4:
                i += 1
                spaces = 0
        elif c == '[':
            spaces = 0

def process(mov):
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
                        elif j == 1:
                            src = int(line[i])
                            j += 1
                        else:
                            dest = int(line[i])
            mov(stacks[src-1], stacks[dest-1], num)
            print("moved " + str(num) + " from " + str(src) + " to " + str(dest))

process(move2) # call this with either move or move2 to do part 1 or part 2

for stack in stacks:
    print(stack.get(), end="")
print("")
