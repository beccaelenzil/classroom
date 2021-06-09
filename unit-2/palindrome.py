def is_palindrome(string):
    n = len(string)
    i = 0
    j = n-1
    half = n//2
    for i in range(half):
        # check if mirroring spots are equal
        if string[i] != string[n-i-1]:
            return False
        i += 1
    return True

print(is_palindrome('mom'))
print(is_palindrome('moam'))
print(is_palindrome('apple'))