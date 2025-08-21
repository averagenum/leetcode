#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        count = 0
        for i, a in enumerate(s):
            if a in 'aeiou':
                count += 1
            if i < k:
                res = max(res, count)
                continue
            elif s[i-k] in 'aeiou':
                m = s[i-k]
                count -= 1
            res = max(res, count)
        return res
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxVowels('a',1))
        
# @lc code=end

