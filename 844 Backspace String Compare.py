class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        
        for ch in S:
            if ch!='#':
                stack1.append(ch)
            else:
                if len(stack1)==0:
                    continue
                stack1.pop(-1) # pop the last character
        
        for ch in T:
            if ch!='#':
                stack2.append(ch)
            else:
                if len(stack2)==0:
                    continue
                stack2.pop(-1) # pop the last character
        
        return stack1==stack2