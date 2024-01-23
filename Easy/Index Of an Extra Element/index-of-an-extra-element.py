class Solution:
    def findExtra(self,a,b,n):
        s1=set(a)
        s2=set(b)
        missing=list(s1.difference(s2))
        return a.index(missing[0])
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends