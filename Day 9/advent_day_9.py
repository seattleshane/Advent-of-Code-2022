import numpy as np

class Head():
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
    
    def move_head(self, direction: str):
        if direction == "U":
            self.y += 1
        if direction == "D":
            self.y -= 1
        if direction == "L":
            self.x -= 1
        if direction == "R":
            self.x += 1

class Tail():
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.cords_traversed: list[tuple[int,int]] = []
        self.cords_traversed.append((0,0))
    def move_tail(self, head: Head):
        knight_move: bool = False
        diagonal: bool = False
        if (self.x - head.x > 1) or (self.y - head.y > 1):
            knight_move = True
        if abs(self.x - head.x) == abs(self.y - head.y):
            diagonal = True
        if knight_move:
            x_distance = (head.x - self.x)
            y_distance = (head.y - self.y)
            if x_distance > 0 or y_distance > 0:
                self.x += 1
                self.y += 1
            else:
                self.x -= 1
                self.y -= 1
        elif diagonal:
            if head.x > self.x:
                self.x += 1 
                self.y += 1
            else:
                self.x -= 1
                self.y -=1
        elif (head.x - self.x) > (head.y - self.y):
                if head.x > self.x:
                    self.x += 1
                else:
                    self.x -= 1
        elif (head.x - self.x) < (head.y - self.y):
            if head.y > self.y:
                self.y += 1
            else:
                self.y -=1
        self.cords_traversed.append((self.x, self.y))
        print(self.cords_traversed)


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
    first_move = True
    for move in lines:
        direction = move.split(" ")[0]
        spaces = int(move.split(" ")[1])
        for i in range(spaces):
            print_position(head, tail)
            if first_move:
                head.move_head(direction)
                first_move = False
            else:
                head.move_head(direction)
                tail.move_tail(head)
    return len(list(set(tail.cords_traversed)))

def part_two(lines: list[str]):
    pass

def print_position(head: Head, tail: Tail):
    game_board = np.zeros((10,10), dtype=str)
    game_board[head.x][head.y] = "H"
    game_board[tail.x][tail.y] = "T"
    print(game_board)
    print("\n")
if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\Shane\\Documents\\GitHub\\Advent-of-Code-2022\\Puzzle Files\\test_input.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")