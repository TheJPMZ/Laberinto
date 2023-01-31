# Graph search algorithms [JPMZ]

This is a simple implementation of graph search algorithms in Python. The algorithms are implemented in a generic way, so they can be used for any graph. The `graph` is represented as an array where each individual node is a `Cell`. 

Each `Cell` has a list of `Cell`s that are its neighbors. The `Cell` class is defined in `memegraph.py`.

## Usage
To run the program you need to have Python 3 installed, with `PIL`, `pygame` and `numpy` installed. Then, run the following command:
```bash
py render.py
```
for installing the dependencies, run:
```bash
pip install -r requirements.txt
```

## Instructions
The program can read an image containing a maze-like puzzle, then it will open a window with a grid of `Cell`s. The `Cell`s are colored based on their state. It works with any square image, but to work it needs to have the following colors:

* ⬜ White: path
* ⬛ Black: wall
* 🟥 Red: start
* 🟩 Green: goal
* 🟦 Blue: visited

Then you can select the algorithm you want to use and the program will show the path from the start to the goal when pressing `click`.

## Controls
* `click`: Find path with the selected algorithm
* `tab`: Change algorithm
* `space`: Change goals
* `r`: Reset the grid
![imagen](https://user-images.githubusercontent.com/64183934/215688776-7b13495c-b2b4-428d-a3fa-0fd8f9d088f2.png)

## Algorithms
All of the following algorithms take a `Graph` and a goal `Cell` as input. They return a list of `Cells` that represent the path from the start `Cell` to the goal `Cell`. If no path is found, an exception is raised.

### Breadth-first search
It travels the graph in a breadth-first manner, prioritizing the neighbors of the current `Cell` over the neighbors of the neighbors.

### Depth-first search
It travels the graph in a depth-first manner, prioritizing traveling down the current path before exploring other paths.

### A*
It uses a heuristic to prioritize the neighbors of the current `Cell` based on their distance to the goal `Cell`. There are two heuristics implemented.

## Examples
This are examples of the capabilities of the software. 

### Using A* with the "pythagorean" heuristic.
![imagen](https://user-images.githubusercontent.com/64183934/215688859-de43d6bd-8a82-4f6d-9ee0-cf4eb7ed48dd.png)

### Using Depth-first search.
![imagen](https://user-images.githubusercontent.com/64183934/215688884-cfc6ff79-20b4-4bc3-ba84-8d0782410606.png)

### Using Breadth-first search.
Using a different maze because of the rendering time of BFS
![imagen](https://user-images.githubusercontent.com/64183934/215688962-8773e948-bc09-4842-a517-4f440335c4b5.png)
