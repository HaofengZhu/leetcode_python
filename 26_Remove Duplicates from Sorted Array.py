from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        prev_num = None
        i = 0
        while i < len(nums):
            if nums[i] != prev_num:
                count += 1
                prev_num = nums[i]
                i += 1
            else:
                del nums[i]

        return count

solution=Solution()
arr=[1,2,2,3]
solution.removeDuplicates(arr)
print(arr)