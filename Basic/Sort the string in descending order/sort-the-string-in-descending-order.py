#User function Template for python3
class Solution:
    def ReverseSort(self, str): 
        # code here
        str="".join(sorted(str))
        return str[::-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.ReverseSort(s))
# } Driver Code Ends