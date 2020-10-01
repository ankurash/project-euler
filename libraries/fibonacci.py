class Fibonacci():
    def __init__(self,N=1):
        self.nums = [1,1]
        self.fill_N_elements(N)
    
    def fill_N_elements(self,N):
        while len(self.nums) < N:
            self.nums.append(self.nums[-1] + self.nums[-2])
    
    def fill_till_Max_N(self, N):
        while self.nums[-1] + self.nums[-2] < N:
            self.nums.append(self.nums[-1] + self.nums[-2])

    def nth_number(self,n):
        if n<3:
            return 1
        else:
            self.fill_N_elements(n)
            return self.nums[n-1]

    def sum_till_Nth_element(self, N, iter=1):
        if len(self.nums) < N:
            self.fill_N_elements(N)
        return sum(self.nums[0:N])
    
    def sum_till_Max_N(self, N, iter=1):
        sum = 0
        while(self.nums[-1]<N):
            self.nth_number(len(self.nums)+1)
        for i in range(0,N,iter):
            sum += self.nums[i]
        return sum

    def sum_of_elements_divisible_by_D(self, D):
        return sum(e for e in self.nums if e%D==0)
    
    def __repr__(self):
        return str(self.nums)