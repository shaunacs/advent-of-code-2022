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

    for caloire in calorie_count:
        calorie_count[caloire] = count_calories(calorie_count[caloire])


    return calorie_count
        

def calculate_most_calories(calorie_count):
    most_calories = 0

    for elf in calorie_count:
        if count_calories(calorie_count[elf]) > most_calories:
            most_calories = count_calories(calorie_count[elf])

    return most_calories


def find_top_three(calorie_data):
    sorted_calorie_data = dict(sorted(split_calorie_count(calorie_data).items(), reverse=True, key=lambda item: item[1]))

    keys = list(sorted_calorie_data)

    num_1 = keys[0]
    num_1_val = int(sorted_calorie_data[num_1])

    num_2 = keys[1]
    num_2_val = int(sorted_calorie_data[num_2])

    num_3 = keys[2]
    num_3_val = int(sorted_calorie_data[num_3])

    return num_1_val + num_2_val + num_3_val


# Answer:
print(find_top_three('./day-1-input.txt'))