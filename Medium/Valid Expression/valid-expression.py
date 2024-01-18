class Solution:
    def valid(self, s): 
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            elif stack and brackets[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return not stack

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        if ob.valid(s):
            print(1)
        else:
            print(0)
# } Driver Code Ends