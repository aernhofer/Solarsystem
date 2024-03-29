__author__ = 'Andreas Ernhofer, Jakub Kopec'
"""
Erde
------------------------------------------------------------------------------------------
Hier sollen bestimmte Eigenschaften der Erde festgelegt werden.
"""
from FactoryPattern.Planet import Planet

class Uranus(Planet):

    def __init__(self,groesse = 1, rotationswinkel=[1,1],rotationspunkt=[0,0,0], position = [25,0,0],rotationsrichtung = [0,0,1],rotationsgeschwindigkeit = [-1,-1.5], textur = "uranus" ):
        super().__init__(groesse,rotationswinkel, rotationspunkt, position, rotationsrichtung, rotationsgeschwindigkeit, textur)