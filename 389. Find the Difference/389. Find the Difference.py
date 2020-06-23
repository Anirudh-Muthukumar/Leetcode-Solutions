class Solution:
    def findTheDifference(self, s, t):
        missing = 0
        for ch in s:
            missing ^= ord(ch)
        for ch in t:
            missing ^= ord(ch)
        return chr(missing)