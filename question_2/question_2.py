
def is_valid_sudoku(matrix):
    """
    Input a matrix 2D (9x9) with  '.', '1', '2', '3', '4', '5', '6', '7', '8',
    '9'.
    Check if row or column or minimatrix (3x3) contains repeated elements then
    it returns False if not it returns True.
    """
    # Check dimensions
    assert len(matrix) == 9, 'input must be 9x9 list'
    assert all(
        [len(matrix[i]) == 9 for i in range(len(matrix))]
    ), 'input must be 9x9 list'

    # Check matrix values
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert matrix[i][j] in ['.', '1', '2', '3', '4', '5', '6',
                                    '7', '8', '9'], \
                'matrix elements must be "." or "number"'

    # Check if row contains repeated elements
    for i in range(9):
        row_matrix = []
        for j in range(9):
            if matrix[i][j] != '.' and matrix[i][j] in row_matrix:
                return False
            row_matrix.append(matrix[i][j])

    # Check if column contains repeated elements
    for j in range(9):
        column_matrix = []
        for i in range(9):
            if matrix[i][j] != '.' and matrix[i][j] in column_matrix:
                return False
            column_matrix.append(matrix[i][j])

    # Check if minimatrix (3x3) contains repeated elements
    for mi in range(3):
        for mj in range(3):
            minimatrix = []
            for i in range(3):
                for j in range(3):
                    if matrix[i+3*mi][j+3*mj] != '.' and \
                            matrix[i+3*mi][j+3*mj] in minimatrix:
                        return False
                    minimatrix.append(matrix[i+3*mi][j+3*mj])
    return True
