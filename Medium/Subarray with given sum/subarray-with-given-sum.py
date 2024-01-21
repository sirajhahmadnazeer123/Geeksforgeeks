#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
         i,j=1,0
         curr_sum=arr[0]
         while curr_sum!=s:
            if curr_sum<s:
                if i==n:
                    return [-1]
                curr_sum+=arr[i]
                i+=1
            else:# curr_sum>s:
                curr_sum-=arr[j]
                j+=1
         return [j+1,i] if j!=i else [-1]
               


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends