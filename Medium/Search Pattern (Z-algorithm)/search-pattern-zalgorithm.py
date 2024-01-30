#User function Template for python3

class Solution:
   def search(self, patt, s):
       l1=[]
       t=len(patt)
       for i in range(len(s)-len(patt)+1):
           if s[i:t+i]==patt:
               l1.append(i+1)
       return l1
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print("-1", end = " ")
        else:
            for value in ans:
                print(value,end = ' ')
        print()
# } Driver Code Ends