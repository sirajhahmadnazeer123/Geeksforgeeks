#Function should return a list/array containing the required words

''' The function returns a  list of strings 
present in the dictionary which matches
the string pattern.
You are required to complete this method '''

def findSpecificPattern(Dict, pattern):
    #Code here
    p=[]
    f=[]
    c=[]
    for i in Dict:
        d=[]
        for j in i:
            d.append(i.index(j))
        p.append(d)
    for j in pattern:
        f.append(pattern.index(j))
    for i in range(len(p)):
        if p[i]==f:
            c.append(Dict[i])
    return c


#{ 
 # Driver Code Starts
#function goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        string = input().strip()
        res = findSpecificPattern(arr, string)
        for i in res:
            print(i, end=" ")
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends