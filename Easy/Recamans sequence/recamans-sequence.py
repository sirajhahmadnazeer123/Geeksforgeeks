#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        d = [0] * n
        s = set()
        d[0] = 0
        for i in range(1, len(d)):
            prev = d[i-1]
            c = prev - i
            if c > 0 and c not in s:
                d[i] = c
            else:
                d[i] = prev + i
            s.add(d[i])
        return d


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends