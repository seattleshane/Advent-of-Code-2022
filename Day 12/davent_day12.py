import numpy as np

class GameBoard():
    def __init__(
        self,
        matrix,
        start_x: int,
        start_y: int,
        goal_x: int,
        goal_y: int,
    ):
        self.matrix = matrix
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.goal_x: int = goal_x
        self.goal_y: int = goal_y
        

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
    game_board: game_board = parse_input(lines)
    simple_path(game_board)

def part_two(lines: list[str]):
    pass

# def pathing(game_board: GameBoard):
#     north_path: list[int] = []
#     south_path: list[int] = []
#     east_path: list[int] = []
#     west_path: list[int] = []
#     paths = list[list[int]] = []
#     for east in range(len(
#         game_board.start_x),
#         len(game_board.start_x) - game_board.start_x
#     ):
#         east_path.append(game_board.matrix[east][game_board.start_y])

#     for west in range(len(
#         game_board.start_x),
#         game_board.start_x -len(game_board.start_x), -1
#     ):
#         west_path.append(game_board.matrix[west][game_board.start_y])

#     for north in range(len(
#         game_board.start_y),
#         len(game_board.start_y) - game_board.start_y
#     ):
#         north_path.append(game_board.matrix[game_board.start_y][north])
#     for south in range(len(
#         game_board.start_y),
#         game_board.start_y -len(game_board.start_y), -1
#     ):
#         south_path.append(game_board.matrix[game_board.start_y][south])
#     paths.append(
#         north_path,
#         south_path,
#         east_path,
#         west_path,
# )

def simple_path(game_board: GameBoard):
    is_complete: bool = False
    open_list: list[tuple[int, int]] = []
    closed_list: list[tuple[int, int]] = []
    best_distance: int = 1_000_000_000
    while not is_complete:
        open_list.append((game_board.start_x, game_board.start_y))
        for position in open_list:
            if position not in closed_list:
                heights: list[int] = []
                position_height = game_board.matrix[position[0]][position[1]]
                heights.append(position_height)
                heights.append(position_height + 1)
                for height in range(position_height, 0, -1):
                    heights.append(height)
                if (game_board.matrix[position[0]][position[1] + 1] in heights):
                    open_list.append((position[0], position[1]))
                else:
                    closed_list.append((position[0], position[1] + 1))

                if (game_board.matrix[position[0]][position[1] - 1] in heights):
                    open_list.append((position[0], position[1] - 1))
                else:
                    closed_list.append((position[0], position[1] - 1))

                if (game_board.matrix[position[0] + 1][position[1]] in heights):
                    open_list.append((position[0], position[1]))
                else:
                    closed_list.append((position[0] + 1, position[1]))

                if (game_board.matrix[position[0] - 1][position[1]] in heights):
                    open_list.append((position[0] - 1, position[1]))
                else:
                    closed_list.append((position[0] - 1, position[1]))
            if (position[0], position[1]) in open_list:
                if len(open_list) < best_distance:
                    best_distance = len(open_list)
        
def parse_input(lines: list[str]):
    matrix = np.zeros((len(lines[0]), len(lines[0])), dtype=int)
    start_x: int = 0
    start_y: int = 0
    goal_x: int = 0
    goal_y: int = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            character = lines[i][j]
            if character == "S":
                start_x = i
                start_y = j
            elif character == "E":
                goal_x = i
                goal_y = j
            else:
                matrix[i][j] = ord(character) - 97
    return GameBoard(
        matrix,
        start_x,
        start_y,
        goal_x,
        goal_y,
    )

if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\test_input.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")