import string

def maybe_int(input): #if input is int > output = int, otherwise unchanged
    
    try:
        return int(input)
    except:
        return input

def create_variables(): # fills a dictionary with letters A-Z as keys, 0 as init value
    
   variables = {}
   for letter in string.ascii_uppercase:
       variables[letter] = 0

def parse_file(program): # runs through the written program line by line
    
    variables = create_variables # creating the initial dictionary for the variables and their values
    i = 0
    output = []
    while i < len(program):
        line = program[i]
        print(line)
        command = line.split(' ') # splits each line of the program into an item in a list for indexing
        commandtype = command[0] # command type, e.g. PRINT, should always be found on  the first index
        # note: add error handling
        
        if commandtype == "PRINT":
            variable = maybe_int(command[1])
            print_output = variables[variable]
            output.append[variable]
        
        if commandtype == "MOV":
        
        i += 1


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