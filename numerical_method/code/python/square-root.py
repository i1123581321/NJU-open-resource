from helper import *


def square_root(matrix: np.ndarray) -> Optional[np.ndarray]:
    """
    Cholesky法 分解正定阵

    :param matrix: 正定阵
    :return: 分解后的下三角矩阵
    """
    row, col = matrix.shape
    if row == col:
        L = np.zeros((row, row))
        # 初始
        L[0][0] = np.sqrt(matrix[0][0])
        for i in range(1, row):
            L[i][0] = (matrix[i][0]) / L[0][0]

        # 迭代
        for j in range(1, row):
            L[j][j] = np.sqrt(matrix[j][j] - sum([L[j][k] * L[j][k] for k in range(0, j)]))
            for i in range(j + 1, row):
                L[i][j] = (matrix[i][j] - sum([L[i][k] * L[j][k] for k in range(0, j)])) / L[j][j]
        return L
    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m5.txt")
    L = square_root(a)
    if L is not None:
        print(L)
        print(L.dot(np.transpose(L)))
