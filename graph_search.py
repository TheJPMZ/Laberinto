


def graph_search(graph, goal):
    caminos = [graph.initial]
    explored = []
    
    while True:
        
        if not caminos: #Si no hay mas caminos
            return False
            
        current_path = 1
        node = current_path[-1]
        explored.append(node)
        
        if node == goal: #Si el nodo es el objetivo
            return current_path
        
        for new in graph.actions:
            result = graph.move(node,new)
            
            if result not in explored:
                new_path = current_path + [new]
                caminos.append(new_path)

                