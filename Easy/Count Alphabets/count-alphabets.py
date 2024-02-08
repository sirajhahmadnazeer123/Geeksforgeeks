#User function Template for python3

class Solution:

    def Count(self, S):
        # code here
            f="abcdefghijklmnopqrstuvwxyz"
            c=0
            for i in S.lower():
                if i in f:
                    c+=1
            return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.Count(S))
# } Driver Code Ends