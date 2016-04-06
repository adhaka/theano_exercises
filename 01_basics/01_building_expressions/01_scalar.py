# Fill in the TODOs in this exercise, then run
# python 01_scalar.py to see if your solution works!
#
import numpy as np
import theano
import theano.tensor as T
from theano import function
#raise NotImplementedError("TODO: add any other imports you need")

def make_scalar():
    """
    Returns a new Theano scalar.
    """
    return T.scalar()
    #raise NotImplementedError("TODO: implement this function.")

def log(x):
    """
    Returns the logarithm of a Theano scalar x.
    """
    return T.log(x)
    #raise NotImplementedError("TODO: implement this function.")

def add(x, y):
    """
    Adds two theano scalars together and returns the result.
    """
    return x+y
    #raise NotImplementedError("TODO: implement this function.")

if __name__ == "__main__":
    a = make_scalar()
    b = make_scalar()
    c = log(b)
    d = add(a, c)
    f = function([a, b], d)
    a = np.cast[a.dtype](1.)
    b = np.cast[b.dtype](2.)
    actual = f(a,b)
    expected = 1. + np.log(2.)
    assert np.allclose(actual, expected)
    print "SUCCESS!"
