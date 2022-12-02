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