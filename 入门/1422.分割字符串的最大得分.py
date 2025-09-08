#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        right1 = s.count('1')
        max_score = left0 = 0
        for a in s[:-1]:
            if a == '0':
                left0 += 1
            else:  # c == '1'
                right1 -= 1
            score = left0 + right1
            max_score = max(max_score, score)
        return max_score
            

          
            
            
        
# @lc code=end

