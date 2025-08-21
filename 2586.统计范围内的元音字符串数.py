#
# @lc app=leetcode.cn id=2586 lang=python3
#
# [2586] 统计范围内的元音字符串数
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowel = 'aeiou'
        for i in range(left, right+1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                count +=1
        return count
        
# @lc code=end

