#User function Template for python3
import math
class Solution:
    def findRank(self, s):
        #Code here
        n=len(s)
        ans=1
        for i in range(n):
            cnt=0
            for j in range(i+1,n):
                if s[i]>s[j]:
                    cnt+=1
            if cnt:
                ans+=(math.factorial(n-i-1))*cnt
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	str = input().strip()
    	obj = Solution()
    	ans = obj.findRank(str)
    	print(ans)
# } Driver Code Ends