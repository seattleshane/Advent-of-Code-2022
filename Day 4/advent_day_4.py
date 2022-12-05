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

def parse_sequence(lines: list[str]):
    count = 0
    sequences: list[tuple[int,int,int,int]] = []
    for line in lines:
        split = line.find(",")
        start_1_index = line[0:split].find("-")
        start_1 = int(line[0:start_1_index])
        end_1 = int(line[start_1_index + 1:split])
        start_2_index = split + line[split:len(line)].find("-")
        start_2 = int(line[split + 1:start_2_index])
        end_2 = int(line[start_2_index + 1:])
        sequences.append((start_1, start_2, end_1, end_2))
    return sequences

def part_one(sequences: list[tuple[int,int,int,int]]) -> int:
    count = 0
    for sequence in sequences:
        (start_1, start_2, end_1, end_2) = sequence
        if (start_2 >= start_1 and end_2 <= end_1) or (start_1 >= start_2 and end_1 <= end_2):
                count += 1
    return count

def part_two(sequences: list[tuple[int,int,int,int]]) -> int:
    count: int = 0
    for sequence in sequences:
        (start_1, start_2, end_1, end_2) = sequence
        set_1 = set(range(start_1, end_1 + 1))
        set_2 = set(range(start_2, end_2 + 1))
        if not set_1.isdisjoint(set_2):
            count += 1
    return count
if __name__ == "__main__":
    lines = get_values_from_file("C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\day_4.txt")
    sequence = parse_sequence(lines)
    print(part_one(sequence))
    print(part_two(sequence))