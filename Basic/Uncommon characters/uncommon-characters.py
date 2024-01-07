#User function Template for python3

class Solution:
    def UncommonChars(self,a, b):
        #code here
        g=""
        for i in a:
            if i not in b:
                if i not in g:
                    g+=i
        for i in b:
            if i not in a:
                if i not in g:
                    g+=i
        g="".join(sorted(g))
        return g if len(g)!=0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends