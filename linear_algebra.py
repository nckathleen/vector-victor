
class ShapeException(Exception):
    pass

def shape(vector_list):
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    shape = len(vector_list)
    return (shape,)


def vector_add(w, y):
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    return [w[i] + y[i] for i in range(len(w))]
