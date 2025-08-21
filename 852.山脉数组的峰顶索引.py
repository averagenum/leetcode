#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left =0
        right = n-2
        while left+1<right:
            mid = (left+right)//2
            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid
        return right
        
# @lc code=end

