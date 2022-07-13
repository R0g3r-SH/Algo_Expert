
# Time Complexity us MxN

def markiland(grid,x,y,r,c) :
    if x<0 or x>=r or y<0 or y>=c or grid[x][y]!="1":
        return 
    grid[x][y] = "2" 
    markiland(grid,x+1,y,r,c) 
    markiland(grid,x,y+1,r,c) 
    markiland(grid,x-1,y,r,c) 
    markiland(grid,x,y-1,r,c) 

def numberOfIlands(grid):
    row = len(grid)
    if (row ==0):
        return 0
    cols = len(grid[0])
    count = 0
    for i in range(row):
        for j in range(cols):
            if grid[i][j] == "1":
                markiland(grid,i,j,row,cols)  
                count +=1
    return count


grid =[
  ["1","1","1","1","0"],
  ["1","1","0","0","0"],
  ["1","1","0","1","0"],
  ["0","0","0","0","0"]
]
print(numberOfIlands(grid))



