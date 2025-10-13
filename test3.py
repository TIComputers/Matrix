
def TC(Matrix:list, col:int, ) -> list:
    """ The columns """

    columns = [] # new list for write columns list
    for row in Matrix:
        columns.append(row[col])
    return columns