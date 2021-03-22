# accept a variable number of positional parameters
def input_int(*args):
    # loop forever (until we get valid input)
    while True:
        # get string input
        user_input = input(*args)
        try:
            # try converting to an int (will return if successful)
            return int(user_input)

            # if the conversion succeeded, we will have returned already
        except ValueError:
            # could not convert the input, so show an error message
            print('Try again.')

def silly_sum():
    # initialize values
    sum = 0
    num = "hello, world"

    # ask for input until sum < 1000 and num != 0
    while sum < 1000 and num != 0:
        num = input_int("Give me a number! ")
        sum += num

    # return sum

silly_sum()

