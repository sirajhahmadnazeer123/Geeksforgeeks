#User function Template for python3
from itertools import permutations
class Solution:
    def permutation(self,S):
        s = sorted(''.join(p) for p in permutations(S))
        result=list(s)
        return result
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends