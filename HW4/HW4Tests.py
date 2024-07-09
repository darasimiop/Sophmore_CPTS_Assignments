import sys
import io
import unittest
from HW4 import *

class HW4Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testOpPush(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[-1],"(Hello)")
    
    def testOpPush2(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1],5)

    def testOpPop(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(),5)
    
    def testDictPush(self):
        dictstack.clear()
        dictPush({})
        self.assertEqual(dictstack[-1],{})

    def testDictPop(self):
        dictstack.clear()
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),0)

    def testDefine(self):
        dictstack.clear()
        define("/a",1)
        self.assertEqual(len(dictstack),1)

    def testLookup(self):
        dictstack.clear()  
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()
        self.assertEqual(lookup("n1"),"(hornswaggle)")

    def testAdd(self):
        opstack.clear()     
        opPush(1.0)       
        opPush(2.0)       
        add()       
        self.assertEqual(opPop(),3)

    def testAdd2(self):
        opstack.clear()     
        opPush(3)
        opPush("(notanum)")
        add()       
        self.assertEqual(opPop(),"(notanum)")
        self.assertEqual(opPop(),3)

    def testSub(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        sub()
        self.assertEqual(opPop(),1)
    
    def testMul(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mul()
        self.assertEqual(opPop(),6)

    def testDiv(self):
        opstack.clear()
        opPush(4)
        opPush(2)
        div()
        self.assertEqual(opPop(),2)
    
    def testMod(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mod()
        self.assertEqual(opPop(),1)

    def testEq2(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        eq()
        self.assertEqual(opPop(),False)

    def testLt(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        lt()
        self.assertEqual(opPop(),True)

    def testGt2(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)

    def testLength(self):
        opstack.clear()
        opPush("(Hello)")
        length()
        self.assertEqual(opPop(),5)

    def testGet(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))

    def testGetInterval(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(Cpt)")

    def testPut(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")

    def testDup(self):
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(len(opstack),2)

    def testPop(self):
        opstack.clear()
        opPush(1)
        pop()
        self.assertEqual(len(opstack),0)
    
    def testClear(self):
        opstack.clear()
        opPush(1)
        clear()
        self.assertEqual(len(opstack),0)

    def testExch(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,1])

    def testRoll(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(2)
        opPush(3)
        roll()
        self.assertListEqual(opstack,[1,2,4,3])
    
    def testStack(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")

    def testPsDict(self):
        opstack.clear()
        opPush(2)
        psDict()
        self.assertIsInstance(opPop(), dict)

    def testPsDef(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1],{"/a":2})

if __name__ == '__main__':
    unittest.main()

