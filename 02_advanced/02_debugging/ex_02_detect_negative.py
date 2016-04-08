# Fill in the TODOs and run the script to see if your implementation works.
import numpy as np

from theano import function
from theano import tensor as T
from theano.compile import Mode

# raise NotImplementedError("TODO: add any imports you need.")

class NegativeVariableError(Exception):
    pass

def get_neg_detection_mode():
    """
    Returns a theano Mode that detects if any negative value occurs in the
    evaluation of a theano function.
    This mode should raise a NegativeVariableError if it ever detects any
    variable having a negative value during the execution of the theano
    function.
    """
    class NegativeVariableCheckMode(Mode):
        def __init__(self, args,):
            super(NegativeVariableCheckMode, self).__init__()            

            def _flatten(element):
                value = []
                if isinstance(element, [list, tuple]):
                    for ele in element:
                        if isinstance(ele, [list, tuple]):
                            value.extend(ele)
                        else:
                            value.append(ele)
                    return value
                else:
                    value.append(element)
                    return ele

            def _not_negative_check(val):
                if val.min() < 0:
                    raise NegativeVariableError()
                else:
                    return True

            def main_checks():





    raise NotImplementedError("TODO: implement this function.")


if __name__ == "__main__":
    x = T.scalar()
    x.name = 'x'
    y = T.nnet.sigmoid(x)
    y.name = 'y'
    z = - y
    z.name = 'z'
    mode = get_neg_detection_mode()
    f = function([x], z, mode=mode)
    caught = False
    try:
        f(0.)
    except NegativeVariableError:
        caught = True
    if not caught:
        print "You failed to catch a negative value."
        quit(-1)
    f = function([x], y, mode=mode)
    y1 = f(0.)
    f = function([x], y)
    assert np.allclose(f(0.), y1)
    print "SUCCESS!"
