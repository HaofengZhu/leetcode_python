import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low,high=1,max(piles)
        self.piles=piles
        self.H=H
        while low<=high:
            K=(low+high)//2
            if self.can_eat_all(K):
                high=K-1
            else:
                low=K+1
        return low

    def can_eat_all(self,K):
        times=[math.ceil(pile/K) for pile in self.piles]
        return sum(times)<=self.H

solution=Solution()
print(solution.minEatingSpeed([3,6,7,11],8))