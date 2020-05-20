'''
Time Complexity : O(m+n)
Space Complexity : O(1)
'''

def oneEditDistance(X, Y):

    m, n = len(X), len(Y)

    # stores the edit distance between two strings
    editDistance = 0 

    # If length of two strings differ by more than 1
    if abs(m-n)>1:
        return False 
    
    i, j = 0, 0

    while i<m and j<n:

        # if characters are same just increment pointers
        if X[i]==Y[j]:
            i+=1
            j+=1
        
        # if characters are not equal
        else:
            
            # Break whenever the difference is more than 1 
            if editDistance==1:
                return False 

            editDistance += 1

            # deletion if source is bigger than target
            if m>n:
                i+=1

            # insertion if source is smaller than target
            elif m<n:
                j+=1

            # substitution if rest of the string length is same
            else:
                i+=1
                j+=1

    # add remainder of both the strings if pointers have not reached the end
    editDistance += (m-i)
    editDistance += (n-j) 

    return editDistance==1

if __name__ == '__main__':
    
    X = "geetcode"
    Y = "leetcode"

    print(oneEditDistance(X, Y))