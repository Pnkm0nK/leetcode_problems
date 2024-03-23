answer = True
sequence = "(("
def isValid(s):
    parentheses_pairs = {"(": ")", "[": "]", "{": "}"}
    parentheses_stack = []

    for parentheses in s:
        if parentheses in parentheses_pairs.keys():  # add opening parentheses to stack
            parentheses_stack.append(parentheses)
        # check if at least one parentheses is opened and it matches the closing one
        elif (len(parentheses_stack) != 0 and
              parentheses_pairs[parentheses_stack.pop()] == parentheses):
            continue
        else:
            return False

    if len(parentheses_stack) != 0:
        return False
    return True

print(isValid(sequence))

