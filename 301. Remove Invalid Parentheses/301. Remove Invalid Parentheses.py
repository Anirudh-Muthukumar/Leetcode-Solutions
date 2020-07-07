class Solution:
    def removeInvalidParentheses(self, s) :
        
        def validParentheses(state):
            stack = []
            for ch in state:
                if ch=='(':
                    stack.append(ch)
                elif ch==')':
                    if len(stack)>0 and stack[-1]=='(':
                        stack.pop() 
                    else:
                        return False
            return len(stack)==0

        q = [(s, 0)]
        visited = set([s])
        min_dist = float('inf')
        res = []
        while q:
            state, dist = q.pop(0) 

            if validParentheses(state):
                if dist <= min_dist:
                    res.append(state)
                    min_dist = dist
                else:
                    break

            for i in range(len(state)):
                new_state = state[:i]+state[i+1:]
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, dist+1))
        
        return res