from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        min_len=float('inf')
        for s in strs:
            if len(s)<min_len:
                min_len=len(s)
        left=1
        right=min_len
        while left<=right:
            mid = (left + right) // 2
            if self.is_commom_prefix(strs,mid):
                left=mid+1
            else:
                right=mid-1
        return strs[0][0:(left+right)//2]

    def is_commom_prefix(self,strs,index):
        sub_str=strs[0][0:index]
        for i in range(1,len(strs)):
            if not strs[i].startswith(sub_str):
                return False
        return True

solution=Solution()
print(solution.longestCommonPrefix(['aa','ab']))