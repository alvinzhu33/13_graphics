from display import *
from draw import *

#Matrix Stuff
print("\nMatrix")
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
m2 = matrix_mult(m,m2)
print_matrix(m2)

print("--------------------------------------")
print("m3:")
m3 = [[0, 1 , 4], [2, 3, 5], [7, 8, 9]]
print_matrix(m3)
print("m4:")
m4 = [[0, 1 , 4], [2, 3, 5], [7, 8, 9]]
print_matrix(m4)
print("m4 scaled by 2:")
scalar_mult(m4, 2)
print_matrix(m4)
print("m3 x m4:")
m4 = matrix_mult(m3, m4)
print_matrix(m4)

print("--------------------------------------")

print("m5:")
m5 = [[0, 1 , 4, 10], [2, 3, 5, 11], [7, 8, 9, 12], [13, 14, 15, 16]]
print_matrix(m5)
print("m6:")
m6 = [[0, 1 , 4], [2, 3, 5], [7, 8, 9], [10, 11, 12]]
print_matrix(m6)
print("m6 scaled by 3:")
scalar_mult(m6, 3)
print_matrix(m6)
print("m5 x m6:")
m6 = matrix_mult(m5, m6)
print_matrix(m6)

print("--------------------------------------")

#Draw Stuff
print("\nDraw")
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_edge(matrix, 0, 10, 0, 10, 10, 0)
add_edge(matrix, 10, 0, 0, 10, 10, 0)

add_edge(matrix, 10, 0, 0, 20, 5, 0)
add_edge(matrix, 10, 10, 0, 20, 5, 0)
add_edge(matrix, 0, 10, 0, 5, 20, 0)
add_edge(matrix, 10, 10, 0, 5, 20, 0)
add_edge(matrix, 10, 10, 0, 20, 20, 0)

#print_matrix(matrix)
add_point(matrix, 0, 0)
add_point(matrix, 10, 10)
add_point(matrix, 0, 10)
add_point(matrix, 10, 0)
#print_matrix(matrix)
draw_lines( matrix, screen, color )
for x in range(10):
    scalar_mult(matrix, 2)
    draw_lines(matrix, screen, color)

display(screen)
