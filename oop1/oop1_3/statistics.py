import math

class Stat:
    def average(self, scores):
        s = 0
        for score in scores:
            s += score
        return round(s/len(scores), 1)
        
    def variance(self, scores, avrg):
        s= 0
        for score in scores:
            s += (score - avrg) ** 2
        return round(s/len(scores), 1)

    def std_dev(self, variance):
        return round(math.sqrt(variance), 1)


