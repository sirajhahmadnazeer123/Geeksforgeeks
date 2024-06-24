#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        if q==1:
            return 0
        if n>q:
            return q-1
        elif q>n:
            s=q-n
            s=n-s+1
            if(s<=0):
                return 0
            else:
                return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends