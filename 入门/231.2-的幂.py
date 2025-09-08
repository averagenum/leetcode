#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
import math

class Solution:
    def is_whole_number(self, n: float) -> bool:
        # 处理浮点数精度问题：检查n是否接近整数
        return abs(n - round(n)) < 1e-10

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:  # 处理0和负数的情况
            return False
        log_value = math.log2(n)
        return self.is_whole_number(log_value)  # 调用类方法需要用self
        
# @lc code=end

