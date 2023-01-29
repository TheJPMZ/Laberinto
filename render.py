from PIL import Image
import numpy as np


CELLS = {
    (0,0,0) : "wall",
    (255,255,255) : "path",
    (255,0,0) : "start",
    (0,255,0) : "end",
}


def get_cell_type (cell):
    
    CELLS = {
        (0,0,0) : "⬛",
        (255,255,255) : "⬜",
        (255,0,0) : "🚩",
        (0,255,0) : "🏁",
    }
    
    return CELLS.get(tuple(cell), "⬜")


img = Image.open('a.png')


matrix = np.array(img)

# Numpy array to normal array
matrix = matrix.tolist()



for x in matrix:
    for y in x:
        print(get_cell_type(y), end="")
    print("\n")