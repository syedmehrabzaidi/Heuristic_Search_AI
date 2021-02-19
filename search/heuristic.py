'''
Created on Feb 25, 2019

@author: dr.aarij
'''
from abc import abstractclassmethod

class Heuristic(object):
    '''
    classdocs
    '''


    @abstractclassmethod
    def __init__(self): pass
    
    @abstractclassmethod
    def evaluateNode(self,state,goal): pass