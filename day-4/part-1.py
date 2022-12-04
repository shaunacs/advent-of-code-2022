def split_input(input):
    pairings = open(input)
    pairs = []

    for pair in pairings:
        pairs.append(pair.strip().split(','))
    
    return pairs


def create_range_list(assignment):

    assignment_range = assignment.split('-')

    start = int(assignment_range[0])
    end = int(assignment_range[1])

    range_list = []

    counter = start

    while counter <= end:
        range_list.append(counter)
        counter +=1

    return range_list
    

def is_assignment_overlap(pair):
    first_assignment = create_range_list(pair[0])
    second_assignment = create_range_list(pair[1])
    track_overlap = []


    if len(first_assignment) == len(second_assignment):
        track_overlap = second_assignment

        for assignment in first_assignment:
            if assignment in track_overlap:
                track_overlap.remove(assignment)

    elif len(first_assignment) > len(second_assignment):
        track_overlap = second_assignment

        for assignment in first_assignment:
            if assignment in second_assignment:
                second_assignment.remove(assignment)

    elif len(second_assignment) > len(first_assignment):
        track_overlap = first_assignment

        for assignment in second_assignment:
            if assignment in first_assignment:
                first_assignment.remove(assignment)
                
    
    if track_overlap == []:
        return True
    else:
        return False

def count_overlap(input):
    pairs = split_input(input)
    counter = 0

    for pair in pairs:
        if is_assignment_overlap(pair):
            counter += 1
    return counter

#Answer
print(count_overlap('./input.txt'))