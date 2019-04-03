from helper import *


def gauss(matrix: np.ndarray) -> Optional[np.ndarray]:
    """
    Gauss 消去法

    :param matrix: 增广矩阵
    :return: 解向量
    """
    row, col = matrix.shape
    if col - row == 1:
        for i in range(0, row - 1):
            # 列主元
            max_element = my_max(matrix, i)
            if matrix[max_element][i] == 0:
                print("no unique solution")
                return None
            if max_element != i:
                swap_rows(matrix, i, max_element)

            # 消去
            for j in range(i + 1, row):
                m = - (matrix[j][i] / matrix[i][i])
                matrix[j] = matrix[j] + m * matrix[i]
            # print(matrix)
        # print(a)
        # 回代
        x = np.zeros(row)
        x[row - 1] = matrix[row - 1][col - 1] / matrix[row - 1][col - 2]
        for k in range(row - 2, -1, -1):
            x_k = (matrix[k][col - 1] - sum([matrix[k][j] * x[j] for j in range(k + 1, row)])) / matrix[k][k]
            x[k] = x_k
        return np.transpose(x)
    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m3.txt")
    if a is not None:
        x = gauss(a)
        if x is not None:
            print(x)
