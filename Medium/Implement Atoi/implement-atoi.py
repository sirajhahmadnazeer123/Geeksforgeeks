#User function template for Python

#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        s=""
        if string[0]=="-":
            s=string[0]
            string=string[1:]
        n="abcdefghijklmnopqrstuvwxyz-"
        string.lower()
        for i in n:
            if i in string:
                return -1
        if int(string)*1==0:
            return 0
        if len(s)==0:
            return int(string)
        return s+str((int(string)))

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends