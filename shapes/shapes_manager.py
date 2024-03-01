from position import Position
from shapes.circle import circle
from shapes.rectangle import rectangle


class shapes_manager:
    def __init__(self) -> None:
        self.shapes_counter = 0
        self.shapes={}

    def add_circle(self,position: Position, color: str,radius:int=4):
        id =self.shapes_counter
        self.shapes[self.shapes_counter] = circle(id ,position=position,color=color,radius=radius)
        self.shapes_counter+=1
        return id 

    def add_square(self,position: Position, color: str,height:int=8,width:int=8):
        id =self.shapes_counter
        self.shapes[self.shapes_counter] = rectangle(id,position=position,color=color,height=height,width=width)
        self.shapes_counter+=1
        return id 