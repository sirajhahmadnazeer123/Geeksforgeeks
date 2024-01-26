#User function Template for python3

class Solution:
    def findNth(self,N):
        #code here
        pos=1
        ans=0
        while(N>0):
            ans+=pos*(N%9)
            N//=9
            pos*=10
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends