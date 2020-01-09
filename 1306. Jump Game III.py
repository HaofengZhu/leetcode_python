from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        _len_=len(arr)
        seen=set()
        queue=deque()
        queue.append(start)
        while(queue):
            idx=queue.popleft()
            if arr[idx]==0:
                return True
            seen.add(idx)
            var=idx-arr[idx]
            if var not in seen and var>-1:
                queue.append(var)
            var=idx+arr[idx]
            if var not in seen and var<len(arr):
                queue.append(var)
        return False



solution = Solution()
arr=[3,0,2,1,2]
start=2
print(solution.canReach(arr,start))

