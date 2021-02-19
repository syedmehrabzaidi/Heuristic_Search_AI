'''
Created on Feb 18, 2019

@author: dr.aarij
'''
import os
os.chdir("//10.0.0.3/Elibrary/Lectures/Duaa Baig/Spring 19/AI/Python/code/lab05/Search/Search/")
import node
import eightPuzzleProblem
import breadthFirstSearchStrategy

import misPlacedTilesEightPuzzleHeuristic
import greedySearch

class Search(object):
    '''
    classdocs
    '''


    def __init__(self, searchProblem, searchStrategy):
        '''
        Constructor
        '''
        self.searchProblem = searchProblem
        self.searchStrategy = searchStrategy
        self.nodeCount = 0
        
    def solveProblem(self):
        node = Node(self.searchProblem.initialState(), None, 0, 0, '')
        self.searchStrategy.addNode(node)
        
        duplicateMap = {}
        duplicateMap[node.state.stringRep()] = node.cost
        
        result = None
        
        while not  self.searchStrategy.isEmpty():

            self.nodeCount += 1
            currentNode = self.searchStrategy.removeNode()
            
            if self.searchProblem.isGoal(currentNode.state):
                result = currentNode
                break
            
            nextMoves = self.searchProblem.succesorFunction(currentNode.state)
            
            for nextState in nextMoves:
                if nextState.stringRep() not in duplicateMap:
                    newNode = Node(nextState, currentNode, currentNode.depth + 1, currentNode.cost + nextState.cost, nextState.action) 
                    self.searchStrategy.addNode(newNode)
                    duplicateMap[newNode.state.stringRep()] = newNode.cost    

                        
        return result
    
    def printResult(self,result):
        print("Total number of expanded nodes are : %d" % self.nodeCount)
        res = []
        while result is not None:
            res.insert(0, "Perform the following action %s,  New State is  %s,  cost is %d"%(result.action,result.state.getCurrentState(),result.cost))
            result = result.parentNode
        
        for x in res:
            print(x)

if __name__ == "__main__":

    goal = [[0,1,2],[3,4,5],[6,7,8]]
    heuristic = MisPlacedTilesEightPuzzleHeuristic(goal)
    searchProblem = EightPuzzleProblem([[0,8,7],[6,5,4],[3,2,1]], goal)
   #searchStrategy = BreadthFirstSearchStrategy()
   #searchStrategy = DepthFirstSearchStrategy()
    
   
    searchStrategy = GreedySearch(heuristic)
    
    search = Search(searchProblem, searchStrategy)
    result = search.solveProblem()
    if result is not None:
        search.printResult(result)
        