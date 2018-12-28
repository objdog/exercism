import re
def abbreviate(words):
    acro = ""
    for i in re.split(' |-|\n', words):
        try: 
            if i[0].isalpha():
                acro = acro + i[0].upper()
        except:
            pass
    return acro
