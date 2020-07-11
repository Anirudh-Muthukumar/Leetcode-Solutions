import bisect

class MedianFinder :

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
            

    def addNum(self, num):
        index = bisect.bisect(self.data, num)
        self.data.insert(index, num)

    def findMedian(self):
        n = len(self.data)
        if n&1:
            return self.data[n>>1]
        return (self.data[n>>1] + self.data[(n>>1)-1]) * 0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()