__author__ = 'jakubkopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Saturn(Planet):

    def __init__(self,groesse = 1.8, rotationswinkel=[50,1],rotationspunkt=[0,0,0], position = [18,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-1.3,-1.5], textur = "saturn" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)