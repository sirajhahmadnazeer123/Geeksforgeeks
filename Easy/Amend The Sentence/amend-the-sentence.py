#User function Template for python3

class Solution:

    def amendSentence(self, s):

        # code here
        a="ABCDEFGHIJKLMNOPQRSTUVWXYYZ"
        p=s[0]
        k=[]
        for i in range(1,len(s)):
            if s[i] not in a:
                p+=s[i]
            else:
                k.append(p.lower())
                p=s[i]
        k.append(p.lower())
        k=" ".join(k)
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.amendSentence(s))
        

# } Driver Code Ends