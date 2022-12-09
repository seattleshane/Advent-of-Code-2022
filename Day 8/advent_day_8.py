import numpy as np

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
    result_matrix = np.zeros((len(lines), len(lines)), dtype=str)
    length_of_matrix = len(matrix)
    count_of_trees = (length_of_matrix * 4) - 4

    index_of_seen_trees = []
    for i in range(1, length_of_matrix-1):
        for j in range(1, length_of_matrix-1):
            #loops over the entire matrix each cell is matrix[i][j]
            cell = matrix[i][j]
            cell_index = (i,j)
            tree_checks = []
            tree_check = True
            for k in range(0, i):
                comparison_cell = matrix[k,j]
                comparison_index = (k,j)
                if (cell <= comparison_cell):
                    tree_check = False
            tree_checks.append(tree_check)
            tree_check = True
            for l in range(i+1, length_of_matrix):
                comparison_cell = matrix[l,j]
                comparison_index = (l,j)
                if (cell <= comparison_cell):
                    tree_check = False
            tree_checks.append(tree_check)
            tree_check = True
            for n in range(0, j):
                comparison_cell = matrix[i,n]
                comparison_index = (i,n)
                if (cell <= comparison_cell):
                    tree_check = False
            tree_checks.append(tree_check)
            tree_check = True
            for m in range(j+1, length_of_matrix):
                comparison_cell = matrix[i,m]
                comparison_index = (i,m)
                if (cell <= comparison_cell):
                    tree_check = False
            tree_checks.append(tree_check)
            if True in tree_checks:
                result_matrix[i,j] = "X"
                count_of_trees += 1
            else:
                result_matrix[i,j] = "O"
    return count_of_trees

def part_two(lines: list[str]):
    matrix = create_matrix(lines)
    result_matrix = np.zeros((len(lines), len(lines)), dtype=int)
    length_of_matrix = len(matrix)
    count_of_trees = (length_of_matrix * 4) - 4

    index_of_seen_trees = []
    for i in range(1, length_of_matrix-1):
        for j in range(1, length_of_matrix-1):
            #loops over the entire matrix each cell is matrix[i][j]
            cell = matrix[i][j]
            if i == 2 and j == 1:
                print("stop")
            cell_index = (i,j)
            tree_checks = []
            top = 0
            bottom = 0
            left = 0
            right = 0
            tree_check = True
            for k in range(i-1, -1, -1):
                comparison_cell = matrix[k,j]
                comparison_index = (k,j)
                if (cell <= comparison_cell):
                    tree_check = False
                    top += 1
                    break
                else:
                    top += 1
            for l in range(i+1, length_of_matrix):
                comparison_cell = matrix[l,j]
                comparison_index = (l,j)
                if (cell <= comparison_cell):
                    bottom += 1
                    break
                else:
                    bottom += 1
            for n in range(j-1, -1, -1):
                comparison_cell = matrix[i,n]
                comparison_index = (i,n)
                if (cell <= comparison_cell):
                    left += 1
                    break
                else:
                    left += 1
            tree_checks.append(tree_check)
            tree_check = True
            for m in range(j+1, length_of_matrix):
                comparison_cell = matrix[i,m]
                comparison_index = (i,m)
                if (cell <= comparison_cell):
                    right += 1
                    break
                else:
                    right += 1
            tree_checks.append(tree_check)
            result_matrix[i,j] = (top * bottom * left * right)
    highest_value = 0
    for i in range(length_of_matrix):
        for j in range(length_of_matrix):
            if result_matrix[i][j] > highest_value:
                highest_value = result_matrix[i][j]
    return highest_value


def create_matrix(lines: list[str]):
    matrix = np.zeros((len(lines), len(lines)), dtype=int)
    for i in range(len(lines)):
        for j in range(len(lines)):
            # matrix[i,j] = (int(lines[i][j]), counter)
            matrix[i,j] = int(lines[i][j])
    #         counter += 1
    # matrix_north = matrix
    # matrix_south = np.rot90(matrix_north)
    # matrix_east = np.rot90(matrix_south)
    # matrix_west = np.rot90(matrix_east)
    # list_of_matrix: list[list[str]] = [
    #     matrix_north,
    #     matrix_south,
    #     matrix_east,
    #     matrix_west,
    # ]
    # list_of_sides = []
    # sub_list = []
    # for matrix in list_of_matrix:
    #     for row in matrix:
    #         sub_list = []
    #         for character in row:
    #             sub_list.append((int(character[0]), int(character[1])))
    #             counter += 1
    #         list_of_sides.append(sub_list)
    #         sub_list = []
    return matrix

if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\day_8.txt"
    )
    #lines = get_values_from_file("example.txt")
    # print(part_one(lines))
    print(part_two(lines))
    print("stop")