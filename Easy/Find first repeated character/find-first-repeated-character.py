#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        p=[]
        for i in s:
            if i in p:
                return(i)
            else:
                p.append(i)
        return(-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends