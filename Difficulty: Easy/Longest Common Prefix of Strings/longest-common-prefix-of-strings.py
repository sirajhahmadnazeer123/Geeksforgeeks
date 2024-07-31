#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        arr.sort()
        s=len(arr[0])
        d=[]
        while(s!=0):
            c=1
            a=arr[0]
            for i in range(1,len(arr)):
                w=arr[i]
                if w[:s]==a[:s]:
                    c+=1
            if c==len(arr):
                d.append(a[:s])
            s-=1
        return -1 if len(d) == 0 else max(d)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends