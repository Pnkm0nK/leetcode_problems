import math
def solveRPN(tokens):
    valid_operators = ['+', '-', '*', '/']
    number_stack = []
    for char in tokens:
        if char not in valid_operators:
            number_stack.append(int(char))
        else:
            second_argument = number_stack.pop()
            first_argument = number_stack.pop()
            if char == '+':
                number_stack.append(first_argument + second_argument)
            elif char == '-':
                number_stack.append(first_argument - second_argument)
            elif char == '/':
                number_stack.append(int(first_argument / second_argument))
            elif char == '*':
                number_stack.append(first_argument * second_argument)
    return number_stack[0]


expression = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(solveRPN(expression))