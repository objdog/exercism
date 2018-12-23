to_strip = ['@','#','$','%','^','&','*','(',')','+','=','[',']','{','}','|',';',':','<','>']

def hey(phrase):
    if phrase.strip().endswith('?'):
        return is_question(phrase)
    elif blank(phrase):
        return "Fine. Be that way!"
    elif phrase.upper() == phrase and phrase.replace(' ','').replace(',','').isdigit() != True:
        return "Whoa, chill out!"
    else:
        return "Whatever."
        
def blank(phrase):
    if phrase.isspace() or len(phrase) == 0:
        return True
    
def is_question(phrase):
    for c in phrase:
        if c in to_strip:
            return "Sure."
    else:
        if phrase.upper() == phrase and phrase.strip('?').isdigit() != True:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."




