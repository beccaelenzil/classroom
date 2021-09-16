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

    sum = 0
    num = "hello, world"

    # keep asking for a number until the the sum is greater than 1000 or the number is 0
    while sum < 1000 and num != 0:
        num = input_int("Give me a number! ")
        sum = num
        
    return sum

sum = silly_sum()


   