# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ

import string
from datetime import datetime

#-----------------------------------------------------------------------------------------

__all__ = ['Base', 'Text', 'Int', 'Float', 'Time', 'Date', 'DateTime']

#-----------------------------------------------------------------------------------------

class Base(object):
    
    _format = "%s"
    _chars = ""
    
    def __init__(self, format=None, chars=None):
        self.format = self._format if (format is None) else format
        self.chars = self._chars if (chars is None) else chars
    
    def adapt(self, text):
        """Return adapted value with the right type or raise ValueError"""
        return text
    
    def check(self, value):
        """Return True if value is into the range or raise ValueError"""
        return True
    
    def getData(self, text):
        value = self.adapt(text)
        self.check(value)
        return value
    
    def getText(self, data):
        txt = "" if (data is None) else (self.format % data)
        return txt

#-----------------------------------------------------------------------------------------

class Text(Base):
    
    def adapt(self, text):
        return unicode(text)


#-----------------------------------------------------------------------------------------

class Int(Base):
    
    _format = "%d"
    _chars = string.digits + "+-"
    
    def __init__(self, format=None, vmin=None, vmax=None, chars=None):
        self.vmin = vmin
        self.vmax = vmax
        Base.__init__(self, format, chars)
    
    def adapt(self, text):
        try:
            return int(text)
        except ValueError:
            raise ValueError("Int or Long expected")

    def check(self, value):
        if not(self.vmin is None) and value < self.vmin:
            raise ValueError("Value (%s) < %s" % (value, self.vmin))
        if not(self.vmax is None) and value > self.vmax:
            raise ValueError("Value (%s) > %s" % (value, self.vmax))


#-----------------------------------------------------------------------------------------

class Float(Int):
    
    _format = "%2f"
    _chars = string.digits + "+-."
    
    def adapt(self, text):
        try:
            return float(text)
        except ValueError:
            raise ValueError("Number expected")


#-----------------------------------------------------------------------------------------

class Time(Int):
    
    _format = "%H:%M"
    _chars = string.digits + ":"
    
    def adapt(self, text):
        try:
            val = datetime.strptime(text, self.format)
            return val.time()
        except ValueError:
            raise ValueError("Time expected")
    
    def getText(self, data):
        txt = "" if (data is None) else data.strftime(self.format)
        return txt

#-----------------------------------------------------------------------------------------

class Date(Time):
    
    _format = "%d/%m/%Y"
    _chars = string.digits + "/"
    
    def adapt(self, text):
        try:
            val = datetime.strptime(text, self.format)
            return val.date()
        except ValueError:
            raise ValueError("Date expected")

#-----------------------------------------------------------------------------------------

class DateTime(Time):
    
    _format = "%d/%m/%Y %H:%M"
    _chars = string.digits + "/:"
    
    def adapt(self, text):
        try:
            return datetime.strptime(text, self.format)
        except ValueError:
            raise ValueError("DateTime expected")