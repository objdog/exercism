def is_leap_year(year):
    if year % 2 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else: 
        return False
        
