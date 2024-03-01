import pygame
from grid import Grid
from position import Position
from shapes.shapes_manager import shapes_manager
import random

class Game:
    def __init__(self,height:int,width:int,caption:str = "Falling Sand") -> None:
        pygame.init()
        self.shape_width = 8
        self.pixel_height = height*self.shape_width
        self.pixel_width = width*self.shape_width
        self.window  = pygame.display.set_mode((self.pixel_width, self.pixel_height))
        pygame.display.set_caption(caption)

        
        self.height = height
        self.width = width

        self.grid=Grid(height=self.height,width=self.width)
        self.shapes_manage=shapes_manager()

    def assign_random(self):
        
        # Add shapes randoly on screen
        for _ in range(5000):
            self.add_square(position=Position(
                        x=random.randint(random.randint(1,26),self.width -random.randint(1,26) ),
                        y=random.randint(1, random.randint(1,60))
                    )                    ,color=(
                        random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255)
                        ))
            self.add_circle(position=Position(
                        x=random.randint(random.randint(1,26),self.width -random.randint(1,26) ),
                        y=random.randint(1, random.randint(1,60))
                    )
                    ,color=(
                        random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255)
                        )
                    )

    def add_circle(self,position:Position,color):
        if self.grid.get_at_pos(position) == -1:
            id = self.shapes_manage.add_circle(position,color)
            self.grid.set_at_pos(position=position,val=id)

    def add_square(self,position:Position,color):
        id = self.shapes_manage.add_square(position,color)
        self.grid.set_at_pos(position=position,val=id)

    def _advance(self,x,y):
        if self.grid.get_at_pos(Position(x=x,y=y)) != -1 :
                    below = (x,y+1)
                    current = (x,y)
                    current_val = self.grid.get_at_pos(Position(*current))
                    if self.grid.get_at_pos(Position(*below)) == -1:
                        self.shapes_manage.shapes[current_val].position= Position(*below)
                        self.grid.set_at_pos(Position(*below),current_val)
                        self.grid.set_at_pos(Position(*current),-1)
                        return
                    
                    botom_right = (x+1,y+1)
                    if x <self.width -1 and self.grid.get_at_pos(Position(*botom_right))== -1:
                        self.shapes_manage.shapes[current_val].position= Position(*botom_right)
                        self.grid.set_at_pos(Position(*botom_right),current_val)
                        self.grid.set_at_pos(Position(*current),-1)
                        return    
                    botom_left = (x-1,y+1)
                    if x >1 and self.grid.get_at_pos(Position(*botom_left))== -1:
                        self.shapes_manage.shapes[current_val].position= Position(*botom_left)
                        self.grid.set_at_pos(Position(*botom_left),current_val)
                        self.grid.set_at_pos(Position(*current),-1)
    def tick(self):
        [self._advance(x,y) for y in range(self.height-2,0,-1) for x in range(self.width-1,0,-1)]
                

    def draw(self):
        self.window.fill("black")
        if self.grid.changed:
            for x in range(self.width):
                for y in range(self.height):
                    shape_id = self.grid.get_at_pos(Position(x=x,y=y))
                    if shape_id != -1:
                        self.shapes_manage.shapes[shape_id].draw(self.window)
            pygame.display.update()
            self.grid.change_handeled()
    def game_loop(self):
        run = True
        pressed= False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    pressed = False
                    
                if event.type == pygame.QUIT:
                    run =False
            if pressed:
                if random.randint(0,1) == 0:
                    draw =self.add_circle
                else:
                    draw = self.add_square
                draw(Position(*event.dict['pos']).to_grid_pos(self.shape_width),color=(
                            random.randint(0,255),
                            random.randint(0,255),
                            random.randint(0,255)
                            ))
                    
            self.draw()
            self.tick()
        pygame.quit()
