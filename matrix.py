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
        m3 = new_matrix()
        r1=0
        c=0
        '''for r in range(len(m1)):
            s = r
            for c in range(len(m1[r])):
                newval = m1[f][s] + m2[s][f]
            m3[s][f]
        while r1 < len(m1):
            r2=0
            newval = 0
            while(r2 < len(m1[r1])):
                newval += m1[r1][r2] * m2[r2][r1]
                r2+=1
            m3[r1][c]= newval
            r1+=1
            c+=1'''
        for r1 in range(len(m1)):
            newval = 0
            for r2 in range(len(m1[r1])):
                newval += m1[r1][r2] * m2[r2][r1]
            m3[r1][c] = newval
            c+=1
        for y in range(len(m2)):
            for x in range(len(m2[y])):
                m2[y][x] = m3[y][x]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
