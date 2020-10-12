import argparse
from time import time_ns

#region commandLineArgs
parser = argparse.ArgumentParser(description="Pythagorean triplet with sum 1000")
args = parser.parse_args()

#endregion

class Solution():
    def solve(self):
        t = time_ns()
        res = ""
        found = False
        a=1
        while a<1000 and not found:
            for b in range(1001-a):
                if 1000*(a+b) == 500000 + a*b:
                    res = a*b*(1000-a-b)
                    found = True
                    break
            a += 1
        t2 = time_ns()-t
        return res,"Solved in "+str(t2)+" ns"

    
if __name__ == "__main__":
    print("Project Euler problem 9: find the Pythagorean triplet with sum 1000")
    sol = Solution()
    print(sol.solve())
    