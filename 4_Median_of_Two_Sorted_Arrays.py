from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        i = m // 2
        while True:
            j = (m + n) // 2 - i
            if i == 0:
                if m==1:
                    #num1只有一个数的特殊情况,插入排序
                    for k,v in enumerate(nums2):
                        if v<nums1[0]:
                            continue
                        else:
                            if (m + n) % 2 == 1:
                                index = (m + n) // 2
                                if k==index:
                                    return nums1[0]
                                elif k<index:
                                    return nums2[index-1]
                                else:
                                    return nums2[index]
                            else:
                                index=n//2
                                if k-1==index or k==index:
                                    return (nums1[0]+nums2[index])/2
                                elif k<index:
                                    return (nums2[index]+nums2[index-1])/2
                                else:
                                    return (nums2[index]+nums2[index+1])/2
                # num1数列完全大于num2数列
                index = (m + n) // 2
                if (m + n) % 2 == 1:
                    return nums2[index]
                else:
                    if m == n:
                        return (nums1[0] + nums2[index - 1]) / 2.0
                    else:
                        return (nums2[index - 1] + nums2[index]) / 2.0
            elif i == m:
                # num1数列完全小于num2数列
                index = (m + n) // 2
                if (m + n) % 2 == 1:
                    return nums2[index - m]
                else:
                    if m == n:
                        return (nums1[index - 1] + nums2[0]) / 2.0
                    else:
                        return (nums2[index - m - 1] + nums2[index - m]) / 2.0
            else:
                if nums1[i - 1] <= nums2[j]:
                    if j == 0 or nums2[j - 1] < nums1[i]:
                        # 找到中间值
                        if (m + n) % 2 == 1:
                            return min(nums1[i], nums2[j])
                        else:
                            return (max(nums1[i - 1], nums2[j - 1]) + min(nums1[i], nums2[j])) / 2.0
                    else:
                        i += 1
                else:
                    i -= 1


solution = Solution()
print(solution.findMedianSortedArrays([3,4],[1,2,5]))
