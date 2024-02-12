#User function Template for python3
class Solution:
    def sequence(self, n):
        mod=1000000007
        res = 0
        start = 1
        for i in range(1 , n+1 ):
            ans = 1
            for _ in range (i):
                ans = ( ans * start )%mod
                start+=1
            res = ( res + ans ) % mod
        
        return res % mod
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends