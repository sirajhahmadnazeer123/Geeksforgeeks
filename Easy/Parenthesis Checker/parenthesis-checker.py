#User function Template for python3

class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        stack = []
        opening_brackets = "{[("
        closing_brackets = "}])"

        for char in x:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or not self.is_matching(stack[-1], char):
                    return False
                stack.pop()

        return not stack

    def is_matching(self, open_char, close_char):
        return (open_char == '(' and close_char == ')') or \
               (open_char == '{' and close_char == '}') or \
               (open_char == '[' and close_char == ']')

        
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends