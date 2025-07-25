class Solution:
    def transpose(self, mat):
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(i + 1, m):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        return mat
        