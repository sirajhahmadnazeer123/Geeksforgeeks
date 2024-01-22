#User function Template for python3

class Solution:
    def countWords(self,l, n):
        #code here
        d={}
        c=0
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==2:
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
# } Driver Code Ends