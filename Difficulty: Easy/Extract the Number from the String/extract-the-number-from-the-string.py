import re
class Solution:
    def ExtractNumber(self,sentence):
        #code here
        temp = re.findall(r'\d+', sentence)
        res = list(map(str, temp))
        d=[]
        for i in res:
            if '9' not in i:
                d.append(int(i))
        if len(d)!=0:
           return max(d)
        return -1
#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends