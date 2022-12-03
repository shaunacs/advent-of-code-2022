def split_input(input):
    data = open(input)

    rucksacks = []

    for line in data:
        rucksacks.append(line.strip())
    
    return rucksacks


def divide_rucksacks(rucksacks):
    rucksack_len = len(rucksacks)

    r1 = rucksacks[0:int(rucksack_len / 2)]
    r2 = rucksacks[int(rucksack_len / 2):]

    return [r1, r2]


def find_shared_item(r1, r2):
    for item in r1:
        if item in r2:
            return item


def find_item_priority(item):
    priority_map = {}
    possible_items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counter = 1

    for i in possible_items:
        priority_map[i] = counter
        counter += 1
    
    return priority_map[item]


def total_item_priorities(input):
    total = 0

    rucksacks = split_input(input)

    for rucksack in rucksacks:
        divided_rucksacks = divide_rucksacks(rucksack)
        shared_item = find_shared_item(divided_rucksacks[0], divided_rucksacks[1])
        total += find_item_priority(shared_item)
    
    return total

#Answer
print(total_item_priorities('./input.txt'))