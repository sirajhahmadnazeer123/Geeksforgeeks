#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        # Code here
        n = len(s)
        ans = []
        
        for i in range(1<<n):
            v = []
            for j in range(n):
                if ((1<<j)&i):
                    v.append(s[j])
            k = "".join(v)
            if k:
                ans.append(k)
            
        ans.sort()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends