# CRISTIAN ECHEVERRÍA RABÍ

import operator as op

#-----------------------------------------------------------------------------------------

__all__ = ['lt', 'le', 'gt', 'ge', 'isIn']

#-----------------------------------------------------------------------------------------

class DecoValueMaker(object):
    """Makes decorators for argument testing"""
    
    txtMessage = "Required argument %s %s (%s entered)"
    
    def __init__(self, compFunc, txtErr):
        self.compFunc = compFunc
        self.txtErr = txtErr

    def __call__(self, limit):
        def myDecorator(func):
            def wrapper(*args):
                if len(args) > 1:    # Es método
                    _x,val = args
                else:                # Es función
                    val, = args
                if self.compFunc(val, limit):
                    return func(*args)
                else:
                    txt = self.txtMessage % (self.txtErr, limit, val)
                    raise ValueError(txt)
            return wrapper
        return myDecorator

lt = DecoValueMaker(op.lt, "<")
le = DecoValueMaker(op.le, "<=")
gt = DecoValueMaker(op.gt, ">")
ge = DecoValueMaker(op.ge, ">=")

#-----------------------------------------------------------------------------------------
# Test if value is inside a secuence

def isIn(valueList):
    def myDecorator(func):
        def wrapper(*args):
            if len(args) > 1:    # Es método
                _x,val = args
            else:                # Es función
                val, = args
            op = (val in valueList)
            if op:
                return func(*args)
            else:
                txt = "Requiered argument in %s (%s entered)" % (valueList, val)
                raise ValueError(txt)
        return wrapper
    return myDecorator