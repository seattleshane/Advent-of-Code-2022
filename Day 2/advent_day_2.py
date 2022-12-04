from enum import Enum

class OpponentsKey(Enum):
    A = "ROCK"
    B = "PAPER"
    C = "SCISSORS"

class MyKey(Enum):
    X = "ROCK"
    Y = "PAPER"
    Z = "SCISSORS"


class MyFixedAnswer(Enum):
    X = "LOSS"
    Y = "DRAW"
    Z = "WIN"


class Values(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

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

def calculate_score(opponent_pick_str: str, my_pick_str: str):
    for _ in OpponentsKey:
        if opponent_pick_str == _.name:
            opponent_pick = _
    for _ in MyKey:
        if my_pick_str == _.name:
            my_pick = _
    if opponent_pick.value == my_pick.value:
        for value in Values:
            if my_pick.value == value.name:
                return int(value.value + 3)
    match my_pick:
        case MyKey.X:
            if opponent_pick == OpponentsKey.C:
                return 7
            else:
                return 1
        case MyKey.Y:
            if opponent_pick == OpponentsKey.A:
                return 8
            else:
                return 2
        case MyKey.Z:
            if opponent_pick == OpponentsKey.B:
                return 9
            else:
                return 3

def calculate_part_two(opponent_pick_str: str, my_pick_str: str):
    my_new_string = ""
    for _ in OpponentsKey:
        if opponent_pick_str == _.name:
            opponent_pick = _
    for _ in MyFixedAnswer:
        if my_pick_str == _.name:
            my_pick = _
    if my_pick == MyFixedAnswer.Y:
        for _ in MyKey:
            if opponent_pick.value == _.value:
                return calculate_score(opponent_pick_str, _.name)
    match my_pick:
        case MyFixedAnswer.X:
            if opponent_pick == OpponentsKey.A:
                my_new_string = "Z"
            elif opponent_pick == OpponentsKey.B:
                my_new_string = "X"
            else:
                my_new_string = "Y"
        case MyFixedAnswer.Z:
            if opponent_pick == OpponentsKey.A:
                my_new_string = "Y"
            elif opponent_pick == OpponentsKey.B:
                my_new_string = "Z"
            else:
                my_new_string = "X"
    return calculate_score(opponent_pick_str, my_new_string)



def part_one(lines: list[str]):
    total: int = 0
    for line in lines:
        (opponent_pick, my_pick) = line.split(" ")
        total += calculate_score(opponent_pick, my_pick)
    return total

def part_two(lines: list[str]):
    total: int = 0
    for line in lines:
        (opponent_pick, my_pick) = line.split(" ")
        total += calculate_part_two(opponent_pick, my_pick)
    return total

if __name__ == "__main__":
    test = [
        "A Y",
        "B X",
        "C Z",
    ]
    lines = get_values_from_file("C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\day_2.txt")
    print(part_one(lines))
    print(part_two(lines))
