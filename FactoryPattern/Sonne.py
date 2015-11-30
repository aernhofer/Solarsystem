__author__ = 'jakubkopec'
"""
Sonne
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Sonne festgelegt werden.
"""
from FactoryPattern.Stern import Stern

from OpenGL.GL import *
from OpenGL.GLU import *

from Textur.Textur import Textur

class Sonne(Stern):

    def __init__(self, groesse = 3.5, position = [0,0,0],drehrichtung = [0,0,1],drehgeschwindigkeit = -0.3, textur = "sonne" ):
        super().__init__(groesse,position, drehrichtung, drehgeschwindigkeit, textur)