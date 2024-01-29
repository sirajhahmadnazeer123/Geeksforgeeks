#User function Template for python3

class Solution:

    def findpos(self, n):
        # code here
        res, length = 0, len(n)
        
        for i in range(length-1, -1, -1):
            power = length-i-1
            if n[i] == "7":
                power += 1
            
            res += 2**power
            
        return res
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = input()

        solObj = Solution()

        ans = solObj.findpos(n)

        print(ans)
# } Driver Code Ends