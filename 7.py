import argparse
from time import time_ns
from libraries.mathprimality import N_primes

#region commandLineArgs
parser = argparse.ArgumentParser(description="the Nth prime number")
parser.add_argument('-N', help="Nth prime number", type=int, default=10001)
args = parser.parse_args()

#endregion

class Solution():
    def __init__(self,N):
        self.N = N

    def __repr__(self):
        return str(self.N)

    def solve(self):
        t = time_ns()
        res = N_primes(self.N)[-1]
        t2 = time_ns()-t
        return res,"Solved in "+str(t2)+" ns"

if __name__ == "__main__":
    print("Project Euler problem 7: find the Nth prime number")
    sol = Solution(args.N)
    print(sol.solve())