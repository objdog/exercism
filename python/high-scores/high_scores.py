class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        return self.scores[-1]
        
    def personal_best(self):
        return max(self.scores)
    
    def personal_top(self):
        top = []
        if len(self.scores) < 3:
            return sorted(self.scores, reverse=True)
        else:
            top.append(max(self.scores))
            self.scores.remove(max(self.scores))
            top.append(max(self.scores))
            self.scores.remove(max(self.scores))
            top.append(max(self.scores))
        return top
        
    def report(self):
        if self.scores[-1] == max(self.scores):
            return "Your latest score was " + str(max(self.scores)) + ". That's your personal best!"
        else:
            return "Your latest score was " + str(self.scores[-1]) + ". That's " + (str(max(self.scores) - self.scores[-1])) + " short of your personal best!"
           