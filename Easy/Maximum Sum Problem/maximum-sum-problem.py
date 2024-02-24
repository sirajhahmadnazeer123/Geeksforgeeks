#User function Template for python3

class Solution:
    def Taylor(self,n):
        if n>=(n//2)+(n//3)+(n//4):
            return n
        return self.Taylor(n//2)+self.Taylor(n//3)+self.Taylor(n//4)
    def maxSum(self, n): 
        # code here 
        return self.Taylor(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends