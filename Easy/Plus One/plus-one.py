#User function Template for python3
class Solution:
    def increment(self, arr, N):
        # code here 
        x = ''.join(map(str, arr))
        y=int(x)+1
        result = list(map(int, str(y)))
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends