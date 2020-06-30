import bisect

class Solution:
    def insert(self, intervals, newInterval):
        n = len(intervals)

        ind = bisect.bisect_right(intervals, newInterval)
        intervals.insert(ind, newInterval)
            
        merged = []
        
        for i in range(n+1):
            if merged == [] or merged[-1][1] < intervals[i][0]:
                merged += intervals[i],
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        
        return merged