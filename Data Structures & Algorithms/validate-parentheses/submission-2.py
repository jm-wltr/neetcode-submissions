# edge cases: 
# empty string
# only opening brackets
# only closing brackets
# early closing brackets

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # Add opening brackets to stack
            if char in {'(', '[', '{'}:
                if char == '(':
                    stack.append(')')
                elif char == '[':
                    stack.append(']')
                else:
                    stack.append('}')

            # Match closing bracket to stack
            else:
                if len(stack) == 0 or stack.pop() != char:
                    return False
        return (len(stack) == 0)





