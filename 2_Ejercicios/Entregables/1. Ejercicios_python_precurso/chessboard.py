space = ' '
mat_8x8 = [[space for j in range(17)] for i in range(16)]
mat_8x8

for j in range(1,17,2):
    mat_8x8[0][j] = '_'

for i in range(1,9):
    for j in range(0,18,2):
        mat_8x8[i][j] = '|'
    for j in range(1,17,2):
        mat_8x8[i][j] = '_'

for line in mat_8x8:
    for it in line:
        print(it, sep = '', end = '')
    print(' ')
     