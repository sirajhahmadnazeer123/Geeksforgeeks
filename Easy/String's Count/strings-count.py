#User function Template for python3

class Solution:

      def countStr(self, n):
        
        res=0
        all_a=1
        b1=n
        c1=n
        res+=all_a+b1+c1
        if n>=2:
            b1_and_c1=n*(n-1)
            c2=n*(n-1)//2
            res+=b1_and_c1+c2
            
        # 1"b" and 2"c" case
        if n>=3:
            b1_and_c2=n*(n-1)*(n-2)//2
            res+=b1_and_c2
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends