import math

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
# Could use shape function from above in this one.
    if len(w) != len(y):
        raise ShapeException('Vectors must be the same size.')
    return [w[i] + y[i] for i in range(len(w))]


def vector_sub(v, w):
    if len(v) != len(w):
        raise ShapeException('Vectors must be the same size.')
    return [v[i] - w[i] for i in range(len(v))]


def vector_sum(*args):
    """vector_sum can take any number of vectors and add them together."""

    if len(args[0]) != len(args[1]):
        raise ShapeException('Vectors must be the same size.')
    total = [0] * len(args[0])
    for i in args:
        total = vector_add(total,i)
    return total


def dot(w, y):
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """

    if len(w) != len(y):
        raise ShapeException('Vectors must be the same size.')
    return sum([w[i] * y[i] for i in range(len(w))])


def vector_multiply(v, s):
    """
    [a b]  *  Z     = [a*Z b*Z]

    Vector * Scalar = Vector
    """

    return [s * i for i in v]


def vector_mean(*args):
    """
    mean([a b], [c d]) = [mean(a, c) mean(b, d)]

    mean(Vector)       = Vector
    """
#  Also could use vector_multiply from above in this one.
    return [i/len(args) for i in vector_sum(*args)]


def magnitude(m):
    """
    magnitude([a b])  = sqrt(a^2 + b^2)

    magnitude(Vector) = Scalar
    """

    magnitude = math.sqrt(sum([x**2 for x in m]))
    return magnitude
