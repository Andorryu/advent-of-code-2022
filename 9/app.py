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
            if self.head.pos[1] - self.pos[1] == 1: # head is also right
                self.pos[1] += 1
            elif self.pos[1] - self.head.pos[1] == 1: # head is also left
                self.pos[1] -= 1
        elif self.pos[0] - self.head.pos[0] == 2: # head is above
            self.pos[0] -= 1 # move up
            if self.head.pos[1] - self.pos[1] == 1: # head is also right
                self.pos[1] += 1
            elif self.pos[1] - self.head.pos[1] == 1: # head is also left
                self.pos[1] -= 1
        elif self.head.pos[1] - self.pos[1] == 2: # head is to the right
            self.pos[1] += 1 # move right
            if self.head.pos[0] - self.pos[0] == 1: # head is also down
                self.pos[0] += 1
            elif self.pos[0] - self.head.pos[0] == 1: # head is also up
                self.pos[0] -= 1
        elif self.pos[1] - self.head.pos[1] == 2: # head is left
            self.pos[1] -= 1 # move left
            if self.head.pos[0] - self.pos[0] == 1: # head is also down
                self.pos[0] += 1
            elif self.pos[0] - self.head.pos[0] == 1: # head is also up
                self.pos[0] -= 1
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
        #print_frame(self, self.tail)
        # settle the tail and recurse
        self.tail.settle()
        self.move(dir, amount - 1)

def print_state(head, tail, start, num_rows, num_cols): # for debugging
    print(f"H at {head.pos}")
    print(f"T at {tail.pos}")
    print(f"Visited spots: {len(tail.poses)}")
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

def print_frame(head, tail): # for debugging
    print("")
    print_state(head, tail, (15, 5), 20, 20)
    time.sleep(.2)
def driver():
    filelines = open("input.txt").readlines()

    # remove new-lines
    i = 0
    for line in filelines:
        filelines[i] = line.removesuffix('\n')
        i += 1

    START = [15, 5]

    # create objects
    tail = Tail(START.copy(), head := Head(START.copy(), None))
    head.tail = tail

    for com in filelines:
        head.move(com[0], int(com[2] + com[3:]))

    print(len(tail.poses))

driver()
