# Fill in the TODOs in this exercise, then run the script to see if your
# solution works.
import numpy as np
import theano.tensor as T
from theano import function 
from theano import shared

def increment_odd(x):
    """
    x: a Theano vector
    Returns:
    y: a Theano vector equal to x, but with all odd-numbered elements
    incremented by 1.
    """
    return T.inc_subtensor(x[1::2], 1.0)

    # y = theano.shared(value=x_val)
    # raise NotImplementedError("TODO: implement the function.")

if __name__ == "__main__":
    x = T.vector()
    xv = np.zeros((4,), dtype=x.dtype)
    yv = increment_odd(x).eval({x:xv})
    assert np.allclose(yv, np.array([0., 1., 0., 1.]))
    print "SUCCESS!"
