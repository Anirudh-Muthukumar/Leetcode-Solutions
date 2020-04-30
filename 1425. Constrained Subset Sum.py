import collections

class Monoqueue(collections.deque):
    def enqueue(self, val):
        count = 1
        while self and self[-1][0] < val:
            count += self.pop()[1]
        self.append([val, count])

    def dequeue(self):
        ans = self.max()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        return ans

    def max(self):
        return self[0][0] if self else 0



def constrainedSubsetSum(A, K):
    monoq = Monoqueue()
    ans = max(A)
    for i, x in enumerate(A):
        monoq.enqueue(x + max(0, monoq.max()))
        if i >= K:
            ans = max(ans, monoq.dequeue())
        print(i, x, monoq)
    return max(ans, monoq.dequeue())


nums = [10,-2,-10,-5,20]
k = 2
print(constrainedSubsetSum(nums, k))