'''
Created on Feb 17, 2019

@author: Aarij Mahmood
'''
from abc import abstractmethod

class SearchProblem(object):

    @abstractmethod
    def __init__(self, params):pass
    
    @abstractmethod
    def initialState(self): pass
    
    @abstractmethod
    def succesorFunction(self,currentState): pass
    
    @abstractmethod
    def isGoal(self,currentState): pass
    
    @abstractmethod
    def __str__(self) : pass
        
        
        