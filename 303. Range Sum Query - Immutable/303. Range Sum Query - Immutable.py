class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [None] * (2*n)
    
    def build(self, A):
        n = self.n
        # fill in the leaf nodes first
        for i in range(n):
            self.tree[i+n] = A[i]
        
        # Fill parents from N-1 to 1
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def query(self, l, r): # range [l, r)
        res = 0
        l += self.n
        r += self.n
        
        while l<r:
            if l&1:
                res += self.tree[l]
                l += 1
            if r&1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        
        return res

class NumArray:

    def __init__(self, nums):
        self.segTree = SegmentTree(len(nums))
        self.segTree.build(nums)
        

    def sumRange(self, i: int, j: int) -> int:
        return self.segTree.query(i, j+1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)