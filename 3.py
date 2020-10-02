import argparse
import libraries.mathprimality as primality
import time

#region commandLineArgs
parser = argparse.ArgumentParser(description="find the largest prime factor of N")
parser.add_argument("-N", help="input number", type=int, default=600851475143)
args = parser.parse_args()      #Parse arguments

#endregion

class Solution:
    def __init__(self, N):
        self.N = N
    
    def solve(self):
        t = time.time_ns()
        res = primality.largest_prime_factor(self.N)
        t2 = time.time_ns()-t
        return res,"Solved in "+str(t2)+" ns"


if __name__ == "__main__":
    print("Project Euler Problem 3")
    sol = Solution(args.N)
    print(sol.solve())
    