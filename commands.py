# Commands for the main program to run
def maybe_int(input): #if input is int > output = int, otherwise unchanged
    
    try:
        return int(input)
    except:
        return input

def print_value(variables:dict, key:str, value:int, output:int):
    
    