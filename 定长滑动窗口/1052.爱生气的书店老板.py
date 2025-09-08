#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        minStf =sum(customers)- sum( [a * b for a, b in zip(customers, grumpy)])
        addStf = maxaddStf = 0
        
        if minutes == 0:
            return minStf
        
        for i in range(len(grumpy)):
            if i < minutes:
                addStf += customers[i]*grumpy[i]
                maxaddStf = addStf
                continue
            addStf += customers[i]*grumpy[i] -customers[i-minutes]*(grumpy[i-minutes])
            maxaddStf = max(addStf,maxaddStf)
        return minStf + maxaddStf
            
            
# @lc code=end

