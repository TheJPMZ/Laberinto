from PIL import Image
import numpy as np
import graph_search
import pygame
from memegraph import Graph, Cell

point = input("Choose an image (1,2,3):")

images = {
    "1" : ("lab1.bmp",64*2),
    "2" : ("lab2.png",64*4),
    "3" : ("lab3.png",32),
}

def image_processing(image:str="lab1.bmp", size:int=64*2):
    img = Image.open(image)
    matrix = np.array(img)
    matrix = matrix.tolist() # Numpy array to normal array

    if len(matrix) != len(matrix[0]):
        raise Exception("Image must be squared")

    if len(matrix) < 2:
        raise Exception("Image must be bigger than 2x2")

    # if the image is bigger than 64x64, resize it
    if len(matrix) > size:
        print("Resizing image to 64x64...")
        img = img.resize((size,size))
        matrix = np.array(img)
        matrix = matrix.tolist()
    
    return matrix
    
def matrix_to_graph(matrix:list):
        
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

    print("Setting goals...")
    for x in graph.goals.copy():
        for y in graph.goals.copy():
            if x.distance(y) < 640/len(graph.matrix)*0.7 and x != y:
                y.type = "⬜"
                if len(graph.goals) > 1:
                    graph.goals.remove(y)
                break
    
    return graph

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
    
def draw_graph(graph):
    dim = len(graph.matrix)
    relation = 640/dim
    for x in range(dim):
        for y in range(dim):
            pygame.draw.rect(window, graph[x][y].color, (y*relation, x*relation, relation, relation))

def update_window():
    display.update()

graph = matrix_to_graph(image_processing(*images.get(point)))

goal_counter = 0
algorithm = 0
algo_list = ["A* with heuristic 1", "A* with heuristic 2", "BFS ~WARNING~ ", "DFS"]

"""Pygame rendering"""

display = pygame.display
display.init()
window = display.set_mode((640,640))

run = True
while run:
    
    draw_graph(graph)
    
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
            if event.key == pygame.K_r:
                graph = matrix_to_graph(image_processing(*images.get(point)))
                goal_counter = 0
                algorithm = 0
    
    update_window()
pygame.quit()