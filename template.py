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
    pass

def part_two(lines: list[str]):
    pass


if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\test_input.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")