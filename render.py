from PIL import Image
import numpy as np
import graph_search

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


img = Image.open('a.png')


matrix = np.array(img)

# Numpy array to normal array
matrix = matrix.tolist()

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix[x][y] = Cell(matrix[x][y], x, y)

for x in matrix:
    for y in x:
        y.set_neighbors(matrix)
        y.clear_walls()


for x in matrix:
    for y in x:
        print(y.type, end=" ")
    print()
    

graph = Graph(matrix)

for x in graph:
    for y in x:
        y.set_heuristic(graph.goals[0])

ala = graph_search.graph_search(graph, graph.goals[0])
# TODO: No path found
for x in ala:
    x.color = (0,0,255)


for x in matrix:
    for y in x:
        print(y.type, end=" ")
    print()
    
    
    
    
    

screen_size = 640
relation = 640/len(matrix)
    
#Screen


import pygame
display = pygame.display
pygame.display.init()
pygame.display.set_caption("Pathfinding")
window = pygame.display.set_mode((640,640))

def update_window():
    display.update()

def draw_grid():
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            pygame.draw.rect(window, graph[x][y].color, (y*relation, x*relation, relation, relation))
            
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_grid()
    
    update_window()
pygame.quit()