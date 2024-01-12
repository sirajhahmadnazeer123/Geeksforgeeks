import random

class Solution:
    def isPrime(self, N):
        # code here
        if N < 2:
            return 0  # 0 and 1 are not prime numbers

        # Miller-Rabin primality test
        def is_probably_prime(n, k=5):  # Default number of iterations for accuracy
            if n == 2 or n == 3:
                return 1
            if n % 2 == 0:
                return 0

            # Write n as 2^r * d + 1
            r, d = 0, n - 1
            while d % 2 == 0:
                r += 1
                d //= 2

            # Witness loop
            for _ in range(k):
                a = random.randint(2, n - 2)
                x = pow(a, d, n)
                if x == 1 or x == n - 1:
                    continue

                for _ in range(r - 1):
                    x = pow(x, 2, n)
                    if x == n - 1:
                        break
                else:
                    return 0  # n is composite

            return 1  # n is probably prime

        return is_probably_prime(N)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends