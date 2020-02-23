from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]
matrix = new_matrix(0, 0)

list1 = [140, 150, 165, 169, 155, 176, 170, 171, 150, 167, 167, 154, 157, 173, 197, 198, 176, 180, 181, 180, 177, 178, 185, 187, 187, 186, 190, 196, 196, 194, 190, 180, 173, 171, 171, 188, 199, 201, 201, 199, 200, 214, 218, 219, 219, 218, 220, 220, 211, 190, 160]

diff = []
for i in range(len(list1) - 1):
    diff.append(list1[i] - list1[i + 1])
list2 = [135]
for i, d in enumerate(diff):
    list2.append(list2[i] + d)

for i in range(2):
    add_edge(matrix, list1[0], 481, 0, list1[1], 480, 0)
    add_edge(matrix, list1[1], 480, 0, list1[2], 474, 0)
    add_edge(matrix, list1[2], 474, 0, list1[3], 470, 0)
    add_edge(matrix, list1[3], 470, 0, list1[4], 457, 0)
    add_edge(matrix, list1[4], 457, 0, list1[5], 455, 0)
    add_edge(matrix, list1[5], 455, 0, list1[6], 453, 0)
    add_edge(matrix, list1[6], 453, 0, list1[7], 431, 0)
    add_edge(matrix, list1[7], 431, 0, list1[8], 430, 0)
    add_edge(matrix, list1[8], 430, 0, list1[9], 418, 0)
    add_edge(matrix, list1[9], 418, 0, list1[10], 416, 0)
    add_edge(matrix, list1[10], 416, 0, list1[11], 412, 0)
    add_edge(matrix, list1[11], 412, 0, list1[12], 407, 0)
    add_edge(matrix, list1[12], 407, 0, list1[13], 405, 0)
    add_edge(matrix, list1[13], 405, 0, list1[14], 397, 0)
    add_edge(matrix, list1[14], 397, 0, list1[15], 395, 0)
    add_edge(matrix, list1[15], 395, 0, list1[16], 329, 0)
    add_edge(matrix, list1[16], 329, 0, list1[17], 326, 0)
    add_edge(matrix, list1[17], 326, 0, list1[18], 323, 0)
    add_edge(matrix, list1[18], 323, 0, list1[19], 320, 0)
    add_edge(matrix, list1[19], 320, 0, list1[20], 318, 0)
    add_edge(matrix, list1[20], 318, 0, list1[21], 311, 0)
    add_edge(matrix, list1[21], 311, 0, list1[22], 309, 0)
    add_edge(matrix, list1[22], 309, 0, list1[23], 306, 0)
    add_edge(matrix, list1[23], 306, 0, list1[24], 302, 0)
    add_edge(matrix, list1[24], 302, 0, list1[25], 300, 0)
    add_edge(matrix, list1[25], 300, 0, list1[26], 298, 0)
    add_edge(matrix, list1[26], 298, 0, list1[27], 292, 0)
    add_edge(matrix, list1[27], 292, 0, list1[28], 288, 0)
    add_edge(matrix, list1[28], 288, 0, list1[29], 284, 0)
    add_edge(matrix, list1[29], 284, 0, list1[30], 280, 0)
    add_edge(matrix, list1[30], 280, 0, list1[31], 276, 0)
    add_edge(matrix, list1[31], 276, 0, list1[32], 275, 0)
    add_edge(matrix, list1[32], 275, 0, list1[33], 266, 0)
    add_edge(matrix, list1[33], 266, 0, list1[34], 253, 0)
    add_edge(matrix, list1[34], 253, 0, list1[35], 180, 0)
    add_edge(matrix, list1[35], 180, 0, list1[36], 174, 0)
    add_edge(matrix, list1[36], 174, 0, list1[37], 170, 0)
    add_edge(matrix, list1[37], 170, 0, list1[38], 166, 0)
    add_edge(matrix, list1[38], 166, 0, list1[39], 158, 0)
    add_edge(matrix, list1[39], 158, 0, list1[40], 151, 0)
    add_edge(matrix, list1[40], 151, 0, list1[41], 136, 0)
    add_edge(matrix, list1[41], 136, 0, list1[42], 128, 0)
    add_edge(matrix, list1[42], 128, 0, list1[43], 122, 0)
    add_edge(matrix, list1[43], 122, 0, list1[44], 117, 0)
    add_edge(matrix, list1[44], 117, 0, list1[45], 109, 0)
    add_edge(matrix, list1[45], 109, 0, list1[46], 100, 0)
    add_edge(matrix, list1[46], 100, 0, list1[47], 79, 0)
    add_edge(matrix, list1[47], 79, 0, list1[48], 70, 0)
    add_edge(matrix, list1[48], 70, 0, list1[49], 59, 0)
    add_edge(matrix, list1[49], 59, 0, list1[50], 50, 0)

    add_edge(matrix, list2[0], 481, 0, list2[1], 480, 0)
    add_edge(matrix, list2[1], 480, 0, list2[2], 474, 0)
    add_edge(matrix, list2[2], 474, 0, list2[3], 470, 0)
    add_edge(matrix, list2[3], 470, 0, list2[4], 457, 0)
    add_edge(matrix, list2[4], 457, 0, list2[5], 455, 0)
    add_edge(matrix, list2[5], 455, 0, list2[6], 453, 0)
    add_edge(matrix, list2[6], 453, 0, list2[7], 431, 0)
    add_edge(matrix, list2[7], 431, 0, list2[8], 430, 0)
    add_edge(matrix, list2[8], 430, 0, list2[9], 418, 0)
    add_edge(matrix, list2[9], 418, 0, list2[10], 416, 0)
    add_edge(matrix, list2[10], 416, 0, list2[11], 412, 0)
    add_edge(matrix, list2[11], 412, 0, list2[12], 407, 0)
    add_edge(matrix, list2[12], 407, 0, list2[13], 405, 0)
    add_edge(matrix, list2[13], 405, 0, list2[14], 397, 0)
    add_edge(matrix, list2[14], 397, 0, list2[15], 395, 0)
    add_edge(matrix, list2[15], 395, 0, list2[16], 329, 0)
    add_edge(matrix, list2[16], 329, 0, list2[17], 326, 0)
    add_edge(matrix, list2[17], 326, 0, list2[18], 323, 0)
    add_edge(matrix, list2[18], 323, 0, list2[19], 320, 0)
    add_edge(matrix, list2[19], 320, 0, list2[20], 318, 0)
    add_edge(matrix, list2[20], 318, 0, list2[21], 311, 0)
    add_edge(matrix, list2[21], 311, 0, list2[22], 309, 0)
    add_edge(matrix, list2[22], 309, 0, list2[23], 306, 0)
    add_edge(matrix, list2[23], 306, 0, list2[24], 302, 0)
    add_edge(matrix, list2[24], 302, 0, list2[25], 300, 0)
    add_edge(matrix, list2[25], 300, 0, list2[26], 298, 0)
    add_edge(matrix, list2[26], 298, 0, list2[27], 292, 0)
    add_edge(matrix, list2[27], 292, 0, list2[28], 288, 0)
    add_edge(matrix, list2[28], 288, 0, list2[29], 284, 0)
    add_edge(matrix, list2[29], 284, 0, list2[30], 280, 0)
    add_edge(matrix, list2[30], 280, 0, list2[31], 276, 0)
    add_edge(matrix, list2[31], 276, 0, list2[32], 275, 0)
    add_edge(matrix, list2[32], 275, 0, list2[33], 266, 0)
    add_edge(matrix, list2[33], 266, 0, list2[34], 253, 0)
    add_edge(matrix, list2[34], 253, 0, list2[35], 180, 0)
    add_edge(matrix, list2[35], 180, 0, list2[36], 174, 0)
    add_edge(matrix, list2[36], 174, 0, list2[37], 170, 0)
    add_edge(matrix, list2[37], 170, 0, list2[38], 166, 0)
    add_edge(matrix, list2[38], 166, 0, list2[39], 158, 0)
    add_edge(matrix, list2[39], 158, 0, list2[40], 151, 0)
    add_edge(matrix, list2[40], 151, 0, list2[41], 136, 0)
    add_edge(matrix, list2[41], 136, 0, list2[42], 128, 0)
    add_edge(matrix, list2[42], 128, 0, list2[43], 122, 0)
    add_edge(matrix, list2[43], 122, 0, list2[44], 117, 0)
    add_edge(matrix, list2[44], 117, 0, list2[45], 109, 0)
    add_edge(matrix, list2[45], 109, 0, list2[46], 100, 0)
    add_edge(matrix, list2[46], 100, 0, list2[47], 79, 0)
    add_edge(matrix, list2[47], 79, 0, list2[48], 70, 0)
    add_edge(matrix, list2[48], 70, 0, list2[49], 59, 0)
    add_edge(matrix, list2[49], 59, 0, list2[50], 50, 0)

    if (i == 0):
        add_edge(matrix, 135, 481, 0, 140, 481, 0)
        add_edge(matrix, 160, 50, 0, 115, 50, 0)
        draw_lines( matrix, screen, color )
        matrix = new_matrix(0, 0);
    else:
        color = [128, 128, 128]
        add_edge(matrix, 355, 481, 0, 360, 481, 0)
        add_edge(matrix, 380, 50, 0, 335, 50, 0)
        draw_lines( matrix, screen, color )

    for i in range(len(list1)):
        list1[i] += 220
    for i in range(len(list1)):
        list2[i] += 220

m2 = new_matrix(0, 0)
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = ")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print("\nTesting ident. m1 =")
m1 = ident(1)
print_matrix(m1)
print("\nTesting Matrix mult. m1 * m2 =")
m2 = matrix_mult(m1, m2)
print_matrix(m2)
print("\nTesting Matrix mult. m1 =")
m1 = new_matrix(0, 0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)
print("\nTesting Matrix mult. m1 * m2 =")
m2 = matrix_mult(m1, m2)
print_matrix(m2)

display(screen)
