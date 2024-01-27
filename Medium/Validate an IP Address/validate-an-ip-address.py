def isValid(s):
    ls = s.split(".")
    if len(ls) != 4:
        return 0
    for i in ls:
        if not i or (i[0] == '0' and len(i) > 1):  
            return 0
        try:
            val = int(i)
            if val < 0 or val > 255:
                return 0
        except ValueError:
            return 0  
    return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends