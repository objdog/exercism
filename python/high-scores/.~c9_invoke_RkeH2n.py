class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    
    def highest(self):
        return self.scores.max
    
    def latest(self):
        return self.scores[-1]
        
    def personal_best(self):
        return self.scores.max
    
    def personal_top(self):
        best = []
        best.append(self.scores.max)
        s
