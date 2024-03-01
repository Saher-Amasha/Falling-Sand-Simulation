from position import Position


class Grid:
    def __init__(self,height:int,width:int) -> None:
        self.height = height
        self.width = width
        self.num_values = width * height
        self.grid = [-1 for _ in range(self.num_values)]
        self.changed = True

    def get_at_pos(self,position:Position)->int:
        return self.grid[position.x+position.y*self.width]
    
    def set_at_pos(self,position:Position,val:int):
        self.changed = True
        self.grid[position.x+position.y*self.width]=val
    
    def change_handeled(self):
        self.changed=False

    def __str__(self) -> str:
        grid=[]
        for val in range(0,self.num_values,self.width):
            grid.append(str(self.grid[val:val+self.width]))
            grid.append('\n')
        return ''.join(grid)