#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        g={}
        for i in s:
            if i in g:
                g[i]+=1
                if g[i]==2:
                    return i
            else:
                    g[i]=1
        return -1


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