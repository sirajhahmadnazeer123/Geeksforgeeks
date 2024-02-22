#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		p=1
		s=1
		ma=arr[0]
		for i in range(n):
		    if p==0:
		        p=1
		    if s==0:
		        s=1
		    p*=arr[i]
		    s*=arr[n-1-i]
		    ma=max(ma,max(p,s))
		return ma

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends