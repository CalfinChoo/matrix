"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for c in range(4):
        line = ""
        for r in range(len(matrix)):
            line += str(matrix[r][c]) + " "
        print(line)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    m = []
    temp = []
    for i in range(4):
        while(len(temp) != i):
            temp.append(0.00)
        temp.append(matrix)
        for n in range(i + 1, 4): temp.append(0.00)
        m.append(temp)
        temp = []
    print_matrix(m)
    return m


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    # 4 x n
    newMatrix = []

    for c in range(len(m2)):
        sum = 0
        for r in range(4):
            sum += m2[c][r] * m1[]





def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
