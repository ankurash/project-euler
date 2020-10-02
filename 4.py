import argparse
from libraries.palindrome import is_palindrome
from libraries.mathprimality import  factorize
from math import pow
import time

#region commandLineArgs
parser = argparse.ArgumentParser(description="find the largest palindrome which is multiple of two N digit numbers")
parser.add_argument("-N", help="number of digits in each number", type=int, default=3)
args = parser.parse_args()      #Parse arguments

#endregion

class Solution:
    def __init__(self, N):
        self.N = N
        self.L = int(pow(10,N-1))
        self.U = self.L*10 - 1
    
    def solve(self):
        res = 0
        found = False
        t = time.time_ns()
        for i in reversed(range(self.U*self.U+1)):
            if is_palindrome(i):
                factor_pairs = factorize(i)
                for a,b in factor_pairs:
                    if a>=self.L and a<=self.U and b>=self.L and b<=self.U:
                        res = i
                        found = True
                        break
            if found:
                break
        t2 = time.time_ns()-t
        return res,"Solved in "+str(t2)+" ns"


if __name__ == "__main__":
    print("Project Euler Problem 4: the largest palindrome which is multiple of two N digit numbers")
    sol = Solution(args.N)
    print(sol.solve())
    