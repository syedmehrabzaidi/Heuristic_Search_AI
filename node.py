'''
Created on Feb 17, 2019

@author: Aarij Mahmood
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, state, parentNode=None,depth=0,cost=0,action=''):
        '''
        Constructor
        '''
        self.state = state
        self.parentNode = parentNode
        self.depth =depth
        self.cost = cost
        self.action = action
    
    def __str__(self) :
        return self.state + " -- "+self.action+" -- "+self.cost
    
    def __gt__(self, other):
        return self.cost > other.cost