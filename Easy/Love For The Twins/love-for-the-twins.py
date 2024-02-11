class Solution:
    def getTwinCount(self, N , Arr):
        # code here 
        d={}
        for i in Arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in d:
            if d[i]>1:
                c+=d[i]//2
                
        return c+c


#{ 
 # Driver Code Starts

t = int (input ())
for _ in range (t):
    N=int(input())
    Arr=list(map(int,input().split()))
    
    ob = Solution()
    print(ob.getTwinCount(N,Arr))
# } Driver Code Ends