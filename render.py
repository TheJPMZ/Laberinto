from PIL import Image
import numpy as np
import graph_search

def get_cell_type (cell):
    
    CELLS = {
        (0,0,0) : "⬛",
        (255,255,255) : "⬜",
        (255,0,0) : "🚩",
        (0,255,0) : "🏁",
    }
    
    return CELLS.get(tuple(cell), "⬜")

class Cell:
    
    def __init__(self, color, x, y):
        self.coords = (x,y)
        self.color = color
        self.type = get_cell_type(color)
        self.neighbors = []
        
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
        for neighbor in self.neighbors:
            if neighbor.type == "⬛":
                self.neighbors.remove(neighbor)

    def __repr__(self) -> str:
        return f"Cell({self.coords}, {self.type})"
        
class Graph:
    
    def __init__(self, matrix):
        self.goals = []
        for x in matrix:
            for y in x:
                if y.type == "🚩":
                    self.initial = y
                if y.type == "🏁":
                    self.goals.append(y)


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

ala = graph_search.graph_search(graph, graph.goals[0])
for x in ala:
    x.type = "🔽"


for x in matrix:
    for y in x:
        print(y.type, end=" ")
    print()