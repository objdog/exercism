def on_square(integer_number):
    if integer_number <= 0 or integer_number > 64:
        raise ValueError("That square doesn't make any sense.")
    return 1 << (integer_number-1)

def total_after(integer_number):
    if integer_number <= 0 or integer_number > 64:
        raise ValueError("That square doesn't make any sense.")
    return (1 << integer_number) - 1