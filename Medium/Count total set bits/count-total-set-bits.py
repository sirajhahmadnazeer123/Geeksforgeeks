#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        if n<=1:
            return n
        x=math.floor(math.log2(n))
        return x*(1<<(x-1))+(n-(1<<x)+1)+self.countSetBits(n-(1<<x))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends