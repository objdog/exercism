def is_armstrong(number):
    exponent = len(str(number))
    digits = [int(i) for i in str(number)]
    product = 0
    for i in digits:
        product += i**exponent
    print(product)
    if product == number:
        return True
    else:
        return False
    
