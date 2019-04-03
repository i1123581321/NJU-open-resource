from helper import *


def jacobi(matrix: np.ndarray, k: int, verbose: bool = False) -> Optional[np.ndarray]:
    """
    Jacobi 迭代法求解

    :param matrix: 增广矩阵
    :param k: 迭代次数
    :param verbose: 是否输出每次迭代的结果
    :return: 解向量
    """
    row, col = matrix.shape
    if col - row == 1:
        x0 = np.zeros(row)
        x1 = np.zeros(row)
        for _ in range(0, k):
            for i in range(0, row):
                x1[i] = (matrix[i][col - 1] - sum([matrix[i][j] * x0[j] for j in range(0, i)]) - sum(
                    [matrix[i][j] * x0[j] for j in range(i + 1, row)])) / matrix[i][i]
            if verbose:
                print(str(_) + ": ", end="")
                print(x1)
            x0 = x1
        return x1
    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m3.txt")
    x = jacobi(a, 100, True)
    print(x)
