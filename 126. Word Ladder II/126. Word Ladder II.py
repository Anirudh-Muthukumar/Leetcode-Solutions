import collections

class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.n = 0
        self.res = []
        
    def findLadders(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or endWord not in wordList or not wordList:
            return []
        
        self.n = len(beginWord)
        
        for word in wordList:
            for i in range(self.n):
                self.graph[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = collections.deque([(beginWord, [beginWord])])  
        visited = set([beginWord])
        found = False
        
        while queue and not found:
            size = len(queue)
            localvisited = set()
            for _ in range(size):
                current_word, path = queue.popleft()
                for i in range(self.n):
                    intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                    for word in self.graph[intermediate_word]:
                        if word==endWord:
                            found = True
                            self.res += path + [endWord],
                        if word not in visited:
                            localvisited.add(word)
                            queue += (word, path + [word]),
            visited = visited.union(localvisited)
        
        return self.res