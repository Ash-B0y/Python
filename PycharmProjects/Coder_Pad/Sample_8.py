def findMaxPath(mat):
    # To find max val in first row
    res = -1

    for i in range(1, N):

        res = -1
        for j in range(M):

            # When all paths are possible
            if (j > 0 and j < M - 1):
                mat[i][j] += max(mat[i - 1][j],
                                 max(mat[i - 1][j - 1],
                                     mat[i - 1][j + 1]))

                # When diagonal right is not possible
            elif (j > 0):
                mat[i][j] += max(mat[i - 1][j],
                                 mat[i - 1][j - 1])

                # When diagonal left is not possible
            elif (j < M - 1):
                mat[i][j] += max(mat[i - 1][j],
                                 mat[i - 1][j + 1])

                # Store max path sum
            res = max(mat[i][j], res)
    return res


# Driver program to check findMaxPath
N = 4
M = 4
mat = ([[0, 0, 0, 1],
        [100, 0, 0, 0],
        [100, 0, 0, 0],
        [100, 0, 0, 0]])

print(findMaxPath(mat))
print(mat)