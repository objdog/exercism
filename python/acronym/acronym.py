import re
def abbreviate(words):
    acro = []
    for i in re.findall(r"[A-Za-z\']+", words):
        if i[0].isalpha():
            acro.append(i[0])
    return ''.join(acro).upper()
