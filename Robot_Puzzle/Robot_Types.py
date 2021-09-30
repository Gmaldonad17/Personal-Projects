#types Format: Type, Speed, Dexterity
types = [['Unipedal'    , 1, 2],
         ['Bipedal'     , 2, 2],
         ['Quadrupedal' , 4, 1],
         ['Arachnid'    , 8, 1],
         ['Radial'      ,10, 0],
         ['Aeronautical', 0, 4]]

class Robot():
    def __init__(self, name, type):
        self.name = name
        self.task = 3
        self.type = types[type]