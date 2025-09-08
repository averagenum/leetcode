#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m,n = len(matrix),len(matrix[0])
        trans = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                trans[j][i] = matrix[i][j]
        return trans
    
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6]]
    print(sol.transpose(matrix))
                
# @lc code=end

