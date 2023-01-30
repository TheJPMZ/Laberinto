
def breath_first_search(caminos):
    return caminos.pop(0)
    
    
def depth_first_search(caminos):
    return caminos.pop()
    
def a_star_search(caminos):
    road = (min(caminos, key=lambda x: x[-1].heuristic))
    caminos.remove(road)
    return road
    
    

def graph_search(graph, goal, search_algorithm=1):
    caminos = [[graph.initial]]
    explored = []
    
    while True:
        
        if not caminos: #Si no hay mas caminos
            return False
            
        current_path = a_star_search(caminos) if search_algorithm == 1 else breath_first_search(caminos) if search_algorithm == 2 else depth_first_search(caminos)
        node = current_path[-1]
        explored.append(node)
        
        if node == goal: #Si el nodo es el objetivo
            return current_path
        
        for new in node.neighbors:
           
            if new not in explored:
                new_path = current_path + [new]
                caminos.append(new_path)

                