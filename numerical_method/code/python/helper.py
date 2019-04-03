import numpy as np
from typing import Optional


def get_matrix(filename: str, delim: str = " ") -> Optional[np.ndarray]:
    """
    从文件中读取矩阵，delim 为分隔符，默认为空格

    :param filename: 文件名
    :param delim: 分隔符
    :return: 矩阵
    """
    try:
        f = open(filename, "r")
        try:
            lines = f.readlines()
            matrix = []
            for line in lines:
                row = list(map(float, line.split(delim)))
                matrix.append(row)
            return np.array(matrix)
        finally:
            f.close()
    except IOError:
        print("file " + filename + " does't exist")
        return None


def my_max(matrix: np.ndarray, index: int) -> int:
    """
    选取列主元

    :param matrix: 矩阵
    :param index: 列下标
    :return: 主元所在行下标
    """
    row, col = matrix.shape
    m = index
    temp = abs(matrix[index][index])
    for i in range(index, row):
        if abs(matrix[i][index]) > temp:
            m = i
            temp = abs(matrix[i][index])
    return m


def swap_rows(matrix: np.ndarray, i: int, j: int) -> None:
    """
    交换两行

    :param matrix: 矩阵
    :param i: 行下标
    :param j: 行下标
    :return: None
    """
    row, col = matrix.shape
    for x in range(0, col):
        matrix[i][x], matrix[j][x] = matrix[j][x], matrix[i][x]
