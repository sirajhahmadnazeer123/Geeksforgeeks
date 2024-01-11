#User function Template for python3

class Solution:        
    def primeRange(self,m,n):
        #code here
        s=1000001
        d=[1]*(n+1)
        d[0]=0
        d[1]=0
        for i in range(2,int(n**0.5)+1):
            if d[i]==1:
                for j in range(i*i,n+1,i):
                    d[j]=0
        s=[]
        for i in range(m,n+1):
            if d[i]==1:
                s.append(i)
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends