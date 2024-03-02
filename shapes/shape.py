from abc import abstractmethod
from position import Position


class Shape:
    """
    Abstract shape class
    """
    def __init__(self,shape_id,position:Position,color:str) -> None:
        self.shape_id=shape_id
        self.position=position
        self.color=color

    @abstractmethod
    def draw(self,window):
        """
        Abstract Draw method
        """

    def __str__(self) -> str:
        return str(self.position)
