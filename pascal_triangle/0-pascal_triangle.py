#!/usr/bin/python3
''' Pascal's Triangle '''


def pascal_triangle(n):
    ''' returns a list of lists of integers
    representing the Pascal's triangle of n '''
    t = []
    if n <= 0:
        return t
    t = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(t[i - 1]) - 1):
            current = t[i - 1]
            tmp.append(t[i - 1][j] + t[i - 1][j + 1])
        tmp.append(1)
        t.append(tmp)
    return t
