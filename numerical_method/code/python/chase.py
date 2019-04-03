from helper import *


def get_b(matrix, i):
    return matrix[i][i]


def get_a(matrix, i):
    return matrix[i - 1][i]


def get_c(matrix, i):
    return matrix[i][i + 1]


def chase(matrix: np.ndarray) -> Optional[np.ndarray]:
    """
    追赶法解三对角矩阵

    :param matrix: 增广矩阵
    :return: 解向量
    """
    row, col = matrix.shape
    if col - row == 1:
        beta = np.zeros(row)
        y = np.zeros(row)
        x = np.zeros(row)
        beta[0] = get_c(matrix, 0) / get_b(matrix, 0)
        for i in range(1, row - 1):
            beta[i] = get_c(matrix, i) / (get_b(matrix, i) - get_a(matrix, i) * beta[i - 1])
        y[0] = matrix[0][col - 1] / get_b(matrix, 0)
        for i in range(1, row):
            y[i] = (matrix[i][col - 1] - get_a(matrix, i) * y[i - 1]) / (
                    get_b(matrix, i) - get_a(matrix, i) * beta[i - 1])
        x[row - 1] = y[row - 1]
        for i in range(row - 2, -1, -1):
            x[i] = y[i] - beta[i] * x[i + 1]

        return np.transpose(x)
    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m6.txt")
    ans = chase(a)
    if ans is not None:
        print(ans)
