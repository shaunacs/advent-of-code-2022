# Lose = X
# Draw = Y
# Win = Z

def win(shape):
    if shape == 'A':
        return 'Y'
    if shape == 'B':
        return 'Z'
    if shape == 'C':
        return 'X'


def lose(shape):
    if shape == 'A':
        return 'Z'
    if shape == 'B':
        return 'X'
    if shape == 'C':
        return 'Y'


def draw(shape):
    if shape == 'A':
        return 'X'
    if shape == 'B':
        return 'Y'
    if shape == 'C':
        return 'Z'

def translate_outcome(letter):
    if letter == 'X':
        return 'Lose'
    if letter == 'Y':
        return 'Draw'
    if letter == 'Z':
        return 'Win'

def calculate_outcome_shape(outcome, shape):
    if outcome == 'Lose':
        return lose(shape)
    if outcome == 'Draw':
        return draw(shape)
    if outcome == 'Win':
        return win(shape)


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
        opponent = game[0]
        outcome = translate_outcome(game[2])
        shape_to_play = calculate_outcome_shape(outcome, opponent)
        
        total += calculate_shape_score(shape_to_play) + calculate_outcome_score(outcome)
    
    return total

#Answer
print(calculate_total_score('./input.txt'))