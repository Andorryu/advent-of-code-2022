from __future__ import annotations
import os
import time

class Tail:
    def __init__(self, pos: list[int], head: Head) -> None:
        self.pos = pos
        self.head = head
        self.poses = {tuple(pos)} # len(self.poses) is answer to part 1
    
    def settle(self) -> None:
        if self.head.pos[0] - self.pos[0] == 2: # head is below
            self.pos[0] += 1 # move down
        elif self.pos[0] - self.head.pos[0] == 2: # head is above
            self.pos[0] -= 1 # move up
        elif self.head.pos[1] - self.pos[1] == 2: # head is to the right
            self.pos[1] += 1 # move right
        elif self.pos[1] - self.head.pos[1] == 2: # head is left
            self.pos[1] -= 1 # move left
        self.poses.add(tuple(self.pos))

class Head:
    def __init__(self, pos: list[int], tail: Tail) -> None: # pos is (row, col)
        self.pos = pos
        self.tail = tail
    
    def move(self, dir: str, amount: int):
        # base case
        if amount == 0:
            return
        #print_frame(self, self.tail)
        # move once
        if dir == "R":
            self.pos[1] += 1
        elif dir == "L":
            self.pos[1] -= 1
        elif dir == "U":
            self.pos[0] -= 1
        elif dir == "D":
            self.pos[0] += 1
        # settle the tail and recurse
        self.tail.settle()
        self.move(dir, amount - 1)

def print_state(head, tail, start, num_rows, num_cols):
    print(f"H at {head.pos}")
    print(f"T at {tail.pos}")
    for row in range(num_rows):
        for col in range(num_cols):
            if head.pos[0] == row and head.pos[1] == col:
                print("H", end="")
            elif tail.pos[0] == row and tail.pos[1] == col:
                print("T", end="")
            elif start[0] == row and start[1] == col:
                print("s", end="")
            else:
                for pos in tail.poses:
                    if pos[0] == row and pos[1] == col:
                        print("#", end="")
                        break
                else:
                    print(".", end="")
        print("")

def print_frame(head, tail):
    print("")
    print_state(head, tail, (4, 0), 5, 6)
    time.sleep(2)

def driver():
    filelines = open("input.txt").readlines()

    # remove new-lines
    i = 0
    for line in filelines:
        filelines[i] = line.removesuffix('\n')
        i += 1
    
    start = [4, 0]

    # create objects
    tail = Tail(start, head := Head(start, None))
    head.tail = tail

    for com in filelines:
        head.move(com[0], int(com[2]))
        # print_frame(head, tail)
        # print(f"H: {head.pos}")
        # print(f"T: {tail.pos}")
    
    print(tail.poses)
    print(len(tail.poses))

driver()
