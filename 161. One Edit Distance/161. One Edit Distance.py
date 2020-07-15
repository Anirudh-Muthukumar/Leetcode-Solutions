'''
Time Complexity : O(m+n)
Space Complexity : O(1)
'''

class Solution:
    def isOneEditDistance(self, x, y):
        def linearSpace():
            m, n = len(x), len(y)
            first = [j for j in range(n+1)]
            
            for i in range(1, m+1):
                second = [0 for _ in range(n+1)]
                second[0] = i
                for j in range(1, n+1):
                    if x[i-1]==y[j-1]:
                        second[j] = first[j-1]
                    else:
                        second[j] = 1 + min(first[j], second[j-1], first[j-1])
                
                first = second[::]
                
            return first[n]==1
        
        def constantSpace():
            m, n = len(x), len(y)
            dist, i, j = 0, 0, 0

            while i<m and j<n:
                if x[i]==y[j]:
                    i+=1
                    j+=1
                else:
                    dist += 1

                    if dist>1:
                        return False 
                    
                    if (m-i)==(n-i): # replace 
                        i += 1
                        j += 1
                    elif (m-i) > (n-j): #insert
                        j+=1 
                    else: # delete
                        i+=1
            
            return dist==1
        
        return constantSpace()
        return linearSpace()
            

if __name__ == '__main__':
    soln = Solution()
    # X = 
    # X = "geetcode"
    # Y = "leetcode"
    print(soln.oneEditDistance('1203', '1213'))
#     print(oneEditDistance(X, Y))