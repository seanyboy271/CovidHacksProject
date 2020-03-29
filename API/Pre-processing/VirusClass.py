import random
import numpy

class VirusStrain:
    def __init__(self, birth, death, mut):
        self.birthRate = birth #this value is g
        self.deathRate = death #this value is gamma
        self.mutRate = mut #this value is mu
        self.updateMutTime = True
        self.randVal = random.uniform(0, 1)
        self.R = sqrt((self.birthRate - self.deathRate) ** 2 + (2 * self.birthRate + 2 * self.deathRate + self.mutRate) * self.mutRate)
        self.W = self.birthRate + self.deathRate + self.mutRate
        #Whenever you see a C(t) in the formula, that is numpy.cosh(self.R * t / 2)
        #Whenever you see a S(t) in the formula, that is numpy.sinh(self.R * t / 2)
        self.MutTimeCheck = ((self.R - self.W + 2*self.deathRate) / (self.R + self.W - 2*self.birthRate))
        if self.randVal > self.firstMutTimeCheck and self.randVal <= 1: #make this into a method for later iterations
            self.nextMutTime = 0 #placeholder, replace with actual thing
            self.updateMutTime = False
        else:
            self.nextMutTime = float("inf")
            self.updateMutTime = False

    def updateRandVal(self):
        self.randVal = random.uniform(0, 1)

    def updateNextMutTime(self):
        
