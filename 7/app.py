
from directory import Directory
from file import File



def driver():
    TOTAL_SPACE = 70000000 # part 2

    filelines: list[str] = []
    for line in open("input.txt").readlines():
        filelines.append(line.removesuffix('\n'))
    
    root: Directory = Directory("/", None, [])
    current_directory = root

    i = 0
    while i < len(filelines):
        line = filelines[i]
        print(line)
        if line[0] == '$': # cd or ls
            if line[2:4] == "cd": # change current_directory
                if line[5:] == "..":
                    current_directory = current_directory.parent
                    print("moved up to " + current_directory.name + ", child of " + (
                        current_directory.parent.name if current_directory.parent == name else "NONE"
                    ))
                elif line[5:] != "/":
                    current_directory = current_directory.find_dir_by_name(line[5:])
                    print("moved down to " + current_directory.name + ", child of " + current_directory.parent.name)
            elif line[2:4] == "ls": # fill directory on ls command

                j = 1 # offset from i
                offset_line = filelines[i + j]

                while (offset_line[0] != '$'):

                    # read line if it is a directory
                    if offset_line[:3] == "dir":
                        current_directory.items.append(Directory(offset_line[4:], current_directory, []))
                        print("added dir " + offset_line[4:] + " to " + current_directory.name)

                    # read line if it is a file
                    elif offset_line[0].isdigit(): # if the first line is a digit then it must be a file
                        # get info about file
                        size = ''
                        name = ""
                        for c in offset_line:
                            if c == " ":
                                continue
                            if c.isdigit():
                                size += c
                            else:
                                name += c
                        size = int(size) # convert to int
                        # add file to current_directory
                        current_directory.items.append(File(name, size))
                        print("added file " + name + " to " + current_directory.name)

                    j += 1
                    try:
                        offset_line = filelines[i + j]
                    except:
                        break
                i += j - 1 # skip ahead past the files
        i += 1

    def printd(item, depth):
        print(("|   "*depth) + item.name)

    root.tree(printd)
    root.find_size()
    sum = 0
    sizes = root.list()
    for size in sizes:
        if size <= 100000:
            sum += size
    print(sum)

    # part 2
    free_space = TOTAL_SPACE - sizes[0]
    print(f"current free space: {free_space}")
    deletable_sizes = []
    for size in sizes:
        if size >= 30000000 - free_space:
            deletable_sizes.append(size)

    lowest_size = deletable_sizes[0]
    for size in deletable_sizes:
        if size < lowest_size:
            lowest_size = size
    print(f"Lowest size is {lowest_size}")


driver()
