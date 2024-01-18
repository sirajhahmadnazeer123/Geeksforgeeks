#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    x=""
    for i in S:
        x=i+x
    return x
        
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends