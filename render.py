from PIL import Image
import numpy as np
import graph_search
import pygame


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


img = Image.open('lab2.png')
matrix = np.array(img)
matrix = matrix.tolist() # Numpy array to normal array

if len(matrix) != len(matrix[0]):
    raise Exception("Image must be squared")

if len(matrix) < 2:
    raise Exception("Image must be bigger than 2x2")

# if the image is bigger than 64x64, resize it
size = 64
if len(matrix) > size:
    print("Resizing image to 64x64...")
    img = img.resize((size,size))
    matrix = np.array(img)
    matrix = matrix.tolist()
    

# Converting the array to a matrix of cells
print("Converting to matrix...")
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix[x][y] = Cell(matrix[x][y], x, y)

print("Setting neighbors...")
for x in matrix:
    for y in x:
        y.set_neighbors(matrix)
        y.clear_walls()

print("Creating graph...")
graph = Graph(matrix)

def get_path(graph, goal, search_algorithm):
    
    if search_algorithm == 1:
        for x in graph:
            for y in x:
                y.set_heuristic2(goal)
                
    if search_algorithm == 0:
        for x in graph:
            for y in x:
                y.set_heuristic(goal)
    
    print(search_algorithm%4)
    
    ala = graph_search.graph_search(graph, goal, search_algorithm%4)
    
    if not ala:
        raise Exception("No path found")

    for x in ala:
        x.color = (0,0,255)

    print("Done!")  
    
"""Pygame rendering"""

screen_size = 640
relation = 640/len(matrix)

display = pygame.display
display.init()
display.set_caption("Pathfinding")
window = display.set_mode((640,640))

def update_window():
    display.update()

def draw_graph():
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            pygame.draw.rect(window, graph[x][y].color, (y*relation, x*relation, relation, relation))





# Grouping goals together
for x in graph.goals.copy():
    for y in graph.goals.copy():
        if x.distance(y) < relation and x != y:
            y.type = "⬜"
            if len(graph.goals) > 1:
                graph.goals.remove(y)
            break
    
    




goal_counter = 0
algorithm = 0
algo_list = ["A* with heuristic 1", "A* with heuristic 2", "BFS", "DFS"]


run = True
while run:
    
    draw_graph()
    
    display.set_caption(
        f"Pathfinding - Algorithm: {algo_list[algorithm%4]} - Goal:{goal_counter%len(graph.goals)+1}"
    )
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Finding path...")
            get_path(graph, graph.goals[goal_counter%len(graph.goals)], algorithm%4)
            print("Done!")
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                algorithm += 1
            if event.key == pygame.K_SPACE:
                goal_counter += 1
    
    update_window()
pygame.quit()