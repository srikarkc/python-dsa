class Solution:
    def valid_parentheses(self, s):
        my_stack = []

        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for char in s:
            if char in closeToOpen:
                if my_stack and my_stack[-1] == closeToOpen[char]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(char)

        #return True if not my_stack else False
        return not my_stack
    