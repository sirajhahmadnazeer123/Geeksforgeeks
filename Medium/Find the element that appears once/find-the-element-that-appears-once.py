#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        dp={}
        for i in A:
            if i in dp:
                dp[i]+=1
            else:
                dp[i]=1
        for key,val in dp.items():
            if val==1:
                return key


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends