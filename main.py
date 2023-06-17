"""
1. Write a Python script that builds Magic Squares.
Your script should:
● Allow the user to enter N through standard input, where N is any positive odd
integer
● Check that N is valid and prompt the user to enter another value for N if it is not
● Calculate a valid magic square for that value of N
● Print out the magic square, legibly
● Verify that the magic square is indeed valid
● Print “correct” if the verification step passes
"""


# the first function which will start the program by getting N from the user
def magic_square():
    # get N from user
    N = int(input("Enter a positive odd integer: "))

    # verification for positive odd integer
    while N % 2 == 0 or N <= 0:
        N = int(input("Ooops, please enter a positive odd integer: "))

    constant = calculate_magic_square(N)  # find the magic square
    print(f"Magic square is {constant}")
    print()
    my_2d_array = create_magic(N)  # creating matrix
    print_2d_array(my_2d_array)  # printing the matrix to the user
    print()

    magic_result = is_valid(my_2d_array)  # checking if magic square is valid
    return magic_result  # will return either True or False


# this function will check what the constant value for the magic square will be
def calculate_magic_square(N):
    constant = N * (N ** 2 + 1) / 2
    return constant


# this function will work through the main logic of magic squares
def create_magic(N):
    max_num = N ** 2  # magic square numbers go from 1 - n^2 so we need to find the max number
    my_2d_array = create_array(N)  # create a 2d array with rows and columns of size n
    num = 1  # will start at 1 and will iterate in a while loop until equal to max_num

    # getting position of first number
    # position_i (i) and position_j (j) are the coordinates for the matrix
    position_i, position_j = position_num_1(N)

    # storing first number
    my_2d_array[position_i][position_j] = num
    num += 1  # num is now at 2

    # storing the rest of the numbers, starting at 2, until max_num
    while num <= max_num:
        # get the new coordinates for i and j to slot in the next number
        position_i, position_j = next_num(N, position_i, position_j)

        # slotting num into array with the given coordinates
        position_i, position_j, my_2d_array = store_num(my_2d_array, position_i, position_j, num)
        num += 1

    return my_2d_array


# this function will return the co-ordinates of the first number(1) in the square
def position_num_1(N):
    # the coordinates for 1 will be found at -> (n / 2, n -1)
    position_i = N // 2  # we want the integer value
    position_j = N - 1
    return [position_i, position_j]  # position of the number 1


# this function will create the 2d array which will hold the magic squares
def create_array(n):
    my_2d_array = []

    for _ in range(n):
        row = [0] * n  # set each value to 0 as a placeholder for an empty slot on the matrix
        my_2d_array.append(row)

    return my_2d_array


# this function finds the co-ordinates of the next number
def next_num(N, position_i, position_j):
    # formula for next coordinates is (i-1, j + 1)
    position_i = position_i - 1  # i - 1
    position_j = position_j + 1  # j + 1

    # this section verifies that the current coordinates are valid and do not break any rules

    # if i is less than 0 and j is equal to N at the same time, this violates a rule
    if position_i == -1 and position_j == N:
        position_i = 0  # reset i to 0
        position_j = N - 2  # j becomes N -2
        return [position_i, position_j]

    #  if j is equal to N, this violates a rule
    elif position_j == N:
        position_j = 0  # reset j to 0
        return [position_i, position_j]

    # if i is less than 0, this violates a rule
    elif position_i == -1:
        position_i = N - 1  # i becomes N -1
        return [position_i, position_j]

    return [position_i, position_j]


# this function will check to see if the given co-ordinates have an empty slot or not
def store_num(my_2d_array, position_i, position_j, num):
    # checking to see if there is an empty slot at the given co-ordinates. Empty slot is identified with a 0
    if my_2d_array[position_i][position_j] == 0:
        my_2d_array[position_i][position_j] = num  # store number at the location
        return position_i, position_j, my_2d_array

    # this rule is triggered if the spot is taken
    else:
        position_i = position_i + 1  # i + 1
        position_j = position_j - 2  # j -2
        my_2d_array[position_i][position_j] = num  # store number at this new location
        return [position_i, position_j, my_2d_array]  # return i, j and the array


# this function will check if a magic square is valid.
def is_valid(magic_array):
    n = len(magic_array)
    # sum_d1 and sum_d2 will be the sum of the two diagonals
    sum_d1 = 0
    sum_d2 = 0

    for i in range(n):
        # (i, i) is the diagonal from top-left -> bottom-right
        # (i, n - i - 1) is the diagonal from top-right -> bottom-left
        sum_d1 += magic_array[i][i]
        sum_d2 += magic_array[i][n - i - 1]

        # if the two diagonal sums are unequal then it is not a magic square
    if sum_d1 != sum_d2:
        return False

    # now check if rows and columns are equal
    for i in range(n):
        # sum_r is the row sum and sum_c is column sum
        sum_r = 0
        sum_c = 0
        for j in range(n):
            sum_r += magic_array[i][j]
            sum_c += magic_array[j][i]
        if not sum_r == sum_c == sum_d1:
            return False
        # if all the conditions are satisfied then it is a magic square
    return True


# this function will display the magic squares legibly
def print_2d_array(my_2d_array):
    # Iterate over each row
    for row in my_2d_array:
        # Print the row as a string
        print(' '.join(str(element) for element in row))


result = magic_square()
if result is True:
    print("correct")

else:
    print("Not Valid")
