import math

def largest_prime_factor(N):
    while N%2==0:
        N=N/2
    for i in range(3,int(math.sqrt(N)),2):
        while N%i==0 and N!=i:
            N=N/i
    return int(N)

def factorize(N):
    factor_pairs = []
    i = 1
    L = N/2
    while i<L:
        L = int(N/i)
        if N%i==0:
            factor_pairs.append((i,L))
        i += 1
    return factor_pairs