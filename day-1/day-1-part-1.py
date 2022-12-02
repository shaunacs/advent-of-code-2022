def count_calories(calorie_list):
    total_calories = 0

    for num in calorie_list:
        total_calories += int(num)

    return total_calories


def split_calorie_count(data_file):
    calories = open(data_file)
    current_elf = 1
    calorie_count = {}
    i = 0

    for calorie in calories:
        calorie = calorie.strip()
        if i == 0:
            calorie_count[current_elf] = [calorie]
            i += 1
        elif calorie != '':
            if current_elf not in calorie_count:
                calorie_count[current_elf] = [calorie]
            else:
                calorie_count[current_elf].append(calorie)
        elif calorie == '':
            current_elf += 1


    return calorie_count
        

def calculate_most_calories(calorie_count):
    most_calories = 0

    for elf in calorie_count:
        if count_calories(calorie_count[elf]) > most_calories:
            most_calories = count_calories(calorie_count[elf])

    return most_calories


def find_most_elf_calories(calorie_data):
    return calculate_most_calories(split_calorie_count(calorie_data))


# Answer:
print(find_most_elf_calories('./day-1-input-part-1.txt'))