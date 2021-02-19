'''
Created on Feb 18, 2019

@author: dr.aarij
'''
from abc import abstractmethod

class SearchState(object):
    '''
    classdocs
    '''


    @abstractmethod
    def __init__(self, params): pass
    
    @abstractmethod
    def getCurrentState(self): pass
    
    @abstractmethod
    def getAction(self): pass
    
    @abstractmethod
    def getCost(self):pass
    
    @abstractmethod
    def stringRep(self) : pass
