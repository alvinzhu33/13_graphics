from display import *
from draw import *

#Matrix Stuff
'''print("\nMatrix")
m = new_matrix()
m2 = new_matrix()

print("m:")
print_matrix(m)
print("m2:")
print_matrix(m2)

print("Identity m:")
ident(m)
print_matrix(m)
print("Scaling m by 4:")
scalar_mult(m,4)
print_matrix(m)

print("Identity m2:")
ident(m2)
print_matrix(m2)
print("Scaling m2 by 5:")
scalar_mult(m2,5)
print_matrix(m2)

print("Multiple m by m2:")
matrix_mult(m,m2)
print_matrix(m2)
'''
print("m3:")
m3 = [[0, 1, 2], [3, 4, 5]]
print_matrix(m3)
print("m4:")
m4 = [[0, 1], [2, 3], [4, 5]]
print_matrix(m4)
print("m4 x m3:")
matrix_mult(m4, m3)
print_matrix(m3)
#print("m3 x m4:")
#matrix_mult(m3, m4)
#print_matrix(m4)

'''
#Draw Stuff
print("\nDraw")
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_edge(matrix, 200, 200, 0, 300, 300, 0)
print_matrix(matrix)
add_point(matrix, 400, 400)
print_matrix(matrix)
draw_lines( matrix, screen, color )
#display(screen)'''
