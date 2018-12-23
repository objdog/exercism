def prime_factors(natural_number):
    result = []

    while natural_number > 1:    
        divisor = 2
        while divisor <= natural_number:
            if natural_number % divisor ==0:
                result.append(divisor)
                natural_number = natural_number / divisor
                prime = False
            else:
                divisor += 1

    return result
    
    
            
    
