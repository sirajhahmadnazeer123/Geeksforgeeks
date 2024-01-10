#User function Template for python3

class Solution:
    def power (self, a, b):
        #complete the function here
        mod=10**9+7
        ans=1
        while(b):
            if(b&1):
                b=b-1
                ans=((ans%mod)*(a%mod))%mod
            else:
                b=b//2
                a=((a%mod)*(a%mod))%mod
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a, b = map(int,input().split())
        ob = Solution()
        print(ob.power(a, b))
# } Driver Code Ends