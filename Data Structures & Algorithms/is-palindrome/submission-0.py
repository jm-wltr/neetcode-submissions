class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        # strip non alphanumeric characters
        processed = ""
        for char in s:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                processed = processed + str(char)

        for i in range(len(processed)):
            if processed[-i - 1] != processed[i]:
                return False
            
        return True
        