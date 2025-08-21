#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n >0:
            while n%5 == 0:
                n //=5
            while n%3 == 0:
                n //=3
            while n%2 == 0:
                n //=2
            if n ==1:
                return True
            else:
                return False
        else:
            return False
# @lc code=end

