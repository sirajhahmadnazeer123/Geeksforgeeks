#User function Template for python3
def maximumFrequency (S) : 
    #Complete the function
    res = {}
    L = S.split(" ")
    for i in L:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    ma = max(list(res.values()))
    mi = min(list(res.values()))
    if mi == ma:
        g = ""
        g += str(L[0])
        g += " "
        g += str(1)
        return g
    else:
        g = []
        for (k,v) in res.items():
            if v == ma:
                g.append(k)
        f = ""
        for i in L:
            if i in g:
                f = str(i)
                f += " "
                f += str(ma)
                break
            
        return f

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    S = input()
    
    print(maximumFrequency(S))




# } Driver Code Ends