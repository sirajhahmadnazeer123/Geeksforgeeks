#User function template for Python 3
from collections import Counter
class Solution:
    def areKAnagrams(self, str1, str2, k):
        # code here
        if len(str1) != len(str2):
            return False
        
        c1, c2 = Counter(str1), Counter(str2)

        for i in range(len(str1)):
                    
            if c2[str1[i]] <= 0:
                k -= 1
            
            elif c2[str1[i]] > 0:
                c2[str1[i]] -= 1             


        return k >= 0
#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# } Driver Code Ends