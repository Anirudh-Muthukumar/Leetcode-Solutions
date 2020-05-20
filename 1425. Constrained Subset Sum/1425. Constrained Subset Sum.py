import collections

class Monoqueue(collections.deque):
    def enqueue(self, new_val):
        count = 1   
        while self and self[-1][0] < new_val: # make sure first element is the largest 
            count += self.pop()[1]
        self.append([new_val, count])
    
    def dequeue(self):
        ans = self.max()
        self[0][1] -= 1    # decrement its count
        if self[0][1] <= 0:
            self.popleft()
        return ans
    
    def max(self):
        if self:
            return self[0][0]
        return 0


def constrainedSubsetSum(self, A, k):
    queue = Monoqueue()
    ans = max(A)
    
    for i, x in enumerate(A):
        queue.enqueue(x + max(0, queue.max()))
        if i>=k :   # update window
            ans = max(ans, queue.dequeue())
    
    return max(ans, queue.dequeue())
        


nums = [10,-2,-10,-5,20]
k = 2
print(constrainedSubsetSum(nums, k))