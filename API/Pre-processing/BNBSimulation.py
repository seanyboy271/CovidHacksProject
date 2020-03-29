
import random
import numpy
import math

class VirusStrain:
    def __init__(self, birth, death, mut, startPop):
        self.birthRate = birth #this value is g
        self.deathRate = death #this value is gamma
        self.mutRate = mut #this value is mu
        if startPop == 1:
            self.population = 2
        else:
            self.population = startPop
        self.prevUpdateTime = 0
        self.updateMutTime = True
        self.randVal = random.uniform(0, 1)
        self.R = math.sqrt((self.birthRate - self.deathRate) ** 2 + (2 * self.birthRate + 2 * self.deathRate + self.mutRate) * self.mutRate)
        self.W = self.birthRate + self.deathRate + self.mutRate

        while 1:
            self.MutTimeCheck = ((self.R - self.W + 2*self.deathRate) / (self.R + self.W - 2*self.birthRate)) ** self.population
            if self.randVal > self.MutTimeCheck and self.randVal <= 1: #make this into a method for later iterations
                top = (self.randVal ** (1/self.population)) * (self.R - self.W + 2*self.birthRate) - self.W - self.R + 2*self.deathRate
                bottom = (self.randVal ** (1/self.population)) * (-1*self.R - self.W + 2*self.birthRate) - self.W + self.R + 2*self.deathRate
                self.nextMutTime = (1 / self.R) * numpy.log(top / bottom) #placeholder, replace with actual thing
                self.updateMutTime = False
                break
            else:
                self.randVal = random.uniform(0,1)

    def C(self, t):
        val = numpy.cosh(self.R * t / 2)
        return val

    def S(self, t):
        val = numpy.sinh(self.R * t / 2)
        return val

    def updateRandVal(self):
        self.randVal = random.uniform(0, 1)

    def updateNextMutTime(self):
        self.updateRandVal()
        self.MutTimeCheck = ((self.R - self.W + 2*self.deathRate) / (self.R + self.W - 2*self.birthRate)) ** self.population
        if self.randVal > self.MutTimeCheck and self.randVal <= 1: #make this into a method for later iterations
            top = (self.randVal ** (1/self.population)) * (self.R - self.W + 2*self.birthRate) - self.W - self.R + 2*self.deathRate
            bottom = (self.randVal ** (1/self.popultion)) * (-1*self.R - self.W + 2*self.birthRate) - self.W + self.R + 2*self.deathRate
            self.nextMutTime = (1 / self.R) * numpy.log(top / bottom) #placeholder, replace with actual thing
            self.updateMutTime = False
        else:
            self.nextMutTime = float("inf")
            self.updateMutTime = False

    def returnPm(self, currTime):
        top = (self.R*self.C(currTime)) + (2*self.deathRate*self.S(currTime)) - (self.W*self.S(currTime))
        bottom = (self.R*self.C(currTime)) - (2*self.birthRate*self.S(currTime)) + (self.W*self.S(currTime))
        return (top/bottom)

    def returnPe(self, currTime):
        top = self.deathRate * (1 - self.returnPm(currTime))
        bottom = self.W - self.deathRate - (self.birthRate * self.returnPm(currTime))
        return (top/bottom)

    def returnPb(self, currTime):
        val = self.returnPe(currTime) * (self.birthRate / self.deathRate)
        return val


class ViralSimulation:
    def __init__(self, time, birth, death, mut, startPop):
        self.end = time
        self.defBirth = birth
        self.defDeath = death
        self.defMut = mut
        self.currentTime = 0
        self.strainCount = 1
        self.strain = {
            str(self.strainCount): VirusStrain(self.defBirth, self.defDeath, self.defMut, startPop)
        }
    # to run simulation, use .runSim() method

    def updateTime(self):
        minTime = self.strain[list(self.strain.keys())[0]].nextMutTime
        minStrain = int(list(self.strain.keys())[0])
        for x in self.strain:
            if self.strain[x].nextMutTime < minTime:
                minTime = self.strain[x].nextMutTime
                minStrain = int(x)
        print("Here is minTime")
        print(minTime)
        self.currentTime += minTime
        return minStrain

    def updatePopulationMute(self, mutStrain):
        currStrain = self.strain[str(mutStrain)]
        tm = self.currentTime - currStrain.prevUpdateTime
        prob = 1-(currStrain.returnPe(tm) / currStrain.returnPm(tm))
        term = currStrain.population - 1
        binomM = numpy.random.binomial(term, prob)
        negBinomM = numpy.random.negative_binomial(binomM + 2, currStrain.returnPb(tm))
        print("here is binomM and negBinomM from mute")
        print(binomM)
        print(negBinomM)
        newPop = binomM + 1 + negBinomM
        currStrain.population = newPop
        currStrain.prevUpdateTime = self.currentTime
        self.strain[str(mutStrain)] = currStrain

    def updateOtherPopulation(self, mutStrain):
        for x in self.strain:
            if x == str(mutStrain):
                continue
            else:
                currStrain = self.strain[x]
                tm = self.currentTime - currStrain.prevUpdateTime
                prob = 1-(currStrain.returnPe(tm) / currStrain.returnPm(tm))
                term = currStrain.population
                binomM = numpy.random.binomial(term, prob)
                print("here is binomM and negBinomM from other")
                print(binomM)
                if binomM <= 0:
                    newPop = 0
                else:
                    negBinomM = numpy.random.negative_binomial(binomM, currStrain.returnPb(tm))
                    print(negBinomM)
                    newPop = binomM + negBinomM
                currStrain.population = newPop
                currStrain.previousUpdateTime = self.currentTime
                self.strain[x] = currStrain

    def generateNewStrain(self):
        self.strainCount += 1
        self.strain[str(self.strainCount)] = VirusStrain(self.defBirth, self.defDeath, self.defMut, 1)

    def checkExtinction(self):
        listRem = []
        for x in self.strain:
            if self.strain[x].population <= 0:
                listRem.append(int(x))
        listRem.sort(reverse=True)
        for x in listRem:
            self.strain.pop(str(x))

    def checkTime(self):
        if self.currentTime >= self.end:
            return True
        else:
            return False

    def runSim(self):
        loopDone = False
        while 1:
            mutStrain = self.updateTime()

            self.updatePopulationMute(mutStrain)

            self.updateOtherPopulation(mutStrain)

            self.generateNewStrain()

            self.checkExtinction()

            loopDone = self.checkTime()

            if loopDone:
                break
