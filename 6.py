import argparse
from time import time_ns
from libraries.number_series import sum_of_squares_of_N_natural_numbers, sum_of_N_natural_numbers

parser = argparse.ArgumentParser(description="the  difference between the sum of the squares of the first N natural numbers and the square of the sum")
parser.add_argument('-N', help="max number", type=int, default=100)
args = parser.parse_args()


class Solution():
    def __init__(self,N):
        self.N = N

    def __repr__(self):
        return str(self.N)

    def solve(self):
        t = time_ns()
        s = sum_of_N_natural_numbers(self.N)
        res = s*s - sum_of_squares_of_N_natural_numbers(self.N)
        t2 = time_ns()-t
        return res,"Solved in "+str(t2)+" ns"

if __name__ == "__main__":
    print("Project Euler problem 6: the  difference between the sum of the squares of the first N natural numbers and the square of the sum")
    sol = Solution(args.N)
    print(sol.solve())
    