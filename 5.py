import argparse
from time import time_ns
from libraries.mathprimality import factorize, hcf

#region commandLineArgs
parser = argparse.ArgumentParser(description="the smallest positive number that is evenly divisible by all of the numbers from 1 to N")
parser.add_argument('-N', help="max number", type=int, default=20)
args = parser.parse_args()

#endregion

class Solution():
    def __init__(self,N):
        self.N = N

    def __repr__(self):
        return str(self.N)

    def solve(self):
        t = time_ns()
        lcm = 1
        for i in range(self.N,1,-1):
            lcm = i*lcm//hcf(i,lcm)
        t2 = time_ns()-t
        return lcm,"Solved in "+str(t2)+" ns"

if __name__ == "__main__":
    print("Project Euler problem 5: the smallest positive number that is evenly divisible by all of the numbers from 1 to N")
    sol = Solution(args.N)
    print(sol.solve())
    