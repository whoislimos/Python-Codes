# Prints the sum of each digit
def digit_sum(n):
    # convert digit to string of characters
    characters = str(n)
    sum_of = 0
    for index in characters:
        sum_of = sum_of + int(index)
    return sum_of 
