#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
		# your code here
		c=""
		a="abcdefghijklmnopqrtuvwxyz"
		for i in s:
		    if i in a:
		        c+=i
		if c==c[::-1]:
		    return True
		return False
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		if ob.sentencePalindrome (s):
			print (1)
		else:
			print (0)
# } Driver Code Ends