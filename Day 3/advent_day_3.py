values_dict = {
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23, 
    "x": 24,
    "y": 25,
    "z": 26,
}

def get_values_from_file(path_to_file: str) -> list[str]:
    """Takes a path to a text file and returns the lines as a list of strings.

    Args:
        path_to_file (str): Absolute path to file.

    Returns:
        list[str]: Lines as a list of strings
    """
    ruck_sacks = []
    with open(path_to_file) as file:
        while (line := file.readline().rstrip()):
            ruck_sacks.append(line)
    return ruck_sacks

def part_one(ruck_sacks: list[str]) -> int:
    """Part one of the Advent of code day 3 challenge.

    Args:
        ruck_sacks (list[str]): List of strings to return

    Returns:
        int: Total
    """
    total = []
    for rucksack in ruck_sacks:
        compartment_1 = []
        compartment_2 = []
        compartment_size = int(len(rucksack)/2)
        shared_items = []
        for i in range(compartment_size):
            compartment_1.append(rucksack[i])
            compartment_2.append(rucksack[i + compartment_size])
        for j in range(compartment_size):
            if compartment_1[j] in compartment_2:
                if compartment_1[j] not in shared_items:
                    shared_items.append(compartment_1[j])
        for shared_item in shared_items:
            total.append(values_dict.get(shared_item))
    return sum(total)

def part_two(ruck_sacks: list[str], group_size: int = 3) -> int:
    """Part two of the Advent of code day 3 challenge.

    Args:
        ruck_sacks (list[str]): List of strings to return

    Returns:
        int: Total
    """
    total = []
    for i in range(0, len(ruck_sacks), group_size):
        grouped_rucksacks = [ruck_sacks[i + j] for j in range(group_size)]
        grouped_rucksacks.sort(key=len)
        for character in grouped_rucksacks[0]:
            if character in grouped_rucksacks[1] and character in grouped_rucksacks[2]:
                group_badge = character
                break
        if group_badge:
            total.append(values_dict.get(group_badge))
    print(total)
    return sum(total)

if __name__ == "__main__":
    ruck_sacks = get_values_from_file("Path to file")
    part_one(ruck_sacks)
    part_two(ruck_sacks)