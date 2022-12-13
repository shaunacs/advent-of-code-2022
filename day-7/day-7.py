def split_input(input):
    terminal_output = open(input)
    terminal_output_list = []

    for line in terminal_output:
        terminal_output_list.append(line.strip())
    
    return terminal_output_list


def split_command_line(command):
    return command.split()

terminal_output = split_input('./input.txt')
directories = {}
location = ""

for line in terminal_output:
    commands = split_command_line(line)
    if commands[0] == '$':
        if commands[1] == 'cd':
            if location not in directories:
                directories[commands[2]] = {}
                location = commands[2]
        elif commands[1] == 'ls':
            continue
    if commands[0] == 'dir':
        if commands[1] not in directories[location]:
            directories[location][commands[1]] = {}
        #else:
            #directories[location][commands[1]].add()
    elif commands[0] != '$':
        directories[location][commands[1]] = commands[0]

    print(directories)
