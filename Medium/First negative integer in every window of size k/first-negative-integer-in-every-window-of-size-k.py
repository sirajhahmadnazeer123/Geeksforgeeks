#User function Template for python3

from collections import deque

def printFirstNegativeInteger(A, N, K):
    result = []
    window_negatives = deque()

    for i in range(N):
        # Remove elements that are no longer in the current window
        while window_negatives and window_negatives[0] < i - K + 1:
            window_negatives.popleft()

        if A[i] < 0:
            window_negatives.append(i)

        # Check if there are negatives in the current window
        if i >= K - 1:
            result.append(A[window_negatives[0]] if window_negatives else 0)

    return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends