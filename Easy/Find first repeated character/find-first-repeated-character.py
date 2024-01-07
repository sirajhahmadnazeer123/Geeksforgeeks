#User function Template for python3

def nonrepeatingCharacter(self,s):
        #code here
        g={}
        c=[]
        for i in s:
            if i in g:
                g[i]+=1
            else:
                g[i]=1
        for i in g:
            if g[i]==1:
                c.append(i)
        for i in s:
            if g[i]==1:
                return i
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
