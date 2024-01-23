mod=1000000007
class Solution:
    def nthFibonacci(self, n : int) -> int:
        a,b=0,1
        if n==1:
            return a
        if n==2:
            return b
        for i in range(3,n+2):
            a,b=b%1000000007,(a+b)%1000000007
        return b
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends