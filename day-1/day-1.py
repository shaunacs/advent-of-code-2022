def count_calories(calorie_list):
    total_calories = 0

    for num in calorie_list:
        total_calories += int(num)

    return total_calories