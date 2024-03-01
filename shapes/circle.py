import pygame
from position import Position
from shapes.shape import Shape


class circle(Shape):
    def __init__(self, id, position: Position, color: str,radius:int) -> None:
        super().__init__(id, position, color)
        self.radius=radius
    
    def draw(self,window):
        return pygame.draw.circle(window,self.color,(self.position.x*8,self.position.y*8),self.radius)