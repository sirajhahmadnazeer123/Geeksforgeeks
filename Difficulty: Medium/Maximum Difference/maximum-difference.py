class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        ls = [0] * n
        rs = [0] * n
        stack = []

        # Calculate left smaller elements
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                ls[i] = stack[-1]
            else:
                ls[i] = 0
            stack.append(arr[i])

        stack.clear()  # Clear stack to reuse for right smaller elements

        # Calculate right smaller elements
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                rs[i] = stack[-1]
            else:
                rs[i] = 0
            stack.append(arr[i])

        # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(ls[i] - rs[i]))

        return max_diff

            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends