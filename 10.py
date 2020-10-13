import argparse
from time import time_ns
from libraries.mathprimality import primes_till_N

#region commandLineArgs
parser = argparse.ArgumentParser(description="sum of all primes till N")
parser.add_argument('-N', help="upper bound", type=int, default=2000000)
args = parser.parse_args()

#endregion

class Solution():
    def __init__(self, N):
        self.N = N

    def solve(self):
        t = time_ns()
        res = sum(primes_till_N(self.N))
        t2 = time_ns()-t
        return res,"Solved in "+str(t2)+" ns"

    
if __name__ == "__main__":
    print("Project Euler problem 10: find the sum of all primes till N")
    sol = Solution(args.N)
    print(sol.solve())
    