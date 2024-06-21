#User function Template for python3


class Solution:
    def compareFrac (self, str):
        s=[]
        for i in str.split(","):
            s.append(i)
        if eval(s[0])>eval(s[1]):
            return s[0]
        elif eval(s[1])>eval(s[0]):
            v=s[1]
            return v[1:]
        else:
            return "equal"
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends