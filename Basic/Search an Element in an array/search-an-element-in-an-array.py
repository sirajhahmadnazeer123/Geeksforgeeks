#User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        s=[]
        for i in arr:
            if i==X:
                s.append(arr.index(i))
        if len(s)==0:
            return -1
        else:
            return s[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            
            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            ob=Solution()
            print(ob.search(A,N,x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends