#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i,x in enumerate(blocks):
            if i <=k-1 :
                w += 1 if x =='W' else 0
                min_w = w
                continue
            w +=(blocks[i]=='W')-(blocks[i-k] == 'W')
            min_w = min(min_w,w)
        return min_w
# @lc code=end

