#!/usr/bin/python3
""" Doc """
matrix_mul = __import__('100-matrix_mul').matrix_mul

m_a = [[5, 6,], [7, 8]]
m_b = [[5, 6], [7, 8]]
try:
    print(matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
