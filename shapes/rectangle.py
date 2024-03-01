import pygame
from position import Position
from shapes.shape import Shape


class rectangle(Shape):
    def __init__(self, id, position: Position, color: str,height:int,width:int) -> None:
        super().__init__(id, position, color)
        self.width=width
        self.height=height
    def draw(self,window):
        return pygame.draw.rect(window,self.color, (self.position.x*8, self.position.y*8, self.width, self.height))