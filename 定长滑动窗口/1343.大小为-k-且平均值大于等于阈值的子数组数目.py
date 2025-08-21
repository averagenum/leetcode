#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ave = sum(arr[:k])/k
        count = 1 if ave>=threshold else 0
        for i in range(k,len(arr)):
            ave += (arr[i]-arr[i-k])/k
            count += 1 if ave>=threshold else 0
        return count
        
# @lc code=end

