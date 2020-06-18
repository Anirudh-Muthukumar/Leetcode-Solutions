class NumArray:

    def __init__(self, A):
        self.n = len(A)
        self.tree = [None] * (2*self.n)
        self.build(A)
        
        
    def build(self, A):
        for i in range(self.n):
            self.tree[i+self.n] = A[i]

        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
        

    def update(self, i, val):
        p = i + self.n
        self.tree[p] = val
        
        while p>1:
            self.tree[p>>1] = self.tree[p] + self.tree[p^1]
            p >>= 1

        

    def sumRange(self, i, j):
        res, l, r = 0, i+self.n, j+1+self.n
        
        while l<r:
            if l&1:
                res += self.tree[l]
                l+=1
            if r&1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)