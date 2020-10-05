import argparse
from time import time_ns
from libraries.mathprimality import factorize, hcf

parser = argparse.ArgumentParser(description="the smallest positive number that is evenly divisible by all of the numbers from 1 to N")
parser.add_argument('-N', help="max number", type=int, default=20)
args = parser.parse_args()


class Solution():
    def __init__(self,N):
        self.N = N

    def __repr__(self):
        return str(self.N)

    def solve(self):
        lcm = 1
        t = time_ns()
        for i in range(self.N,1,-1):
            lcm = i*lcm//hcf(i,lcm)
        t2 = time_ns()-t
        return lcm,"Solved in "+str(t2)+" ns"

if __name__ == "__main__":
    sol = Solution(args.N)
    print(sol.solve())
    