
def split(lis):
    num = ''
    num1,num2 = 0, 0
    set1, set2 = 0, 0
    final = []
    
    for line in lis:
        for char in line:
            if char.isdigit():
                num += char
            elif char == '-':
                num1 = int(num)
                num = ''
            elif char == ',':
                num2 = int(num)
                num = ''
                set1 = set(range(num1, num2 + 1))
            elif char == '\n':
                num2 = int(num)
                num = ''
                set2 = set(range(num1, num2 + 1))
        final.append((set1, set2))
    return final
                

def calculate1(filelist):
    total = 0
    for pair in filelist:
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            total += 1
    return total

def calculate2(filelist):
    total = 0
    for pair in filelist:
        contains = False
        for item in pair[0]:
            if set([item]).issubset(pair[1]):
                contains = True
        if contains:
            total += 1
    return total

file = open("input.txt", "r")

filelist = file.readlines()

file.close()

filelist = split(filelist)

def driver1():
    global filelist
    ans = calculate1(filelist)
    print(ans)

def driver2():
    global filelist
    ans = calculate2(filelist)
    print(ans)
    
driver2()
