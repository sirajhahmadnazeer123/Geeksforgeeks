#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
    # Your code goes here
        if 1 in arr:
            return arr.index(1)
        else:
            return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends