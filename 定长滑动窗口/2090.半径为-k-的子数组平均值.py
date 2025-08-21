#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#

# @lc code=start
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1]*n
        
        if 2*k+1>n:
            return avgs
        
        s = sum(nums[:2*k+1]) 
        
        for i in range(k, n-k):
            if i < k or i >n-k-1:
                continue
            else :
                avgs[i]=(s//(2*k+1))
                s += nums[i+k+1]-nums[i-k] if i+k+1 <= n-1 else 0
                
        return avgs
    
if __name__ =='__main__':
    sol = Solution()
    print(sol.getAverages([7,4,3,9,1,8,5,2,6], 3))
            
            
        
# @lc code=end

