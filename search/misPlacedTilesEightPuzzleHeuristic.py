'''
Created on Feb 25, 2019

@author: dr.aarij
'''
import heuristic

class MisPlacedTilesEightPuzzleHeuristic(heuristic.Heuristic):
    '''
    classdocs
    '''


    def __init__(self,goal):
        self.goal = goal
    
    def evaluateNode(self,state):
        totalCost = 0
        for i in range(len(state)):
                 if state[i][j] != self.goal[i][j]:
                    totalCost += 1 
        
        return totalCost
            
        