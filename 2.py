import argparse
import libraries.fibonacci as fib

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
        res = fib.Fibonacci()
        res.fill_till_Max_N(self.N)
        return res.sum_of_elements_divisible_by_D(2)


if __name__ == "__main__":
    print("Project Euler Problem 2")
    res = Solution(args.N)
    print(res.solve())
    