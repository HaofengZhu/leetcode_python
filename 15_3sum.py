from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        #非0的最多2个，0最多3个
        cut_nums=[]
        num_count={}
        for num in nums:
            if num not in num_count.keys():
                num_count[num]=0
            if num_count[num]>2:
                continue
            else:
                num_count[num]+=1
                cut_nums.append(num)

        if nums.count(0)>2:
            cut_nums.index(0,cut_nums.index(0))

        for center in range(len(cut_nums) - 1):
            left = 0
            right = len(cut_nums) - 1

            while left < center and center < right:

                temp = cut_nums[left] + cut_nums[center] + cut_nums[right]

                if temp == 0:
                    if (cut_nums[left], cut_nums[center], cut_nums[right]) not in ans:
                        ans.add((cut_nums[left], cut_nums[center], cut_nums[right]))
                    left += 1
                    right -= 1
                elif temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1
        return list(ans)


s=Solution()
a=s.threeSum([-1,0,1,2,-1,-4])
print(a)
a=s.threeSum([0,0,0])
print(a)
a=s.threeSum([0,0,0,0,0,0,0,0,0])
print(a)