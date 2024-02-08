#User function Template for python3

class Solution:
    def karatsubaAlgo(self, A , B):
        # code here 
        c=int(A,2)
        d=int(B,2)
        return c*d

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B = map(str,input().split())
        
        ob = Solution()
        print(ob.karatsubaAlgo(A,B))
# } Driver Code Ends