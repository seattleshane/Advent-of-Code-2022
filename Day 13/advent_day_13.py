class PairOfPackets():
    def __init__(self, left, right):
        self.left = left
        self.right = right

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
    indicies: list[int] = []
    packets = parse_lines(lines)
    for index, packet in enumerate(packets):
        if left_or_right(packet):
            indicies.append(index)


def part_two(lines: list[str]):
    pass


def parse_lines(lines: list[str]):
    packets: list[PairOfPackets] = []
    for i in range(0, len(lines), 3):
        parsed_lines = lines[i:i+3]
        left = eval(parsed_lines[0])
        right = eval(parsed_lines[1])
        packets.append(PairOfPackets(left, right))
    return packets

def left_or_right(packet: PairOfPackets) -> bool:
    left = packet.left
    right = packet.right
    len_left = len(packet.left)
    len_right = len(packet.right)

    if len_left == len_right:
        return evaluate_even(left, right)
    else:
        return False


def evaluate_even(left_list: list, right_list: list) -> bool:
    is_correct: bool = True
    for i in range(len(left_list)):
        left = left_list[i]
        right = right_list[i]
        left_type = type(left_list[i])
        right_type = type(right_list[i])
        if left_type == right_type and left_type == int:
            if left > right:
                return False
        elif left_type == right_type:
            if isinstance(left, list):
                left = unpack_to_list(left)
                right = unpack_to_list(right)
                if left > right:
                    return False
    return is_correct

def unpack_to_list(item) -> list:
    if isinstance(item, int):
        return [item]
    if isinstance(item[0], list):
        unpack_to_list(item)
    else:
        return item

if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\test_input.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")