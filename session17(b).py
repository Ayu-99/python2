import numpy as np
board = np.zeros((8, 8))
print(board)

# 1. Creation of a Chess Board
for i in range(0, 8):
    for j in range(0, 8):

        board[i][j] = (i+j) % 2


print()
print()
print(board)

# 2. Place the no. of queens on the desired position
print()
l=[]
flag = True
print("Enter how many queens do u want to place:")
n = int(input())

for g in range(0, n):
    print("Enter the position:")
    p = input()
    x = int(p[0])
    y = int(p[2])
    i = x-1
    j = y-1
    k = x+1
    o = y+1
    # 3. Check whether a queen is placed in the diagonal where a queen is already existing
    # Lower Right Diagonal
    while k < 7 and o < 8:

        if board[k][o] == 9:
            flag = False
            print("Queen already existing in the lower right diagonal !!")
            break

        k = k + 1
        o = o + 1

    #  Upper Left Diagonal
    while i > 0 and j > 0:

        if board[i][j] == 9:
            flag = False
            print("Queen already existing in the upper left diagonal !!")
            break

        i = i-1
        j = j-1

    a = x-1
    b = y+1
    c = x+1
    d = y-1

    # Upper Right Diagonal
    while a >= 0 and b < 7:
        if board[a][b] == 9:
            flag = False
            print("Queen already existing in the upper right diagonal !!")
            break
        a = a-1
        b = b+1

    # Lower Left Diagonal
    while c < 7 and d >= 0:
        if board[c][d] == 9:
            flag = False
            print("Queen already existing in the lower left diagonal !!")
            break
        a = c + 1
        d = d - 1


    # 4.Check whether queen is placed in row or column where a queen is already existing
    if x in l :
        print("Already a queen in same row  !!")
        flag = False

    elif y in l:
        print("Already a queen in same column !!")
        flag = False
    else:
        #print("Can enter !!")
        #print(x)
        #print(y)
        board[x][y] = 9

        l.append(x)
        l.append(y)


    if flag == False:
        print("Cannot enter!!")
    else:
        print("Can enter!!")
        board[x][y] = 9



print()
print()
print(board)
