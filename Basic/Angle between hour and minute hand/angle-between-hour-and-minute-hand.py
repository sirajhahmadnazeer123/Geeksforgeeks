#User function Template for python3

class Solution:
    def getAngle(self, H , M):
        # code here
        angle = (abs( 0.5 * (60*H-11*M)))

        if angle > 180:

            return int(360-angle)

        else:

            return int(angle)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        H,M=map(int,input().split())
        
        ob = Solution()
        print(ob.getAngle(H,M))
# } Driver Code Ends