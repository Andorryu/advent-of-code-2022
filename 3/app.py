
def split(bag: str):
    str1, str2 = "", ""
    length = len(bag)

    for i in range(length):
        if i < length / 2:
            str1 += bag[i]
        else:
            str2 += bag[i]
    return str1, str2

def split_baglist(baglist):
    final = []
    for bag in baglist:
        final.append(split(bag))
    return final

def group_baglist(baglist):
    i = 0
    final = []
    group = [None, None, None]
    while i < len(baglist):
        for j in range(3):
            group[j] = baglist[i + j]
        a, b, c = group
        final.append((a, b, c))
        i += 3
    return final
            
def find_similar_items(baglist):
    final:str = ""
    for bag in baglist:
        char = ''
        for i in bag[0]:
            for j in bag[1]:
                if i == j:
                    char = i
                    break
            else:
                continue # continue if loop completes
            break # break out of outer loop if inner breaks
        final += char
    return final

def find_similar_items2(baglist):
    final:str = ""
    for bag in baglist:
        char = ''
        for i in bag[0]:
            for j in bag[1]:
                for k in bag[2]:
                    if i == j and i == k:
                        char = i
                        break
                else:
                    continue # continue if loop completes
                break
            else:
                continue
            break # break out of outer loop if inner breaks
        final += char
    return final

def calculate_score(string):
    score = 0
    for char in string:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            score += ord(char) - ord('a') + 1
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
            score += ord(char) - ord('A') + 27
    return score

def driver1():
    file = open("input.txt", "r")
    filelist: list[str] = file.readlines()
    file.close()

    baglist = []

    # remove new-line ending
    for line in filelist:
        baglist.append(line.removesuffix('\n'))

    # convert baglist from list[str] to list[tuple[str, str]]
    baglist = split_baglist(baglist)

    similar_item_list = find_similar_items(baglist)
    print(calculate_score(similar_item_list))

def driver2():
    file = open("input2.txt", "r")
    filelist: list[str] = file.readlines()
    file.close()

    baglist = []
    
    # remove new-line ending
    for line in filelist:
        baglist.append(line.removesuffix('\n'))

    baglist = group_baglist(baglist)
    similar_items = find_similar_items2(baglist)
    print(calculate_score(similar_items))

driver2()

