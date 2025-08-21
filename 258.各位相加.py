#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            add = 0
            while num >0:
                add += num %10
                num //= 10
            num = add
        return num
# @lc code=end


# 本地测试代码
if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(38))  # 应该输出 2
    print(sol.addDigits(0))    # 应该输出 0
    print(sol.addDigits(12345)) # 应该输出 6
   