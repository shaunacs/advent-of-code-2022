# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

def win_or_lose(opponent, you):
    if opponent == 'A' and you == 'X':
        return 'Draw'
    if opponent == 'A' and you == 'Y':
        return 'Win'
    if opponent == 'A' and you == 'Z':
        return 'Lose'
    if opponent == 'B' and you == 'X':
        return 'Lose'
    if opponent == 'B' and you == 'Y':
        return 'Draw'
    if opponent == 'B' and you == 'Z':
        return 'Win'
    if opponent == 'C' and you == 'X':
        return 'Win'
    if opponent == 'C' and you == 'Y':
        return 'Lose'
    if opponent == 'C' and you == 'Z':
        return 'Draw'


def split_input(input_file):
    game_data = open(input_file)
    games = []

    for line in game_data:
        games.append(line.strip())
    
    return games


def calculate_shape_score(shape):
    if shape == 'X':
        return 1
    if shape == 'Y':
        return 2
    if shape == 'Z':
        return 3


def calculate_outcome_score(outcome):
    if outcome == 'Lose':
        return 0
    if outcome == 'Draw':
        return 3
    if outcome == 'Win':
        return 6


def calculate_round_score(shape, outcome):
    return calculate_shape_score(shape) + calculate_outcome_score(outcome)


def calculate_total_score(input):
    total = 0
    for game in split_input(input):
        total += calculate_round_score(game[2], win_or_lose(game[0], game[2]))
    
    return total


#Answer
print(calculate_total_score('./input.txt'))