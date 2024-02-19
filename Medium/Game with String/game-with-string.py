#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        while k > 0:
            mx = max(d.values())
            if mx == 0:
                break
            for i in d:
                if d[i] == mx:
                    d[i] -= 1
                    k -= 1
                    if k==0:
                        break

        c=0
        for i in d:
            c+=pow(d[i],2)
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends