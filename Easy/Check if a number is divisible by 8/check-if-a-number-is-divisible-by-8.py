#User function Template for python3

class Solution:
    def DivisibleByEight(self,S):
        #code here
        s=str(S)
        if len(s)>=3:
            s=s[len(s)-3:]
            if int(s)%8==0:
                return 1
        if len(s)<=2:
            if int(s)%8==0:
                return 1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends