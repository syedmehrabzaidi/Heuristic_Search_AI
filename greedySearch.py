'''
Created on Feb 25, 2019

@author: dr.aarij
'''
from com.search.strategy.searchStrategy import SearchStrategy
from queue import PriorityQueue

class GreedySearch(SearchStrategy):
    '''
    classdocs
    '''


    def __init__(self, heuristic):
        '''
        Constructor
        '''
        
        self.heuristic = heuristic
        self.queue = PriorityQueue()
        
    def isEmpty(self):        
        return self.queue == []

    def addNode(self,node):
        self.queue.put((self.heuristic.evaluateNode(node.state.currentState),node))

    def removeNode(self):
        return self.queue.get()[1]


    