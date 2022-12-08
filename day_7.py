class Directory():
    def __init__(self, name: str, parent):  # type: ignore
        self.parent = parent
        self.name = name
        self.children: list[Directory] = []
        self.file_sizes: list[int] = []
        self.directory_size = 0

    def __str__(self, level=0):
        ret = "\t"*level+repr(f"{self.name}-{self.directory_size}")+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret



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
    current_directory: None | Directory = None
    parent_directory: None | Directory = None
    final_list = []
    for i in range(len(lines)):
        line = lines[i]
        if line == "$ ls":
            pass
        elif line.split(" ")[1] == "cd" and line.split(" ")[2] != "..":
            if current_directory:
                if current_directory.children:
                    for j in range(len(current_directory.children)):
                        if current_directory.children[j].name == line.split(" ")[2]:
                            current_directory = current_directory.children[j]
                            break
            else:
                directory = Directory(line.split("$ cd ")[1], None)
                parent_directory = directory
                current_directory = directory
        elif line == "$ cd ..":
            if current_directory and current_directory.parent:
                current_directory = current_directory.parent
        elif line.split(" ")[0] == "dir":
            if current_directory:
                current_directory.children.append(
                    Directory(
                        line.split(" ")[1],
                        current_directory
                    ))
        elif line.split(" ")[0].isnumeric():
            if current_directory:
                current_directory.file_sizes.append(
                    int(line.split(" ")[0])
                )
        else:
            print("error")
    if parent_directory:
        get_directory_size(parent_directory)
        total_values: list[int] = []
        final_list = check_if_valid_directory(parent_directory, total_values)
    print(str(parent_directory))
    return sum(final_list)


def part_two(lines: list[str]):
    current_directory: None | Directory = None
    parent_directory: None | Directory = None
    final_list = []
    for i in range(len(lines)):
        line = lines[i]
        if line == "$ ls":
            pass
        elif line.split(" ")[1] == "cd" and line.split(" ")[2] != "..":
            if current_directory:
                if current_directory.children:
                    for j in range(len(current_directory.children)):
                        if current_directory.children[j].name == line.split(" ")[2]:
                            current_directory = current_directory.children[j]
                            break
            else:
                directory = Directory(line.split("$ cd ")[1], None)
                parent_directory = directory
                current_directory = directory
        elif line == "$ cd ..":
            if current_directory and current_directory.parent:
                current_directory = current_directory.parent
        elif line.split(" ")[0] == "dir":
            if current_directory:
                current_directory.children.append(
                    Directory(
                        line.split(" ")[1],
                        current_directory
                    ))
        elif line.split(" ")[0].isnumeric():
            if current_directory:
                current_directory.file_sizes.append(
                    int(line.split(" ")[0])
                )
        else:
            print("error")
    if parent_directory:
        get_directory_size(parent_directory)
        total_values: list[int] = []
        final_list = list_directory_sizes(parent_directory, total_values)
        final_list.sort()
        TOTAL_SPACE = 70_000_000
        TARGET_SPACE = 30_000_000
        used_space = final_list[-1]
        free_space = TOTAL_SPACE - used_space
        needed_space = TARGET_SPACE - free_space
        print(needed_space)
        highest_value = used_space
        for file_size in final_list:
            if file_size >= needed_space and file_size < highest_value:
                highest_value = file_size
        print(highest_value)

def get_directory_size(directory: Directory) -> int:
    directory_size = 0
    directory_size += sum(directory.file_sizes)
    print(f"{directory.name}-{directory_size}")
    if directory.children:
        for children in directory.children:
            directory_size += get_directory_size(children)
    print(f"{directory.name}-{directory_size}")
    directory.directory_size = directory_size
    return directory_size


def list_directory_sizes(directory: Directory, directory_sizes: list[int]):
    directory_sizes.append(directory.directory_size)
    if directory.children:
        for children in directory.children:
            list_directory_sizes(children, directory_sizes)
    return directory_sizes


def check_if_valid_directory(directory: Directory, list_of_directory_values: list[int]) -> list[int]:
    if directory.directory_size <= 100_000:
        list_of_directory_values.append(directory.directory_size)   
    if directory.children:
        for children in directory.children:
            check_if_valid_directory(children, list_of_directory_values)
    return list_of_directory_values


if __name__ == "__main__":
    lines = get_values_from_file(
        "C:\\Users\\srideout\\Desktop\\Advent of Code\\day_7.txt"
    )
    #lines = get_values_from_file("example.txt")
    print(part_one(lines))
    print(part_two(lines))
