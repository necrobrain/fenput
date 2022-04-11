import string

def maybe_int(input):
    
    try:
        return int(input)
    except:
        return input

def create_variables():
    
   variables = {}
   for letter in string.ascii_uppercase:
       variables[letter] = 0


def parse_file(program):
    
    variables = create_variables
    i = 0
    output = []
    while i < len(program):
        line = program[i]
        print(line)
        command = line.split(' ')
        commandtype = command[0]
        
        if commandtype == "PRINT":
            variable = int(command[1])
            print_output = variables[variable]
            output.append[variable]


def run(program):
    
    parsed_program = parse_file(program)

def main():
    
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

if __name__ == "__main__":
    
    main()