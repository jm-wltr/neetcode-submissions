# edge cases: 
# empty string
# only opening brackets
# only closing brackets
# early closing brackets

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            # Add opening brackets to stack
            if char in {'(', '[', '{'}:
                stack.append(mapping[char])

            # Match closing bracket to stack
            else:
                if not stack or stack.pop() != char:
                    return False

        return (len(stack) == 0)





