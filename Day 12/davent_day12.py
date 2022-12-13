import numpy as np


class GameBoard():
    def __init__(
        self,
        matrix,
        start_x: int,
        start_y: int,
        goal_x: int,
        goal_y: int,
        width: int,
        height: int,
    ):
        self.matrix = matrix
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.goal_x: int = goal_x
        self.goal_y: int = goal_y
        self.width: int = width
        self.height: int = height


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
    game_board: GameBoard = parse_input(lines)
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
    open_list: dict[tuple[int, int], int] = {}
    closed_list: dict[tuple[int, int], int] = {}
    approached_positions: dict[tuple[int, int], bool] = {}
    approached_positions[game_board.goal_y, game_board.goal_x] = True
    open_list[game_board.start_x, game_board.start_y] = 0
    best_distance: int = 1_000_000_000
    distance: int = -1
    while not is_complete:
        new_open_list: dict[tuple[int, int], int] = {}
        for position in open_list:
            if (
                ((position[0], position[1]) not in closed_list)
            ):
                distance = open_list[(position[0], position[1])]
                distance += 1
                heights: list[int] = []
                position_height = game_board.matrix[position[0]][position[1]]
                heights.append(position_height)
                heights.append(position_height + 1)
                # print_game_board(
                #     game_board,
                #     position[0],
                #     position[1],
                #     open_list,
                #     closed_list
                # )
                if position[0] == game_board.goal_y and position[1] == game_board.goal_x:
                    is_complete = True
                    best_distance = distance - 1
                for height in range(position_height - 1, -1, -1):
                    heights.append(height)
                right = position[1] + 1
                left = position[1] - 1
                up = position[0] + 1
                down = position[0] - 1
                if (right) < game_board.width:
                    if (game_board.matrix[position[0]][right] in heights):
                        if ((position[0], right, distance) not in open_list):
                            new_open_list[position[0], right] = distance
                if (left) >= 0:
                    if (game_board.matrix[position[0]][left] in heights):
                        if (((position[0], left, distance) not in open_list)):
                            new_open_list[position[0], left] = distance
                if (up) < game_board.height:
                    if (game_board.matrix[up][position[1]] in heights):
                        if (up, position[1], distance) not in open_list:
                            new_open_list[up, position[1]] = distance
                if (down) >= 0:
                    if (game_board.matrix[down][position[1]] in heights):
                        if (down, position[1], distance) not in open_list:
                            new_open_list[down, position[1]] = distance
                closed_list[position[0], position[1]] = distance
        open_list = new_open_list
    return best_distance


def parse_input(lines: list[str]):
    height = len(lines)
    width = len(lines[0])
    matrix = np.zeros((height, width), dtype=int)
    start_x: int = 0
    start_y: int = 0
    goal_x: int = 0
    goal_y: int = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            character = lines[i][j]
            if character == "S":
                start_x = j
                start_y = i
            elif character == "E":
                goal_x = j
                goal_y = i
                matrix[i][j] = 25
            else:
                matrix[i][j] = ord(character) - 97
    return GameBoard(
        matrix,
        start_x,
        start_y,
        goal_x,
        goal_y,
        width,
        height,
    )


def print_game_board(
    game_board: GameBoard,
    position_y: int,
    position_x: int,
    open_list: dict[tuple[int, int], int],
    closed_ist: dict[tuple[int, int], int]
):
    printed_game_board = np.zeros((game_board.height, game_board.width), dtype=str)
    printed_game_board.fill("_")
    for item in open_list:
        printed_game_board[item[0], item[1]] = "0"
    for closed_item in closed_ist:
        printed_game_board[closed_item[0], closed_item[1]] = "X"
    printed_game_board[position_y, position_x] = "█"
    print(printed_game_board)


if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\srideout\\Desktop\\Advent of Code\\example.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")
