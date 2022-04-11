# Fenput

A <i>very</i> rudimentary progrmaming language

## Plan

Primarily an assignment work for the Helsinki University Python MOOC of 2022, found <a href="https://programming-22.mooc.fi/part-7/6-more-features">here</a>. The purpose of the language is to be capable of basic functions like addition, subtraction, and multiplication using a predefined list of commands. The program will be completed in python, with a web interface in the long term plans. First thing to do is to do a blueprint of the necessary functions and how to write them efficiently. Then I need to actually complete the program, starting with the simplest commands and working my way up.

## Commands

The commands are as listed:

<ul>
  <li>PRINT [value]</li>
  <li>MOV [variable] [value]</li>
  <li>ADD [variable] [value]</li>
  <li>SUB [variable] [value]</li>
  <li>MUL [variable] [value]</li>
  <li>[location:]</li>
  <li>JUMP [location]</li>
  <li>IF [condition] JUMP [location]</li>
  <li>END</li>
</ul>

### Commands legend

Legend for the list of commands:

<ul>
  <li>[value] : value assigned to a variable</li>
  <li>[variable] : A-Z, default 0</li>
  <li>[location] : jump location initialization on input location</li>
  <li>[condition] : [value][comparison][value] (_list of comparisons available below_)</li>
  <ul>
    <li>== : AND</li>
    <li>!= : NAND</li>
    <li>< : less than</li>
    <li>> : more than</li>
    <li><= : less than or equals to</li>
    <li>>= : more than or equals to</li>
  </ul>
</ul>

### Commands explained

#### PRINT [value] 
Outputs the _value_ of a variable

#### MOV [variable] [value]
Assigns an input value to a stored variable by name

#### ADD [variable] [value]
Sum of the value of the variable with the input value

#### SUB [variable] [value]
Subtracts the value of the variable with the input value

#### MUL [variable] [value]
Multiplies the value of the variable with the input value

#### "location:": 
Inputs a jump point for the program (only lowercase, **notice the colon**)

#### JUMP [LOCATION]
Jumps to a location that was input, allowing for rudimentary loops

#### IF [condition] JUMP [location]

If the condition is true, then the program jumps to the location specified in the program

#### END

Ends the program


#### Currently relevant sample program
```
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
```
