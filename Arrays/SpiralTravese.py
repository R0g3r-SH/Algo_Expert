from tracemalloc import start

from pandas import array

# recuerda los edge cases en los que la maxitri tiene una fila enmedio o 
# una culumna enmedio 

def spiralTraverse(array):
    # Write your code here.
    out = []
    startCol, endCol = 0, len(array[0])-1
    startRow, endRow = 0, len(array)-1

    while startCol <= endCol and startRow<=endRow:

        for col in range(startCol, endCol+1):
            out.append(array[startRow][col])

        for row in range(startCol+1, endRow):
            out.append(array[row][endCol])

        for col in reversed(range(startCol, endCol+1)):
            if startRow== endRow:
                break
            out.append(array[endRow][col])

        for row in reversed(range(startCol+1, endRow)):
            if startCol == startCol:
                break
            out.append(array[row][startCol])
        
        startCol+=1
        endCol-=1
        startRow+=1
        endRow-=1

    return out


array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
spiralTraverse(array)
