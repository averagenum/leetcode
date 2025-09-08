#
# @lc app=leetcode.cn id=2841 lang=python3
#
# [2841] 几乎唯一子数组的最大和
#

# @lc code=start
class Solution:
    def NumOfDiff(self,arr:list)->int :
        return len(set(arr))
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        win =[]
        maxsum = 0
        for i,x in enumerate(nums):
            if i <= k-1 :
                win.append(x)
                if len(win) == k:
                    if self.NumOfDiff(win) >= m:
                        maxsum = max(maxsum, sum(win))
                continue
            
            del win[0]
            win.append(x)
            
            if self.NumOfDiff(win) >= m:
                maxsum = max(maxsum, sum(win))
                
        return maxsum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSum([2,6,7,3,1,7],3,4))
# @lc code=end
