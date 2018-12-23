def square_of_sum(count):
    sub = 0
    for i in range(1, count+1):
        sub += i
    total = sub**2
    return total
    pass

def sum_of_squares(count):
    sub = 0 
    for i in range(1, count+1):
        sub += i**2
    return sub
    pass

def difference(count):
    return abs(square_of_sum(count) - sum_of_squares(count))
    
