from helper import *


def doolittle(matrix: np.ndarray) -> Optional[np.ndarray]:
    """
    Doolittle 法 LU 分解

    :param matrix: 系数矩阵
    :return: 分解后的矩阵，下半为 L，上半为 U
    """
    row, col = matrix.shape
    if row == col:
        u = np.zeros((row, row))

        # init
        for j in range(0, row):
            u[0][j] = matrix[0][j]
            # l[j][j] = 1
        for i in range(1, row):
            u[i][0] = matrix[i][0] / u[0][0]

        # iteration
        for r in range(1, row):
            for i in range(r, row):
                u[r][i] = matrix[r][i] - sum([u[r][k] * u[k][i] for k in range(0, r)])
            for k in range(r + 1, row):
                u[k][r] = (matrix[k][r] - sum([u[k][n] * u[n][r] for n in range(0, r)])) / u[r][r]

        return u

    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m1.txt")
    U = doolittle(a)
    # print(L)
    print(U)
