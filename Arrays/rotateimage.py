def rotate(matrix) -> None:

    startRow, endRow = 0, len(matrix)-1
    startCol, endCol = 0, len(matrix[0])-1

    while startCol < endCol:
        for i in range(endRow-startRow):
            corn = matrix[startRow][startCol+i]

            matrix[startRow][startCol+i] = matrix[endRow-i][startCol]
            matrix[endRow - i][startCol] = matrix[endRow][endCol-i]
            matrix[endRow][endCol - i] = matrix[startRow + i][endCol]
            matrix[startRow+i][endCol] = corn

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return matrix
