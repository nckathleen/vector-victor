
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
    """Shape rule: the vectors must be the same size."""

    if len(w) != len(y):
        raise ShapeException('Vectors must be the same size.')
    return [w[i] + y[i] for i in range(len(w))]


def vector_sub(v, w):
    if len(v) != len(w):
        raise ShapeException('Vectors must be the same size.')
    return [v[i] - w[i] for i in range(len(v))]

#
# def vector_sum(*args):
#     """vector_sum can take any number of vectors and add them together."""
#
#     return [arg1[i] + arg2[i] for i in range(len(arg1))]
#

def dot(w, y):
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """

    if len(w) != len(y):
        raise ShapeException('Vectors must be the same size.')
    return sum([w[i] * y[i] for i in range(len(w))])


    #  for n in range(len(newmat)):
    #       new_sum += newmat[n]
