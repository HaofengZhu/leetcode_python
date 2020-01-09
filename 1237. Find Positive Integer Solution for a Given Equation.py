"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List
import numpy as np
class CustomFunction:
    def f(self, x, y):
        return x*y

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result=[]
        y_min = 1001
        for x in range(1, 1001):
            l = 1
            r = 1000
            find=False

            while l<=r:
                y=(l+r)//2
                output=customfunction.f(x,y)
                if output==z:
                    result.append([x,y])
                    if y<y_min:
                        y_min=y
                    find=True
                    break
                elif output>z:
                    r=y-1
                else:
                    l=y+1
            if not find and y_min==1:
                break
        return result

solution=Solution()
c=CustomFunction()
print(solution.findSolution(c,5))