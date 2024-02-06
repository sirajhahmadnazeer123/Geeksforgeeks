#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        hp={}
        for i in words:
            c="".join(sorted(i))
            if c not in hp:
                hp[c]=[i]
            else:
                hp.get(c).append(i)
        return hp.values()
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends