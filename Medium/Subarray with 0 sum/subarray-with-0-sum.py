#User function Template for python3

class Solution:
    
  
    def subArrayExists(self,a,n):
        su=0
        d=set()
        for i in range(n):
            su+=a[i]
            if su==0 or su in d:
                return True
            d.add(su)
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends