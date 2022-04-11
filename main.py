from string import ascii_uppercase


def maybe_int(s):

    try:
        return int(s)
    except:
        return s


def populate_variables():
    keys = ascii_uppercase
    variables = {}
    for letter in keys:
        variables[letter] = 0
    return variables


def find_jump_locations(program: list):
    jumps = {}
    for i in range(len(program)):
        line = program[i]
        command = line.split(' ')
        commandtype = command[0]
        # Jump location definition
        if isinstance(commandtype, str) and commandtype[-1] == ":":
            jump_instance = commandtype[:-1]
            jump_index = i
            jumps[jump_instance] = jump_index
    return jumps


def run(program: list):
    variables = populate_variables()
    jump_location_indexes = find_jump_locations(program)
    output = []
    i = 0
    while i < len(program):
        line = program[i]
        command = line.split(' ')
        commandtype = command[0]
        if commandtype == "MOV":  # Assigns value of int(X) to the variable
            target = command[1]
            value = maybe_int(command[2])
            if isinstance(value, int):
                variables[target] = value
            else:
                variables[target] = variables[value]

        if commandtype == "PRINT":  # Prints assigned variable to the output list
            print_value = maybe_int(command[1])
            if isinstance(print_value, int):
                output.append(print_value)
            else:
                output.append(variables[command[1]])

        if commandtype == "ADD":  # Addition X + Yint()int()
            append_variable = command[1]
            append_value = maybe_int(command[2])
            if not isinstance(append_value, int):
                append_value = variables[append_value]
            variables[append_variable] += append_value

        if commandtype == "SUB":  # Subtraction X - Y
            minuend = command[1]
            subtrahend = maybe_int(command[2])
            if isinstance(subtrahend, int):
                variables[minuend] -= subtrahend
            else:
                variables[minuend] -= variables[subtrahend]

        if commandtype == "MUL":
            factor_one = maybe_int(command[1])
            factor_two = maybe_int(command[2])
            if not isinstance(factor_one, int):
                factor_one = variables[factor_one]
            if not isinstance(factor_two, int):
                factor_two = variables[factor_two]
            product = factor_one * factor_two
            variables[command[1]] = product

        if commandtype == "JUMP":
            jump_instance = command[1]
            i = jump_location_indexes[jump_instance]
            continue

        if commandtype == "IF":
            variable_one = maybe_int(command[1])
            variable_two = maybe_int(command[3])
            if not isinstance(variable_one, int):
                variable_one = variables[variable_one]
            if not isinstance(variable_two, int):
                variable_two = variables[variable_two]

            comparison = command[2]
            jump_instance = command[5]
            if comparison == ">=" and variable_one >= variable_two:
                i = jump_location_indexes[jump_instance]
                continue
            elif comparison == ">" and variable_one > variable_two:
                i = jump_location_indexes[jump_instance]
                continue
            elif comparison == "<=" and variable_one <= variable_two:
                i = jump_location_indexes[jump_instance]
                continue
            elif comparison == "<" and variable_one < variable_two:
                i = jump_location_indexes[jump_instance]
                continue
            elif comparison == "==" and variable_one == variable_two:
                i = jump_location_indexes[jump_instance]
                continue
            elif comparison == "!=" and variable_one != variable_two:
                i = jump_location_indexes[jump_instance]
            else:
                pass

        if commandtype == "END":
            break

        i += 1

    return output


def main():

    while True:
        program = []
        command_input = input(
            "Type in a command (strict syntax)\nRead README.md for a list of commands and syntax\n  * Type EXIT to exit CLI.\n  * Type RUN to run program\nEnter: ")
        if command_input == "EXIT":
            print("Goodbye!")
            break
        elif command_input == "RUN":
            run(program)
        else:
            program.append(command_input)


if __name__ == "__main__":
    
    main()
