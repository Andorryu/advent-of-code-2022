
import io

choice_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

outcome_points = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

# input player and opponent's choice
# output outcome
def play(player, opponent):
    if player == "rock":
        if opponent == "rock":
            return "draw"
        elif opponent == "paper":
            return "lose"
        else:
            return "win"
    elif player == "paper":
        if opponent == "rock":
            return "win"
        elif opponent == "paper":
            return "draw"
        else:
            return "lose"
    else:
        if opponent == "rock":
            return "lose"
        elif opponent == "paper":
            return "win"
        else:
            return "draw"

# input character from file
# output what it corresponds to in rock paper scissors
def convert(char):
    if char == 'A' or char == 'X':
        return "rock"
    elif char == 'B' or char == 'Y':
        return "paper"
    elif char == 'C' or char == 'Z':
        return "scissors"
    else:
        return ''

# input file
# output double of the following form: (player's choice, opponent's choice)
def parse_line(file: io.TextIOWrapper):
    char = '' # read from file
    player = '' # player's choice
    opponent = '' # opponent's choice

    for i in range(4):
        char = file.read(1)
        if i == 0:
            opponent = convert(char)
        elif i == 2:
            player = convert(char)

    return player, opponent

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

def calculate_points(game: list[tuple[str, str]]):
    score = 0
    for round in game:
        # points based on choice
        for choice in choice_points:
            if round[0] == choice:
                score += choice_points[choice]
        # points based on outcome
        for outcome in outcome_points:
            if play(round[0], round[1]) == outcome:
                score += outcome_points[outcome]
    return score

print(str(calculate_points(read_file(open("input.txt", "r")))))
