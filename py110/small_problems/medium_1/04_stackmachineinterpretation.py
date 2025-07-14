"""
Problem: Write a function that implements a miniature stack-and-register-based programming 
language that has the following commands (also called operations or tokens):

    n: Place an integer value, n, in the register. Do not modify the stack.
    PUSH : Push the current register value onto the stack. Leave the value in the register.
    ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
    SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
    MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
    DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
    REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
    POP : Remove the topmost item from the stack and place it in the register.
    PRINT : Print the register value.

    input: 
        - always: upper case string
        - often: upper case string + an integer or a series of both
        - never: just an integer
    output: 
        - often: an integer
        - sometimes: empty response
        - never: a string

Example: '5 PRINT PUSH 3 PRINT ADD PRINT' ==> 5 /n 3 /n 8

Data Structure: 2 lists: stack and actions, which is handling the inputs

Algorithm: 
    
  
    - def minilang(input_string):   
            - purpose: handle the input string and run the program
            - initialize register as 0
            - initialize stack as []
            - actions = input_string.split()
            - for action in actions:
                try: 
                    register = int(action)
                except ValueError:
                    action = action.upper()

                register, stack = choose_action(register, stack, action)

        - choose_action(register, stack, action): 
            match action:
                - case 'ADD':
                    return ADD(register, stack)
                - case 'SUB':
                    return SUB(register, stack)
                - case 'MULT':
                    return MULT(register, stack)
                - case 'DIV':
                    return DIV(reguster, stack)
                - case 'REMAINDER':
                    return REMAINDER(register, stack)
                - case 'PUSH':
                    return PUSH(register, stack)
                - case 'POP':
                    return POP(register, stack)
                - case 'PRINT':
                    return PRINT(register, stack)

        - PUSH(register, stack): 
            - stack.append(register)
            - return register, stack
        - ADD(register, stack): 
            - popped_value = stack.pop(value)
            - register = register + popped_value
            - returns register, stack
        - SUB(register, stack): 
            - popped_value = stack.pop(value)
            - register = register - popped_value
            - returns register, stack
        - MULT(register, stack):
            - popped_value = stack.pop(value)
            - register = register * popped_value 
            - returns register, stack
        - DIV(register, stack): 
            - popped_value = stack.pop(value)
            - register = register // popped_value 
            - returns register, stack
        - REMAINDER(register, stack):
            - popped_value = stack.pop(value)
            - register = register % popped_value
            - returns register, stack
        - POP(register, stack):
            - popped_value = stack.pop()
            - register = popped_value
            - return register, stack
        - PRINT(register, stack):
            - print(f'{register}')
            - return register, stack
            

"""

def minilang(input_string):
    """Purpose: handle the input string and run the program"""
    register = 0
    stack = []
    actions = input_string.split()
    for action in actions:
        try: 
            register = int(action)
        except ValueError:
            action = action.upper()
            register, stack = choose_action(register, stack, action)

def choose_action(register, stack, action): 
    """ Initiates correct action signifed by the ALL CAPS string"""
    match action:
        case 'ADD':
            return ADD(register, stack)
        case 'SUB':
            return SUB(register, stack)
        case 'MULT':
            return MULT(register, stack)
        case 'DIV':
            return DIV(register, stack)
        case 'REMAINDER':
            return REMAINDER(register, stack)
        case 'PUSH':
            return PUSH(register, stack)
        case 'POP':
            return POP(register, stack)
        case 'PRINT':
            return PRINT(register, stack)

def PUSH(register, stack): 
    stack.append(register)
    return register, stack

def ADD(register, stack): 
    popped_value = stack.pop()
    register = register + popped_value
    return register, stack

def SUB(register, stack): 
    popped_value = stack.pop()
    register = register - popped_value
    return register, stack
    
def MULT(register, stack):
    popped_value = stack.pop()
    register = register * popped_value 
    return register, stack

def DIV(register, stack): 
    popped_value = stack.pop()
    register = register // popped_value 
    return register, stack

def REMAINDER(register, stack):
    popped_value = stack.pop()
    register = register % popped_value
    return register, stack

def POP(register, stack):
    popped_value = stack.pop()
    register = popped_value
    return register, stack

def PRINT(register, stack):
    print(f'{register}')
    return register, stack



minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)