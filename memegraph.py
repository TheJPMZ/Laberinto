def get_cell_type (cell):
        
    type = ["⬛", "🏁"] if cell[0] <= 127 else ["🚩", "⬜"]
    
    return type[0] if cell[1] <= 127 else type[1] 

def get_color(type) -> tuple:
    colors: dict = {
        "⬛": (0,0,0),
        "⬜": (255,255,255),
        "🚩": (255,0,0),
        "🏁": (0,255,0)
    }
    return colors[type]


class Cell:
    
    def __init__(self, color, x, y):
        self.coords = (x,y)
        self.type = get_cell_type(color)
        self.color = get_color(self.type)
        self.neighbors = []
        self.heuristic = None
        
    def set_neighbors(self, matrix):
        x,y = self.coords
        if x > 0:
            self.neighbors.append(matrix[x-1][y])
        if x < len(matrix)-1:
            self.neighbors.append(matrix[x+1][y])
        if y > 0:
            self.neighbors.append(matrix[x][y-1])
        if y < len(matrix[x])-1:
            self.neighbors.append(matrix[x][y+1])
            
    def clear_walls(self):
        for neighbor in self.neighbors.copy():
            if neighbor.type == "⬛":
                self.neighbors.remove(neighbor)
    
    def distance(self, goal):
        return (((self.coords[0] - goal.coords[0])**2 + (self.coords[1] - goal.coords[1])**2)**0.5)           
    
    def set_heuristic(self, goal):
        self.heuristic = self.distance(goal)
    
    def set_heuristic2(self, goal):
        self.heuristic = self.distance(goal)/2

    def __repr__(self) -> str:
        return f"Cell({self.coords}, {self.type})"
        
class Graph:
    
    def __init__(self, matrix):
        self.goals = []
        self.matrix = matrix
        for x in matrix:
            for y in x:
                if y.type == "🚩":
                    self.initial = y
                if y.type == "🏁":
                    self.goals.append(y)
    
    def __getitem__(self, key):
        return self.matrix[key]