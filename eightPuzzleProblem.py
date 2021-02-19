'''
Created on Feb 17, 2019

@author: Aarij Mahmood
'''

from com.search.searchProblem import SearchProblem
import copy
from com.search.eightPuzzleState import EightPuzzleState


class EightPuzzleProblem(SearchProblem):
    '''
    classdocs
    '''

    def __init__(self, initialState,goalState):
        '''
        Constructor
        '''
        self._initialState = EightPuzzleState(initialState, '', 0) 
        self._goalState = goalState
        self._numberOfRows = len(initialState)
        self._numberOfColumns = len(initialState[0])
        
    def initialState(self):
        return self._initialState
    
    def succesorFunction(self,cs): 
        nextMoves = []
        emptyRow,emptyColumn = 0,0
        currentState = cs.currentState
        
        emptyFound = False
        
        for i in range(len(currentState)):
            for j in range(len(currentState[i])):
                if currentState[i][j] == 0:
                    emptyRow,emptyColumn = i,j
                    emptyFound = True
                    break
            if emptyFound:
                break
            
        #check up move
        if emptyRow != 0:
            newState = copy.deepcopy(currentState)
            tempS = newState[emptyRow-1][emptyColumn]
            newState[emptyRow-1][emptyColumn] = 0
            newState[emptyRow][emptyColumn] = tempS
            ep = EightPuzzleState(newState, 'Move Up', 1.0)
            nextMoves.append(ep) 
        
        #check down move
        if emptyRow + 1 != self._numberOfRows:
            newState = copy.deepcopy(currentState)
            tempS = newState[emptyRow + 1][emptyColumn]
            newState[emptyRow + 1][emptyColumn] = 0
            newState[emptyRow][emptyColumn] = tempS
            ep = EightPuzzleState(newState, 'Move Down', 1.0)
            nextMoves.append(ep)
        
        #check left move
        if emptyColumn != 0:
            newState = copy.deepcopy(currentState)
            tempS = newState[emptyRow][emptyColumn-1]
            newState[emptyRow][emptyColumn-1] = 0
            newState[emptyRow][emptyColumn] = tempS
            ep = EightPuzzleState(newState, 'Move Left', 1.0)
            nextMoves.append(ep)
        
        #check right move
        if emptyColumn +1 != self._numberOfColumns:
            newState = copy.deepcopy(currentState)
            tempS = newState[emptyRow][emptyColumn+1]
            newState[emptyRow][emptyColumn+1] = 0
            newState[emptyRow][emptyColumn] = tempS
            ep = EightPuzzleState(newState, 'Move Right', 1.0)
            nextMoves.append(ep)
            
        return nextMoves
    
    def isGoal(self,currentState):
        cs = currentState.getCurrentState()
        for i in range(len(cs)):
            for j in range(len(cs[i])):
                if cs[i][j] != self._goalState[i][j]:
                    return False
        return True