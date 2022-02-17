'''
Created on 23 avr. 2019

@author: gtexier
'''
from enum import IntEnum, unique

@unique
class Orientation(IntEnum):
    '''
    Name of the directions used during the robot moves
    '''
    WEST = 1
    NORTH = 2
    EAST = 3
    SOUTH = 4

def inverse_direction(dir):
    '''
    Returns the inverse of the direction dir
    Parameters:
        dir: the direction to be inverted
    '''
    # Ajoutez le code pour renvoyer la direction opposee a dir
    pass

def get_left(dir):
    '''
    Returns the next direction when we are in direction dir and turn left
    Parameters:
        dir: the initial direction (before going left)
    '''
    # Ajoutez le code pour renvoyer la direction dans laquelle le robot sera
    # apres avoir tourne a gauche
    pass

def get_right(dir):
    '''
    Returns the next direction when we are in direction dir and turn right
    Parameters:
        dir: the initial direction (before going right)
    '''
    # Ajoutez le code pour renvoyer la direction dans laquelle le robot sera
    # apres avoir tourne a droite
    pass

class OrientationError(Exception):
    pass
