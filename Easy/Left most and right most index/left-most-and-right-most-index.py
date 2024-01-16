#User function Template for python3

class Solution:
    def indexes(self, v, x):
        j=[]
        s=[]
        # Your code goes here
        for i in range(0,len(v)):
            if v[i]==x:
                j.append(i)
        if len(j)==0:
            s.append(-1)
            s.append(-1)
        else:
            s.append(min(j))
            s.append(max(j))
        return s
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends