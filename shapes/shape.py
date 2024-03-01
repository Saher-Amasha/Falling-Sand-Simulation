from abc import abstractmethod
from position import Position


class Shape:
    def __init__(self,id,position:Position,color:str) -> None:
        self.id=id
        self.position=position
        self.color=color
    
    @abstractmethod
    def draw(self):
        pass