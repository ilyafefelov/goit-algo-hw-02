from collections import deque


def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Parameters:
    s (str): The string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove spaces
    s = "".join(filter(str.isalnum, s)).lower()

    char_deque = deque(s)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Loop until 'q' is pressed to quit
while True:
    input_str = input(
        "Enter a string to check if it is a palindrome (press 'q' to quit): "
    ).strip()

    if input_str == "q":
        break

    if is_palindrome(input_str):
        print(f"'{input_str}' is a palindrome.")
    else:
        print(f"'{input_str}' is not a palindrome.")
