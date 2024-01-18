#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        x=[]
        for i in Str.split():
            x.append(i)
        z=""
        for i in range(0,len(x)):
            if i%2==0:
                z+=x[i]
                z+=" "
            else:
                z+=x[i][::-1]
                z+=" "
        return z[:-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends