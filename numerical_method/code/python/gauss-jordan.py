from helper import *


def gauss_jordan(matrix: np.ndarray) -> Optional[np.ndarray]:
    """
    Gauss-Jordan 法消去

    :param matrix: 矩阵
    :return: 消去后的结果
    """
    row, col = matrix.shape
    if col - row > 0:
        for i in range(0, row):
            # 列主元
            max_element = my_max(matrix, i)
            if matrix[max_element][i] == 0:
                print("no unique solution")
                return None
            if max_element != i:
                swap_rows(matrix, i, max_element)

            # 消去
            for j in range(0, row):
                m = - (matrix[j][i] / matrix[i][i])
                if j != i:
                    matrix[j] = matrix[j] + m * matrix[i]
                else:
                    matrix[j] = matrix[j] / matrix[i][i]
            # print(matrix)
        # print(a)
        return matrix
    else:
        print("illegal input")
        return None


if __name__ == '__main__':
    a = get_matrix("m4.txt")
    if a is not None:
        a = gauss_jordan(a)
        if a is not None:
            print(a)
