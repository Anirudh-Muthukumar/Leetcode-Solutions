class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        q = set([beginWord])
        res = 0
        
        if endWord not in wordList:
            return 0
        
        visited = set([beginWord])
        while q:
            res+=1
            temp = set()
            for old_word in q:
                for i in range(len(old_word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = old_word[:i] + ch + old_word[i+1:]
                        if new_word == endWord:
                            return res+1
                        if new_word in wordList and new_word not in visited:
                            visited.add(new_word)
                            temp.add(new_word)
            q = temp
        
        return 0