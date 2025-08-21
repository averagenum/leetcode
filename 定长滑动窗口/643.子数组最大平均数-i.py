#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        average = res = sum(nums[:k])/k
        for i in range(k,len(nums)):  
            average += (nums[i]-nums[i-k])/k
            res = max(res,average)
        return res
if __name__ =='__main__':
    sol = Solution()
    print(sol.findMaxAverage([-1],1))
            
        
# @lc code=end

