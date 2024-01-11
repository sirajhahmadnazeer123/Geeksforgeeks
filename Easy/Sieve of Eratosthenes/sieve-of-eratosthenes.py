#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, n):
    	#code here 
    	d=[1]*(n+1)
    	d[0]=0
    	d[1]=0
    	for i in range(2,int(n**0.5)+1):
    	    if d[i]==1:
    	        for j in range(i*i,n+1,i):
    	            d[j]=0
    	f=[]
    	for i in range(0,len(d)):
    	    if d[i]==1:
    	        f.append(i)
    	return f
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends