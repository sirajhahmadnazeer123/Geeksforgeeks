#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items(), key=lambda x:x[1])
        s=d[-2]
        return s[0]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends