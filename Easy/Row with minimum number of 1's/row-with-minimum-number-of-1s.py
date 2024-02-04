#User function Template for python3

class Solution:
    def minRow(self,N,M,A):
        #code here
        s=[]
        for i in A:
            s.append(i.count(1))
        for i in s:
            if i==min(s):
                return s.index(i)+1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends