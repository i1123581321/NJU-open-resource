from helper import *


def SOR(matrix: np.ndarray, k: int, omega: float, verbose: bool = False) -> Optional[np.ndarray]:
    """
    超松弛迭代法

    :param matrix: 增广矩阵
    :param k: 迭代次数
    :param omega: 松弛因子
    :param verbose: 是否输出每次迭代的结果
    :return: 解向量
    """

    row, col = matrix.shape
    if col - row == 1:
        x0 = np.zeros(row)
        x1 = np.zeros(row)
        for _ in range(0, k):
            for i in range(0, row):
                y = (matrix[i][col - 1] - sum([matrix[i][j] * x1[j] for j in range(0, i)]) - sum(
                    [matrix[i][j] * x0[j] for j in range(i + 1, row)])) / matrix[i][i]
                x1[i] = (1 - omega) * x0[i] + omega * y
            if verbose:
                print(str(_ + 1) + ": ", end="")
                print(x1)
                print(np.linalg.norm(x1 - np.array([0.5, 1, -0.5]), ord=np.inf))
            x0 = x1.copy()
        return x1
    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m8.txt")
    ans = SOR(a, 100, 1.1, True)
    print(ans)
