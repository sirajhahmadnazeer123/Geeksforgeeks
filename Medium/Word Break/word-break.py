#User function Template for python3

class Solution:
       # Complete this function
    def solve(self,s,dictionary):
        if not s:
            return True
        for i in dictionary:
            if s.startswith(i) and self.solve(s[len(i):],dictionary):
                return True
        return False
    def wordBreak(self, n, s, dictionary):
        return self.solve(s,dictionary)
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends