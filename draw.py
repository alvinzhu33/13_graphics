from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for i in range(0, len(matrix[0])-1, 2):
        draw_line(matrix[0][i], matrix[1][i], matrix[0][i+1], matrix[1][i+1], screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    key = [x0, x1, y0, y1, z0, z1, 1, 1]
    for i in range(len(matrix)):
        matrix[i].append(key[2*i])
        matrix[i].append(key[2*i+1])
    '''matrix[0].append(x0)
    matrix[0].append(x1)
    matrix[1].append(y0)
    matrix[1].append(y1)
    matrix[2].append(z0)
    matrix[2].append(z1)
    matrix[3].append(1)
    matrix[3].append(1)'''

def add_point( matrix, x, y, z=0 ):
    key = [x, y, z, 1]
    for i in range(len(matrix)):
        matrix[i].append(key[i])
        matrix[i].append(key[i])




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
