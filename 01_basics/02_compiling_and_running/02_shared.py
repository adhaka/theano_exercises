# Fill in the TODOs in this exercise, then run
# python 01_function.py to see if your solution works!
#
import numpy as np
import theano
from theano import function 
from theano import shared
from collections import OrderedDict

# raise NotImplementedError("TODO: add any other imports you need")

def make_shared(shape):
    """
    Returns a theano shared variable containing a tensor of the specified
    shape.
    You can use any value you want.
    """
    return theano.shared(value=np.zeros(shape))
    # raise NotImplementedError("TODO: implement the function")

def exchange_shared(a, b):
    """
    a: a theano shared variable
    b: a theano shared variable
    Uses get_value and set_value to swap the values stored in a and b
    """
    a_value = a.get_value()
    b_value = b.get_value()
    b.set_value(a_value)
    a.set_value(b_value)
    # a_value, b_value = b_value, a_value
    # raise NotImplementedError("TODO: implement the function")

def make_exchange_func(a, b):
    """
    a: a theano shared variable
    b: a theano shared variable
    Returns f
    where f is a theano function, that, when called, swaps the
    values in a and b
    f should not return anything
    """
    # a,b = b,a
    updates = OrderedDict()
    updates[a] = b 
    updates[b] = a
    f = function([], updates=updates)
    return f

    # raise NotImplementedError("TODO: implement the function")



if __name__ == "__main__":
    a = make_shared((5, 4, 3))
    assert a.get_value().shape == (5, 4, 3)
    b = make_shared((5, 4, 3))
    assert a.get_value().shape == (5, 4, 3)
    a.set_value(np.zeros((5, 4, 3), dtype=a.dtype))
    b.set_value(np.ones((5, 4, 3), dtype=b.dtype))
    exchange_shared(a, b)
    assert np.all(a.get_value() == 1.)
    assert np.all(b.get_value() == 0.)
    f = make_exchange_func(a, b)
    rval = f()
    assert isinstance(rval, list)
    assert len(rval) == 0
    assert np.all(a.get_value() == 0.)
    assert np.all(b.get_value() == 1.)

    print "SUCCESS!"
