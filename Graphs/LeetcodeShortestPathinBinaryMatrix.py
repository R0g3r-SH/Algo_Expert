#BFS

from collections import deque
from this import s
from tkinter import Grid
from typing import Deque
# N times N time complexiti 
#BFS Breadth First Search 0(V+E) Vertices + Edges
#finding a shortest Path 
#neigbords nodedes first 

def shortestPath(grid):
    # m= 3 N =4
    M,N =len(grid),len(grid[0])
    visited = set()
    #0(1) Time complexiti for append and pop operations compared to a list
    q = deque()
    dirs = [(0,1),(0,-1),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
    if grid[0][0]==0:
        q.append((1,(0,0)))
        visited.add((0,0))
    while q:
        steps,tmp = q.popleft()
        r,c = tmp[0],tmp[1]
        if (r,c) == (M-1,N-1):
            return steps
        for i,j in dirs:
            new_r,new_c = r+i ,c+j
            #in bounce we habven vitede befopre
            if 0<=new_r<M and 0<=new_c<N and  grid[new_r][new_c] == 0 and(new_r,new_c) not in visited:
                q.append((steps+1,(new_r,new_c)))
                visited.add((new_r,new_c))
    return -1


grid = [[0,1,1,0,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [1,0,1,1,0],
        [1,1,1,1,0]]

print(shortestPath(grid))
