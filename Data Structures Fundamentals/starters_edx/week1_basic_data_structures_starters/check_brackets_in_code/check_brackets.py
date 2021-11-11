# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                prev = opening_brackets_stack.pop()
                if prev.Match(next):
                    pass
                else:
                    opening_brackets_stack.append(Bracket(next, i))
                    break
            else:
                opening_brackets_stack.append(Bracket(next, i))
                break

    # Printing answer, write your code here
    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        prev = opening_brackets_stack.pop()
        print(prev.position + 1)
