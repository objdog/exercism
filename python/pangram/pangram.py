def is_pangram(sentence):
    result = True
    check = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for c in check:
        if c in sentence.lower():
            result = True
        else:
            result = False
            return result
    return result
    
    
