from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                #突然降序
                j=i+1
                while j<len(nums) and nums[j]>nums[i-1]:
                    j+=1
                nums[i-1],nums[j-1]=nums[j-1],nums[i-1]
                #对i及后面的元素反转
                nums[i:]=nums[i:][::-1]
                #python自带的反转比自己实现的快：
                # for k in range((len(nums) - i) // 2):
                #     nums[i + k], nums[len(nums) - k - 1] = nums[len(nums) - k - 1], nums[i + k]
                return

        nums[:]=nums[::-1]

solution=Solution()
arr=[1,3,2]
solution.nextPermutation(arr)
print(arr)

