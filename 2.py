import argparse
import libraries.fibonacci as fib
import time

#region commandLineArgs
parser = argparse.ArgumentParser(description="find the sum of the even-valued terms till elements less than N")
parser.add_argument("-N", help="Max element value", type=int, default=4000000)
args = parser.parse_args()      #Parse arguments

#endregion

class Solution:
    def __init__(self, N):
        self.sum = 0
        self.N = N

    def solve(self):
        t = time.time_ns()
        f = fib.Fibonacci()
        f.fill_till_Max_N(self.N)
        res = f.sum_of_elements_divisible_by_D(2)
        t2 = time.time_ns()-t
        return res, "Solved in "+str(t2)+" ns"


if __name__ == "__main__":
    print("Project Euler Problem 2: the sum of the even-valued terms till elements less than N")
    sol = Solution(args.N)
    print(sol.solve())
    