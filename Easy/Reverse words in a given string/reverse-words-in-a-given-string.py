# User function Template for python3

# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        f=len(S)
        j=""
        d=S[::-1]
        
        for i in d.split('.'):
            j+=i[::-1]
            j+='.'
        return j[0:f]
        

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends