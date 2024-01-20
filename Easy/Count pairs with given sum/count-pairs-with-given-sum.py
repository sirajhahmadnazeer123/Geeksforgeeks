#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        d = {}
        count = 0
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for num in arr:
            c = k - num

            if c in d:
                count += d[c]

            # Avoid counting the same pair twice
            if c== num:
                count -= 1

        # Divide by 2 as each pair is counted twice
        return count // 2
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends