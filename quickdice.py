#A quick way to get DnD style dice rolls
import os
import random


#Call by roll(value, bool, bool)
#Dice size, Advantage, Disadvantage
class roll():
    
    def __init__(self, num, adv, dadv):
        self.adv = adv
        self.dadv = dadv


#If there is neither Advantage nor Disadvantage
        #if adv and dadv == False:
        ###I know there is prob a better way to do this
        if self.adv == False:
            if self.dadv == False:
                self.num = random.randint(1, num)
                print(self.num)
                if self.num == 20:
                    print("crit")


#If there is Advantage
        result = []
        if self.adv == True:
            for self.num in range(2):
                self.num = random.randint(1, num)  
                res = self.num
                result.append(res)
    #Print
            advantage = max(result)
            print("best")
            if advantage == 20:
                print("CRIT!!")
            print(advantage)
            

#If there is Disadvantage
        self.dadv = dadv
        result = []
        if self.dadv == True:
            for self.num in range(2):
                self.num = random.randint(1, num) 
                res = self.num
                result.append(res)
    #Print
            disadvantage = min(result)
            print("worst")
            if disadvantage == 20:
                print("CRIT!!")
            print(disadvantage)

                
roll(100, False, False)