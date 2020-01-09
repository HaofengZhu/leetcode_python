from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,tail_index=0,len(nums)-1
        while i<len(nums):
            if nums[i]==val:
                tmp=tail_index
                while nums[tmp]==val:
                    if tmp==i:
                        del nums[tmp:tail_index+1]
                        return i
                    tmp-=1
                nums[i]=nums[tmp]
                del nums[tmp:tail_index+1]
                tail_index=tmp-1
            i+=1
        return i

solution=Solution()
arr=[3,3]
print(solution.removeElement(arr,3),arr)