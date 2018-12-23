import random
import string
historic_names = []
class Robot(object):
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = ''.join(random.choice(string.ascii_letters).upper() for x in range(2)) + str(random.randrange(100, 999))
        while self.name in historic_names:
            self.name = ''.join(random.choice(string.ascii_letters).upper() for x in range(2)) + str(random.randrange(100, 999))
        historic_names.append(self.name)