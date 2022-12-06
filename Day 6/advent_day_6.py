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

def part_one(lines: list[str]):
    for line in lines:
        for i in range(0, len(line)):
            packet = ""
            found_characters = set()
            for j in range(i, i + 4):
                packet += line[j]
                if line[j] not in found_characters:
                    found_characters.add(line[j])
            if len(packet) == len(found_characters):
                return i + 4

def part_two(lines: list[str]):
    for line in lines:
        for i in range(0, len(line)):
            packet = ""
            found_characters = set()
            for j in range(i, i + 14):
                packet += line[j]
                if line[j] not in found_characters:
                    found_characters.add(line[j])
            if len(packet) == len(found_characters):
                return i + 14

if __name__ == "__main__":
    lines = get_values_from_file("C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\day_6.txt")
    print(part_one(lines))
    # print(part_two(lines))