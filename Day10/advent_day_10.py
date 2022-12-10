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
    x: int = 1
    cycle: int = 0
    signals_of_interest: list[int] = []
    debug_list: list[tuple[int, str]] = []
    for instruction in lines:
        if len(instruction.split(" ")) == 1:
            cycle += 1
            debug_list.append((cycle,  x, instruction, (cycle * x), 0))
            calculate_signal_strength(cycle, x, signals_of_interest,)
        else:
            cycle += 1
            debug_list.append((cycle,  x, instruction, (cycle * x), int(instruction.split(" ")[1])))
            calculate_signal_strength(cycle, x, signals_of_interest,)
            cycle += 1
            debug_list.append((cycle,  x, instruction, (cycle * x), int(instruction.split(" ")[1])))
            calculate_signal_strength(cycle, x, signals_of_interest,)
            x += int(instruction.split(" ")[1])
    return sum(signals_of_interest)

def part_two(lines: list[str]):
    x: int = 1
    cycle: int = 0
    signals_of_interest: list[int] = []
    debug_list: list[tuple[int, str]] = []
    for instruction in lines:
        if len(instruction.split(" ")) == 1:
            cycle += 1
            debug_list.append((cycle,  x, instruction, (cycle * x), 0))
            calculate_signal_strength(cycle, x, signals_of_interest,)
        else:
            cycle += 1
            debug_list.append((cycle,  x, instruction, (cycle * x), int(instruction.split(" ")[1])))
            calculate_signal_strength(cycle, x, signals_of_interest,)
            cycle += 1
            debug_list.append((cycle,  x, instruction, (cycle * x), int(instruction.split(" ")[1])))
            calculate_signal_strength(cycle, x, signals_of_interest,)
            x += int(instruction.split(" ")[1])
    line: str = ""
    counter = 0
    for item in debug_list:
        if (
            counter == item[1] + 1 or
            counter == item[1] - 1 or
            counter == item[1]
        ):
            line += "#"
        else:
            line += "."
        counter += 1
        if counter % 40 == 0:
            print(str(line))
            line = ""
            counter = 0

            

def calculate_signal_strength(cycle: int, x: int, signals: list[int]) -> int:
    if cycle == 20:
        signals.append(cycle * x)
    elif (cycle + 20) % 40 == 0:
        signals.append(cycle * x)
        print(f"during {cycle} added {cycle} * {x}")

if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\day_10.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")