def is_balanced(expression):
    """
    Checks if the given expression has balanced brackets.

    Args:
        expression (str): The expression to be checked.

    Returns:
        bool: True if the expression has balanced brackets, False otherwise.
    """
    stack = []
    opening_brackets = {'(': ')', '[': ']', '{': '}'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack and stack[-1] == closing_brackets[char]:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

while True:
    input_expr = input("Enter an expression to check for balanced brackets (press 'q' to quit): ").strip()
    if input_expr == 'q':
        break
    
    if is_balanced(input_expr):
        print(f"The expression '{input_expr}' is balanced.")
    else:
        print(f"The expression '{input_expr}' is not balanced.")
( 11 }