# CRISTIAN ECHEVERRÍA RABÍ

from cer.value.checker import Check, CheckReport
import unittest

#-----------------------------------------------------------------------------------------

class TCCheck(unittest.TestCase):
    
    def testObjReturn(self):
        ck = Check(4)
        self.assertEqual(ck, ck.lt(5))
        self.assertEqual(ck, ck.le(4))
        self.assertEqual(ck, ck.gt(3))
        self.assertEqual(ck, ck.ge(4))
        self.assertEqual(ck, ck.isIn([2, 3, 4]))
    
    def testLt(self):
        self.assertTrue(Check(2).lt(3))
        self.assertRaises(ValueError, Check(2).lt, 2)
        self.assertRaises(ValueError, Check(2).lt, 1)
        #with self.assertRaises(ValueError):
        #    Check(2).lt(2)
        #    Check(2).lt(3)    # Esto no funciona
    
    def testLe(self):
        self.assertTrue(Check(2).le(4))
        self.assertTrue(Check(2).le(2))
        self.assertRaises(ValueError, Check(3).le, 2)
    
    def testGt(self):
        self.assertTrue(Check(4).gt(1))
        self.assertRaises(ValueError, Check(2).gt, 2)
        self.assertRaises(ValueError, Check(3).gt, 4)
    
    def testGe(self):
        self.assertTrue(Check(4).ge(1))
        self.assertTrue(Check(2).ge(2))
        self.assertRaises(ValueError, Check(3).ge, 4)
    
    def testMixed(self):
        self.assertTrue(Check(0.5).gt(0).lt(1))
        self.assertTrue(Check(0).ge(0).le(1))
        self.assertTrue(Check(1).ge(0).le(1))
        self.assertTrue(Check(0.5).ge(0).le(1).isIn, [0, 0.25, 0.5, 1])
        
        self.assertRaises(ValueError, Check(0).lt(1).gt, 0)
        self.assertRaises(ValueError, Check(1).gt(0).lt, 1)
        
        self.assertRaises(ValueError, Check(0.5).gt(0).lt(1).isIn, [0, 1, 2])
        
    
    def testIsIn(self):
        self.assertTrue(Check(1).isIn([1.0, 2, 3, 4]))
        self.assertTrue(Check(2).isIn([1, 2, 3, 4]))
        self.assertTrue(Check("c").isIn("casa"))
        self.assertTrue(Check("c").isIn(["a", "b", "c"]))
        
        self.assertRaises(ValueError, Check(2).isIn, [1, 4, 6])
        self.assertRaises(ValueError, Check("c").isIn, "test")
        self.assertRaises(ValueError, Check("c").isIn, ["a", "b", "d"])

#-----------------------------------------------------------------------------------------

s1 = unittest.TestLoader().loadTestsFromTestCase(TCCheck)

suite = unittest.TestSuite([s1])

#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)