import numpy as np


class Head():
    def __init__(self):
        self.x: int = 0
        self.y: int = 0

    def move_head(self, direction: str, tail: "Tail"):
        if direction == "U":
            self.y += 1
        if direction == "D":
            self.y -= 1
        if direction == "L":
            self.x -= 1
        if direction == "R":
            self.x += 1
        print(f"Head: {self.x}, {self.y}")
        print(f"Tail: {tail.x}, {tail.y}")
        print("Next move tail")

class Tail():
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.cords_traversed: list[tuple[int, int]] = []
        self.cords_traversed.append((0, 0))

    def move_tail(self, head: Head):
        diagonal: bool = False
        touching: bool = False
        x_difference = (self.x - head.x)
        y_difference = (self.y - head.y)
        touching_distances = [1, 0, -1]
        diagonal_distances_1 = [2, -2]
        diagonal_distances_2 = [1, -1]
        if x_difference in touching_distances and y_difference in touching_distances:
            touching = True
        if x_difference in diagonal_distances_1 and y_difference in diagonal_distances_2:
            diagonal = True
        if y_difference in diagonal_distances_1 and x_difference in diagonal_distances_2:
            diagonal = True
        if touching:
            pass
        elif diagonal:
            if head.x > self.x:
                if head.y > self.y:
                    self.x += 1
                    self.y += 1
                else:
                    self.x += 1
                    self.y -= 1
            else:
                if head.y > self.y:
                    self.x -= 1
                    self.y += 1
                else:
                    self.x -= 1
                    self.y -= 1             
        elif abs(head.x - self.x) > abs(head.y - self.y):
            if head.x > self.x:
                self.x += 1
            else:
                self.x -= 1
        elif abs(head.y - self.y) > abs(head.x - self.x):
            if head.y > self.y:
                self.y += 1
            else:
                self.y -= 1
        self.cords_traversed.append((self.x, self.y))
        print(f"Head: {head.x}, {head.y}")
        print(f"Tail: {self.x}, {self.y}")
        print("Next move head")


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
    head = Head()
    tail = Tail()
    for move in lines:
        direction = move.split(" ")[0]
        spaces = int(move.split(" ")[1])
        for i in range(spaces):
            head.move_head(direction, tail)
            # print_position(head, tail)
            tail.move_tail(head)
            # print_position(head, tail)
    return len(list(set(tail.cords_traversed)))


def part_two(lines: list[str]):
    pass


def print_position(head: Head, tail: Tail):
    game_board = np.zeros((10, 10), dtype=str)
    game_board.fill("0")
    game_board[head.x][head.y] = "H"
    game_board[tail.x][tail.y] = "T"
    print(game_board)
    print("\n")


if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\srideout\\Desktop\\Advent of Code\\day_9.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")
