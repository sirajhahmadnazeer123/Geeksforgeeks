#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,m, r, c): 
        # code here 
        sp=[]
        l, r, t, b = 0, c - 1, 0, r - 1
        while(t<=b and l<=r):
            for i in range(l,r+1):
                sp.append(m[t][i])
            t+=1
            for i in range(t,b+1):
                sp.append(m[i][r])
            r-=1
            if t <= b:
                for i in range(r, l - 1, -1):
                    sp.append(m[b][i])
                b -= 1 
            if l<=r:
                for i in range(b,t-1,-1):
                    sp.append(m[i][l])
                l+=1
        return sp
                    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends