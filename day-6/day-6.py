def is_unique(marker):
    letter_count = {}

    for char in marker:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            return False
    
    return True


def find_marker(signal):
    end = 4
    marker = signal[:end]

    for i, char in enumerate(signal):
        if is_unique(marker):
            return i + 3
        else:
            marker = signal[i:end]
            end += 1






signal = open('./input.txt').read()

# Part 1 Answer
print(find_marker(signal))




#print(is_unique(starting_marker))