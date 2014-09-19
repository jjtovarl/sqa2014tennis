# -*- coding: utf-8 -*-
class Match:
    def __init__(self,player1,player2,pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.count_p1 = 0
        self.count_p2 = 0
        self.score_p1 = ['', '', '', '', '']
        self.score_p2 = ['', '', '', '', '']
        self.points = ""

    def score(self):
    	if self.count_p1 == 0 and self.count_p2 == 0:
    		return "{0} plays with {1} | 0-0".format(self.p1,self.p2)
    	elif self.count_p1 > self.count_p2:
    		return "{0} defeated {1} | {2}".format(self.p1, self.p2, self.scores(self.p1))
    	else:
    		return "{0} defeated {1} | {2}".format(self.p2, self.p1, self.scores(self.p2))

    def anotar(self,player,num,n1,n2):
    	if player == self.p1:
    		self.count_p1 += 1
    		self.score_p1[num - 1] = n1
    		self.score_p2[num - 1] = n2
    	else:
    		self.count_p2 += 1
    		self.score_p1[num - 1] = n2
    		self.score_p2[num - 1] = n1

    def scores(self, player):
    	points = ""
    	total = self.count_p1 + self.count_p2
    	i = 0

    	while i < total:
    		if player == self.p1:
    			points += str(self.score_p1[i]) + "-" + str(self.score_p2[i]) + ", "
    		else:
    			points += str(self.score_p2[i]) + "-" + str(self.score_p1[i]) + ", "
    		i += 1
    	return points[:-2]
