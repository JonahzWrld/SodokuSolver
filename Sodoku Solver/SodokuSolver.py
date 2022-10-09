

# 1. solver will pick an empty square ( represented by 0 on board )
# 2. try all possible numbers for squard by checking surrounding squares
# 3. find number that works based on adjacent rows & columns
# 4. repeat for each square
# 5. backtrack to check if solver is correct


# sodoku solver board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty_square(bo)

    # base case of recursion
    # solution has been found
    if not find:
        return True
    else:
        row, col = find

    # loop values 1-9 to attempt to put into solution
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0    

    return False


# takes 3 parameters, board, number and position
def valid(bo, num, pos):
    
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False


    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # loop through all 9 elements in each box
    # make sure element isnt appearing twice
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):   
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True                     


# print board function
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") 

def find_empty_square(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:

                # i = row, j = column
                return (i, j)   

    return None

print_board(board)
print("-----------------------------------")
solve(board)
print_board(board)    