class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        q = set([n])
        res = 0
        
        while q:
            res += 1
            temp = set()
            for x in q:
                for sq in squares:
                    if x==sq:
                        return res
                    elif sq > x:
                        break
                    temp.add(x-sq)
            q = temp
        
        return res