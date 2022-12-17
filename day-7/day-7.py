class Tree:
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"


class Node:
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"




def split_input(input):
    terminal_output = open(input)
    terminal_output_list = []

    for line in terminal_output:
        terminal_output_list.append(line.strip())
    
    return terminal_output_list


def split_command_line(command):
    return command.split()

terminal_output = split_input('./input.txt')

files = Tree(Node('/', []))
print(files)




# directories = {}
# location = ""

# for line in terminal_output:
#     commands = split_command_line(line)
#     if commands[0] == '$':
#         if commands[1] == 'cd':
#             if location not in directories:
#                 directories[commands[2]] = {}
#                 location = commands[2]
#         elif commands[1] == 'ls':
#             continue
#     if commands[0] == 'dir':
#         if commands[1] not in directories[location]:
#             directories[location][commands[1]] = {}
#         #else:
#             #directories[location][commands[1]].add()
#     elif commands[0] != '$':
#         directories[location][commands[1]] = commands[0]

#     print(directories)
