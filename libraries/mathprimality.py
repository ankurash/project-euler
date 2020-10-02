import math

def largest_prime_factor(N):
    while N%2==0:
        N=N/2
    for i in range(3,int(math.sqrt(N)),2):
        while N%i==0 and N!=i:
            N=N/i
    return int(N)
