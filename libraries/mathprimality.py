import math

def largest_prime_factor(N):
    while N%2==0:
        N=N//2
    for i in range(3,int(math.sqrt(N)),2):
        while N%i==0 and N!=i:
            N=N//i
    return N

def factorize(N, pairs=True):
    if pairs:
        factor_pairs = []
        i = 1
        L = N
        while i<L:
            L = N//i
            if N%i==0:
                factor_pairs.append((i,L))
            i += 1
        return factor_pairs
    else:
        factors = [1]
        i = 1
        L = N
        while i<L:
            L = N//i
            if N%i==0:
                if i not in factors:
                    factors.append(i)
                if L not in factors:
                    factors.append(L)
            i += 1
        return factors

def hcf(a,b):
    return max(set(factorize(a,pairs=False)).intersection(factorize(b,pairs=False)))


def N_primes(N):
    try:
        nums = [True] * (N*100)
    except:
        nums = [True] * (N*10)
        
    count = 0
    x = 1
    primes = []
    while count<N:
        x += 1
        if nums[x]:
            primes.append(x)
            count += 1
            for i in range(x, len(nums), x):
                nums[i] = False
    return primes