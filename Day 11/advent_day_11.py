class Monkey():
    def __init__(
        self,
        monkey: int,
        items: list[int],
        operation_function: str,
        operation_amount: int,
        divisible_by: int,
        true_monkey_to_throw_to: int,
        false_monkey_to_throw_to: int,
    ):
        self.name: int = monkey
        self.items: list[int] = items
        self.operation_function: str = operation_function  
        self.operation_amount: str = operation_amount  
        self.divisible_by: int = divisible_by  
        self.true_monkey_to_throw_to: int = true_monkey_to_throw_to  
        self.false_monkey_to_throw_to: int = false_monkey_to_throw_to
        self.list_of_monkeys: list["Monkey"] = []
        self.inspected_items: int = 0

    def decide_if_throw(self):
        while len(self.items) > 0:
            new_value = self._operation(self.items[0])
            self._throw_item(new_value)
            self.inspected_items += 1

    def _operation(self, item: int):
        if self.operation_function == "+":
            if self.operation_amount.isnumeric():
                return item + int(self.operation_amount)
            else:
                return item + item
        elif self.operation_function == "*":
            if self.operation_amount.isnumeric():
                return item * int(self.operation_amount)
            else:
                return item * item
        
    def _throw_item(self, value: int):
        value = value // 3
        if value % self.divisible_by == 0:
            for monkey in self.list_of_monkeys:
                if monkey.name == self.true_monkey_to_throw_to:
                    monkey.items.append(value)
                    self.items.pop(0)
                    break
        else:
            for monkey in self.list_of_monkeys:
                if monkey.name == self.false_monkey_to_throw_to:
                    monkey.items.append(value)
                    self.items.pop(0)
                    break


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
    list_of_monkeys: list[Monkey] = []
    parse_input(lines, list_of_monkeys)
    for monkey in list_of_monkeys:
        monkey.list_of_monkeys = list_of_monkeys
    for _ in range(20):
        for monkey in list_of_monkeys:
            monkey.decide_if_throw()
        print(f"Round {_}")

    inspected_items: list[int] = []
    for monkey in list_of_monkeys:
        inspected_items.append(monkey.inspected_items)
    inspected_items.sort()
    inspected_items.reverse()
    return inspected_items[0] * inspected_items[1]

def part_two(lines: list[str]):
    pass

def parse_input(parsed_lines: list[str], list_of_monkeys: list[Monkey]):
    for i in range(0, len(parsed_lines), 7):
        lines = parsed_lines[i:i+7]
        monkey = int(lines[0].split("Monkey ")[1][0])
        items: list[int] =  [int(x) for x in lines[1].split("items: ")[1].strip().split(",")]
        operation_function: str = lines[2].split("old ")[1][0]
        operation_amount: str = str(lines[2].split("old ")[1].split(operation_function)[1].strip())
        divisible_by: int = int(lines[3].split("by ")[1])
        true_monkey_to_throw_to: int = int(lines[4].split("monkey ")[1])
        false_monkey_to_throw_to: int = int(lines[5].split("monkey ")[1])
        list_of_monkeys.append(Monkey(
            monkey,
            items,
            operation_function,
            operation_amount,
            divisible_by,
            true_monkey_to_throw_to,
            false_monkey_to_throw_to,
            )
        )

if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\Shane\\Documents\\GitHub\\"
        "Advent-of-Code-2022\\Puzzle Files\\day_11.txt"
    )
    print(part_one(lines))
    print(part_two(lines))
    print("stop")