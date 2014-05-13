# CRISTIAN ECHEVERRÍA RABÍ

import operator as op

#-----------------------------------------------------------------------------------------

__all__ = ['lt', 'le', 'gt', 'ge', 'isIn']

#-----------------------------------------------------------------------------------------

class CheckValueMaker(object):
    """Makes function for value testing"""
    
    txtMessage = "Required value %s %s (%s entered)"
    
    def __init__(self, compFunc, txtErr):
        self.compFunc = compFunc
        self.txtErr = txtErr
    
    def __call__(self, value, limit):
        if not self.compFunc(value, limit):
            txt = self.txtMessage % (self.txtErr, limit, value)
            raise ValueError(txt)
        return True

lt = CheckValueMaker(op.lt, "<")
le = CheckValueMaker(op.le, "<=")
gt = CheckValueMaker(op.gt, ">")
ge = CheckValueMaker(op.ge, ">=")

#-----------------------------------------------------------------------------------------
# Test if value is inside a secuence

def isIn(value, valueList):
    op = (value in valueList)
    if not op:
        txt = "Requiered value in %s (%s entered)" % (valueList, value)
        raise ValueError(txt)
    return True