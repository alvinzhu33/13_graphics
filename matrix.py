import math


def print_matrix( matrix ):
    printing = "";
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            printing+=(str)(matrix[y][x]) + "\t"
        printing+="\n"
    print(printing)

def ident( matrix ):
    for y in range(len(matrix)):
        for x in range (len(matrix[y])):
            if x == y:
                matrix[y][x]=1
            else:
                matrix[y][x]=0

def scalar_mult( matrix, s ):
    for y in range(len(matrix)):
        for x in range (len(matrix[y])):
            matrix[y][x]=matrix[y][x]*s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if(len(m1[0])==len(m2)):
        m3 = new_matrix(len(m1), len(m2[0]))
        for r1 in range(len(m1)):
            #y = r1
            for c2 in range(len(m2[0])):
                newval = 0
                #x = c2
                for r in range(len(m2)):
                        newval += m1[r1][r] * m2[r][c2]
                m3[r1][c2] = newval
        return m3



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( rows ):
        m.append( [] )
        for r in range( cols ):
            m[c].append( 0 )
    return m
