#User function Template for python3

class Solution:
	def PowMod(self, a, b,mod):
		# Code here
		ans = 1
        while b:
            if b & 1:
                b = b - 1
                ans = ((ans % mod)*(a % mod))%mod
            else:
                b = b // 2
                a = ((a% mod)*(a % mod))%mod
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends