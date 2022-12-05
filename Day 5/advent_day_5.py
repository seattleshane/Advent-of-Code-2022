import numpy as np

class Martix(list[list[str]]):
    pass

def create_matrix(lines: list[str]) -> list[list[str]]:
    matrix: list[list[str]] = []
    for i in range(8):
        matrix.append(lines[i])

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
    matrix = create_matrix(lines)
    final_string: str = ""
    for i in range(10, len(lines)):
        line_list = lines[i].split(" ")
        move_amount = int(line_list[1])
        start_column = int(line_list[3]) - 1
        end_column = int(line_list[-1]) - 1
        for j in range(move_amount):
            matrix[end_column].append(matrix[start_column][len(matrix[start_column]) - 1])
            matrix[start_column].pop()
    for k in range(len(matrix)):
        final_string += matrix[k][len(matrix[k]) - 1]
    return final_string

def part_two(lines: list[str]):
    matrix = create_matrix(lines)
    final_string: str = ""
    for i in range(10, len(lines)):
        line_list = lines[i].split(" ")
        move_amount = int(line_list[1])
        start_column = int(line_list[3]) - 1
        end_column = int(line_list[-1]) - 1
        cargo_list: list[str] = []
        for j in range(move_amount):
            cargo_list.append(matrix[start_column][len(matrix[start_column]) - 1])
            matrix[start_column].pop()
        cargo_list.reverse()
        for cargo in cargo_list:
            matrix[end_column].append(cargo)
        cargo_list = []
    for k in range(len(matrix)):
        final_string += matrix[k][len(matrix[k]) - 1]
    return final_string

def create_matrix(lines: list[str]):
    matrix = np.zeros((8, 9), dtype=str)
    for i in range(8):
        matrix[i, 0] = lines[i][1]
        counter = 1
        for j in range(5, len(lines[i]), 4):
            matrix[i, counter] = lines[i][j]
            counter += 1
    matrix = np.rot90(matrix)
    list_matrix: list[list[str]] = []
    sub_list: list[str] =[]
    for row in matrix:
        for character in row:
            sub_list.append(character)
        sub_list.reverse()
        for i in range(len(sub_list) - 1, 0, -1):
            if sub_list[i] == " ":
                sub_list.remove(" ")
        list_matrix.append(sub_list)
        sub_list = []
    list_matrix.reverse()
    return list_matrix

        

if __name__ == "__main__":
    lines = get_values_from_file("C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\day_5.txt")
    print(part_one(lines))
    print(part_two(lines))