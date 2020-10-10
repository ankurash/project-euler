import argparse
from libraries.mathprimality import largest_prime_factor, factorize
from time import time_ns

#region commandLineArgs
parser = argparse.ArgumentParser(description="find the largest prime factor of N")
parser.add_argument("-N", help="input number", type=int, default=600851475143)
args = parser.parse_args()      #Parse arguments

#endregion

class Solution:
    def __init__(self, N):
        self.N = N
    
    def solve(self):
        t = time_ns()
        res = largest_prime_factor(self.N)
        t2 = time_ns()-t
        return res,"Solved in "+str(t2)+" ns"
    
    def solve2(self):
        t = time_ns()
        for a,b in factorize(self.N):
            if len(factorize(b))<2:
                res = b
                break
            if len(factorize(a))<2:
                res = a
        t2 = time_ns()-t
        return res,"Solved in "+str(t2)+" ns"


if __name__ == "__main__":
    print("Project Euler Problem 3: largest prime factor of N")
    sol = Solution(args.N)
    print("\t",sol.solve())
    print("\t",sol.solve2())
    