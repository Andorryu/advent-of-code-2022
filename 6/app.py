
def is_string_repeat(string):
    setofs = set(string)
    return len(setofs) != len(string)

def driver(num):
    file = open("input.txt")
    filestring = file.read()
    print(filestring)

    for i in range(len(filestring)):
        if not is_string_repeat(filestring[i:i+num]):
            ans = i+num
            break
    print(ans)

driver(14) # pass in 4 for part 1 and 14 for part 2
