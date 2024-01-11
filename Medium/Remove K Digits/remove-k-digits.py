#User function Template for python3

class Solution:

    def removeKdigits(self, s, k):
        stack = []

        for digit in s:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        result = ''.join(stack[:len(stack)-k]).lstrip('0') or '0'
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends