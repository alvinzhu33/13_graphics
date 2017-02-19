from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix)

ident(matrix)
print_matrix(matrix)

scalar_mult(matrix,4)
print_matrix(matrix)

matrix2 = new_matrix()
ident(matrix2)
scalar_mult(matrix2,5)
print_matrix(matrix2)

matrix_mult(matrix,matrix2)
print_matrix(matrix2)

#draw_lines( matrix, screen, color )
#display(screen)
