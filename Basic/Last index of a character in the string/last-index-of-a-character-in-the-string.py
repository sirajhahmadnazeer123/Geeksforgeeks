#User function Template for python3

class Solution:
    def LastIndex(self, s, p):
        # code here
        j=-1
        for i in range(0,len(s)):
            if s[i]==p:
                j=i
        return j
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        p = input().strip()[0]
        
        ob=Solution()
        print(ob.LastIndex(s, p))
# } Driver Code Ends