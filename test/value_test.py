# -*- coding: utf-8 -*-
# CRISTIAN ECHEVERRÍA RABÍ

from datetime import datetime, date, time
from cer.value import validator
from cer.value import check
from cer.value import deco
import unittest

#-----------------------------------------------------------------------------------------

class TCValidator(unittest.TestCase):
    
    def testText(self):
        v = validator.Text()
        self.assertEqual(v.getData("4"), "4")
        self.assertEqual(v.getData("4"), u"4")
        self.assert_(v.check(""))
        
        v = validator.Text(format="Hola %s")
        self.assertEqual(v.getData("Pepe"), "Pepe")
        self.assertEqual(v.getText("Pepe"), u"Hola Pepe")
    
    def testInt(self):
        v = validator.Int()
        self.assertEqual(v.getData("4"), 4)
        self.assertEqual(v.getText(3), "3")
        self.assertRaises(ValueError, v.getData, "AA")
        
        v = validator.Int(vmin=4, vmax=10)
        self.assertEqual(v.getData("4"), 4)
        self.assertRaises(ValueError, v.getData, "3")
        self.assertRaises(ValueError, v.getData, "11")
    
"""
    def testFuntionMayor(self):
        self.assert_(check.gt(4,1))
        self.assertRaises(ValueError, check.gt, 2, 2)
        self.assertRaises(ValueError, check.gt, 3, 4)
    
    def testFuntionMayorIgual(self):
        self.assert_(check.ge(4,1))
        self.assert_(check.ge(2,2))
        self.assertRaises(ValueError, check.ge, 3, 4)
    
    def testFuntionIsIn(self):
        self.assert_(check.isIn(2,[1, 2, 3, 4]))
        self.assert_(check.isIn("c","casa"))
        self.assert_(check.isIn("c",["a", "b", "c"]))
        
        self.assertRaises(ValueError, check.isIn, 2, [1, 4, 6])
        self.assertRaises(ValueError, check.isIn, "c", "test")
        self.assertRaises(ValueError, check.isIn, "c", ["a", "b", "d"])
"""
#-----------------------------------------------------------------------------------------

class TCCheck(unittest.TestCase):
    
    def testFuntionMenor(self):
        self.assert_(check.lt(2,4))
        self.assertRaises(ValueError, check.lt, 2, 2)
        self.assertRaises(ValueError, check.lt, 3, 2)
    
    def testFuntionMenorIgual(self):
        self.assert_(check.le(2,4))
        self.assert_(check.le(2,2))
        self.assertRaises(ValueError, check.le, 3, 2)
    
    def testFuntionMayor(self):
        self.assert_(check.gt(4,1))
        self.assertRaises(ValueError, check.gt, 2, 2)
        self.assertRaises(ValueError, check.gt, 3, 4)
    
    def testFuntionMayorIgual(self):
        self.assert_(check.ge(4,1))
        self.assert_(check.ge(2,2))
        self.assertRaises(ValueError, check.ge, 3, 4)
    
    def testFuntionIsIn(self):
        self.assert_(check.isIn(2,[1, 2, 3, 4]))
        self.assert_(check.isIn("c","casa"))
        self.assert_(check.isIn("c",["a", "b", "c"]))
        
        self.assertRaises(ValueError, check.isIn, 2, [1, 4, 6])
        self.assertRaises(ValueError, check.isIn, "c", "test")
        self.assertRaises(ValueError, check.isIn, "c", ["a", "b", "d"])

#-----------------------------------------------------------------------------------------

class TCDeco(unittest.TestCase):
    
    @deco.lt(2)
    def myDecoMenor(self, value):
        return value
    
    @deco.isIn([2, 4, 6, 8, 10])
    def myDecoIn(self, value):
        return value
    
    def testDecoIsIn(self):
        
        @deco.isIn([1, 2, 3])
        def prueba(value):
            return value
        
        self.assert_(prueba(1))
        self.assertRaises(ValueError, prueba, 4)
        self.assertEqual(prueba(2), 2)
        
        self.assert_(self.myDecoIn(4))
        self.assert_(self.myDecoIn(6))
        self.assertRaises(ValueError, self.myDecoIn, 1)
        self.assertRaises(ValueError, self.myDecoIn, 3)
        self.assertEqual(self.myDecoIn(8), 8)
    
    def testDecoMenor(self):
        
        @deco.lt(2)
        def prueba(value):
            return value
        
        self.assert_(prueba(1))
        self.assertRaises(ValueError, prueba, 2)
        self.assertRaises(ValueError, prueba, 3)
        self.assertEqual(prueba(1.5), 1.5)
        
        self.assert_(self.myDecoMenor(1))
        self.assertRaises(ValueError, self.myDecoMenor, 2)
        self.assertRaises(ValueError, self.myDecoMenor, 3)
        self.assertEqual(self.myDecoMenor(1.5), 1.5)
    
    def testDecoMenorIgual(self):
        
        @deco.le(2)
        def prueba(value):
            return value
        
        self.assert_(prueba(1))
        self.assert_(prueba(2))
        self.assertRaises(ValueError, prueba, 3)
        self.assertEqual(prueba(1.5), 1.5)
    
    def testDecoMayor(self):

        @deco.gt(2)
        def prueba(value):
            return value
        
        self.assert_(prueba(2.1))
        self.assertRaises(ValueError, prueba, 2)
        self.assertRaises(ValueError, prueba, 1)
        self.assertEqual(prueba(2.5), 2.5)
    
    def testDecoMayorIgual(self):

        @deco.ge(2)
        def prueba(value):
            return value
        
        self.assert_(prueba(2.1))
        self.assert_(prueba(2))
        self.assertRaises(ValueError, prueba, 1)
        self.assertEqual(prueba(2.5), 2.5)

#-----------------------------------------------------------------------------------------

s1 = unittest.TestLoader().loadTestsFromTestCase(TCValidator)
s2 = unittest.TestLoader().loadTestsFromTestCase(TCCheck)
s3 = unittest.TestLoader().loadTestsFromTestCase(TCDeco)

suite = unittest.TestSuite([s1, s2, s3])

#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)