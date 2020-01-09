class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=abs(n)
        single=1
        if n%2==1:
            single=x
        return (self.myPow(x,n//2)**2)*single

solution=Solution()
print(solution.myPow(5,-2))