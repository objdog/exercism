def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
    
def largest_product(series, size):
    slices = []
    running_products = []
    if size < 0 or size > len(series):
        raise ValueError("Size should be greater than 0 and greater than the series")
    elif size == 0:
        return 1
    for index, element in enumerate(series):
        slices.append(series[index:index+size])
    slices = [item for item in slices if len(item) == size]
    for i in slices:
        working_scratch = []
        for c in i:
            working_scratch.append(int(c))
        running_products.append(multiply(working_scratch))
    return max(running_products)
 
