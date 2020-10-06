class Fibonacci():
    def __init__(self,N=1):
        """Initialization

        Args:
            N (int, optional): number of fibonacci numbers to generate. Defaults to 1.
        """
        self.nums = [1,1]
        self.fill_N_elements(N)
    
    def fill_N_elements(self,N:int):
        """Fill up the list with N fibonacci numbers

        Args:
            N (int): number
        """
        while len(self.nums) < N:
            self.nums.append(self.nums[-1] + self.nums[-2])
    
    def fill_till_Max_N(self, N:int):
        """Fill up the list with fibonacci numbers < N

        Args:
            N (int): number
        """
        while self.nums[-1] + self.nums[-2] < N:
            self.nums.append(self.nums[-1] + self.nums[-2])

    def nth_number(self,n:int):
        """Return nth fibonacci number

        Args:
            n (int): number

        Returns:
            [int]: nth fibonacci number
        """
        if n<3:
            return 1
        else:
            self.fill_N_elements(n)
            return self.nums[n-1]

    def sum_till_Nth_element(self, N:int, iter=1):
        """Fibonacci sum till N iterated over iter indices

        Args:
            N (int): number
            iter (int, optional): iteration/jump value in list. Defaults to 1.

        Returns:
            [int]: sum
        """
        if len(self.nums) < N:
            self.fill_N_elements(N)
        return sum(self.nums[0:N])
    
    def sum_till_Max_N(self, N:int, iter=1):
        """sum of all fibonacci numbers less than N iterated over iter indices

        Args:
            N (int): number
            iter (int, optional): iteration/jump value in list. Defaults to 1.

        Returns:
            [int]: sum
        """
        sum = 0
        while(self.nums[-1]<N):
            self.nth_number(len(self.nums)+1)
        for i in range(0,N,iter):
            sum += self.nums[i]
        return sum

    def sum_of_elements_divisible_by_D(self, D:int):
        """sum of fibonacci elements in the list that are multiples of D

        Args:
            D (int): divisor

        Returns:
            [int]: sum
        """
        return sum(e for e in self.nums if e%D==0)
    
    def __repr__(self):
        return str(self.nums)