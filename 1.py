import argparse

#region commandLineArgs
parser = argparse.ArgumentParser(description="sum of all the multiples of 3 or 5 under N")
parser.add_argument("-N", help="max number", type=int, default=1000)
args = parser.parse_args()      #Parse arguments

#endregion

class Solution:
    def __init__(self,N):
        self.sum = 0
        self.N = N

    def solve(self):
        for i in range(self.N):
            if i%3 == 0 or i%5 == 0:
                self.sum += i
        return self.sum


if __name__ == "__main__":
    print("Project Euler Problem 1")
    res = Solution(args.N)
    print(res.solve())