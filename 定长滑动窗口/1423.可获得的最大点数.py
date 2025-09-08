#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
#计算留下的卡牌的最小值
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        allPoint = sum(cardPoints)
        lenleft = len(cardPoints)-k
        pointleft = 0
        minleft = 0
        for i,x in enumerate(cardPoints):
            if i <lenleft:
                pointleft += x
                minleft = pointleft
                continue
            pointleft += x -cardPoints[i-lenleft]
            minleft = min(minleft,pointleft)
        return allPoint - minleft
            # @lc code=end

