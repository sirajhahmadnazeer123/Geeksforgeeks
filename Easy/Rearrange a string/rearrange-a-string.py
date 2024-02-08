#User function Template for python3

class Solution:
    def arrangeString(self, s):
        # code here
        if len(s)==1:
            return s[0]
        a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d=[]
        c=0
        for i in s:
            if i in a:
                d.append(i)
            else:
                c+=int(i)
        d.sort()
        d.append(str(c))
        return "".join(d)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends