import part1
import io

def convert(outcome, opponent):
    if opponent == 'A':
        if outcome == 'X':
            return "scissors", "rock"
        elif outcome == 'Y':
            return "rock", "rock"
        else:
            return "paper", "rock"
    elif opponent == 'B':
        if outcome == 'X':
            return "rock", "paper"
        elif outcome == 'Y':
            return "paper", "paper"
        else:
            return "scissors", "paper"
    elif opponent == 'C':
        if outcome == 'X':
            return "paper", "scissors"
        elif outcome == 'Y':
            return "scissors", "scissors"
        else:
            return "rock", "scissors"
    else:
        return '', ''

def parse_line(file: io.TextIOWrapper):
    char = '' # read from file
    outcome = '' # outcome
    opponent = '' # opponent's choice
    player = '' # player's choice

    for i in range(4):
        char = file.read(1)
        if i == 0:
            opponent = char
        elif i == 2:
            outcome = char
    
    return convert(outcome, opponent)

def read_file(file: io.TextIOWrapper):
    game = []
    running = True

    while running:
        round = parse_line(file)
        if round == ("", ""):
            running = False
        else:
            game.append(round)
    
    return game

print(str(part1.calculate_points(read_file(open("input.txt", "r")))))
