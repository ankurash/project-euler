import argparse
import time

#region commandLineArgs
parser = argparse.ArgumentParser(description="find sum of all the multiples of 3 or 5 under N")
parser.add_argument("-N", help="max number", type=int, default=1000)
args = parser.parse_args()      #Parse arguments

#endregion

class Solution:
    def __init__(self,N):
        self.sum = 0
        self.N = N

    def solve(self):
        t = time.time_ns()
        for i in range(self.N):
            if i%3 == 0 or i%5 == 0:
                self.sum += i
        t2 = time.time_ns()-t
        return self.sum, "Solved in "+str(t2)+" ns"


if __name__ == "__main__":
    print("Project Euler Problem 1: sum of all the multiples of 3 or 5 under N")
    sol = Solution(args.N)
    print(sol.solve())