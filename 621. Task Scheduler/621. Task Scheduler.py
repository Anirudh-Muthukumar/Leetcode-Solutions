class Solution:
    def leastInterval(self, tasks, n):
        
        mp = [0] * 26
        
        for task in tasks:
            mp[ord(task) - ord('A')] += 1
        
        mp.sort(reverse = True)  # 26log(26)
        
        max_val = mp[0] - 1
        idle_slots = max_val * n
        
        for i in range(1, 26): # first task is already accounted
            idle_slots -= min(max_val, mp[i])
        
        
        if idle_slots > 0:
            return idle_slots + len(tasks)
        
        return len(tasks)
            