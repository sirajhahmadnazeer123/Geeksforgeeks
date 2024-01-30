#User function Template for python3

class Solution:
    def ExcelColumn(self, columnNumber):
        #return required string
        #code here
        ans=""
        while(columnNumber>0):
            c=chr(ord('A')+(columnNumber-1)%26)
            ans=c+ans
            columnNumber=(columnNumber-1)//26            
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends