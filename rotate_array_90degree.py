class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(i + 1, m):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for j in range(m):
            top = 0
            bottom = n - 1
            while top < bottom:
                mat[top][j], mat[bottom][j] = mat[bottom][j], mat[top][j]
                top += 1
                bottom -= 1

        return mat        
    	
        



