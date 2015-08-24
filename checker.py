# CRISTIAN ECHEVERRÍA RABÍ

import operator as op

#-----------------------------------------------------------------------------------------

__all__ = ['Check', 'CheckReport']

#-----------------------------------------------------------------------------------------

def _isIn(val, valSecuence):
    return op.contains(valSecuence, val)

#-----------------------------------------------------------------------------------------

class Check(object):
    """Class for value testing with error raising"""
    
    txtMessage = "Required value %s %s (%s entered)"
    
    def __init__(self, value):
        self._value = value
    
    def _compare(self, compFunc, txte, limit):
        if not compFunc(self._value, limit):
            txt = self.txtMessage % (txte, limit, self._value)
            raise ValueError(txt)
        return self
    
    def lt(self, limit):
        return self._compare(op.lt, "<", limit)
    
    def le(self, limit):
        return self._compare(op.le, "<=", limit)
    
    def gt(self, limit):
        return self._compare(op.gt, ">", limit)
    
    def ge(self, limit):
        return self._compare(op.ge, ">=", limit)
    
    def isIn(self, valSecuence):
        return self._compare(_isIn, "in", valSecuence)

#-----------------------------------------------------------------------------------------

class CheckReport(Check):
    """Class for value testing with reporting"""
    
    def __init__(self, value):
        Check.__init__(self, value)
        self.errors = []
    
    def _compare(self, compFunc, txte, limit):
        if not compFunc(self._value, limit):
            txt = self.txtMessage % (txte, limit, self._value)
            self.errors.append(txt)
        return self

#-----------------------------------------------------------------------------------------

if __name__ == "__main__":
    value = 0
    #ck = Check(value).ge(0).le(1).isIn([0.1, 0.5, 0.7])
    ck = CheckReport(value).ge(0).le(1).isIn([0.1, 0.5, 0.7])
    print(ck.errors)
    
    