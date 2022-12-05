def get_values_from_file(path_to_file: str) -> list[str]:
    """Takes a path to a text file and returns the lines as a list of strings.

    Args:
        path_to_file (str): Absolute path to file.

    Returns:
        list[str]: Lines as a list of strings
    """
    with open(path_to_file) as file:
        lines = file.readlines()
        stripped_lines = [line.rstrip() for line in lines]
        return stripped_lines

def part_one(lines: list[str]) -> int:
    """Returns the highest amount of calories an elf is carrying

    Args:
        lines (list[str]): list of calories

    Returns:
        int: highest amount of calories
    """
    highest_calories: int = 0
    calories: int = 0
    for i in range(len(lines)):
        if lines[i]:
            calories += int(lines[i])
        else:
            if calories >= highest_calories:
                highest_calories = calories
                calories = 0
            else:
                calories = 0
    return highest_calories

def part_two(lines: list[str]) -> int:
    """Returns the sum of the top three caloric elfs

    Args:
        lines (list[str]): list of calories

    Returns:
        int: sum of the top 3 elfs highest amount of calories
    """
    calories: int = 0
    top_3_highest_calories: list[int] = [0,0,0]
    for i in range(len(lines)):
        if lines[i]:
            calories += int(lines[i])
        else:
            top_3_highest_calories.sort()
            for index, highest_calorie in enumerate(top_3_highest_calories):
                if calories >= highest_calorie:
                    top_3_highest_calories[index] = calories
                    calories = 0
                    break
                else:
                    calories = 0
    return sum(top_3_highest_calories)

if __name__ == "__main__":
    lines = get_values_from_file("path")
    print(part_two(lines))