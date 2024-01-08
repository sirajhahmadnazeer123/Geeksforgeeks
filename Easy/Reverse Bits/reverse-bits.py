#User function Template for python3

class Solution:
    def reversedBits(self, X):
        # Convert X to a 32-bit binary string
        binary_str = format(X, "032b")
        
        # Reverse the binary string
        reversed_binary_str = binary_str[::-1]
        
        # Convert the reversed binary string back to an integer
        reversed_integer = int(reversed_binary_str, 2)
        
        # Convert the reversed integer back to a 32-bit binary string
        return reversed_integer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends