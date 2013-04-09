'''
Created on 08.04.2013

@author: daddy
'''
import unittest
from solver import Field

f = Field( "aber"
          +"wasi"
          +"stda"
          +"sasd")

class Test(unittest.TestCase):
    
    def testField(self):
        assert f.lines[0] == "aber"

    def testPossibleNextPicks(self):
        picks = f.possibleNextPicks()
        assert (0, 0) in picks
        assert (3, 0) in picks
        assert (3, 3) in picks

    def testPossibleNextPicksWithGivenPath(self):
        picks = f.possibleNextPicks(chosenElements=[(0,0)])
        assert (0, 0) not in picks
        assert (1, 0) in picks
        assert (0, 1) in picks
        assert (1, 1) in picks

    def testPossibleNextPicksWithGivenPath2(self):
        picks = f.possibleNextPicks(chosenElements=[(0,0), (0,1)])
        assert (0, 0) not in picks
        assert (1, 0) in picks
        assert (0, 1) not in picks
        assert (1, 1) in picks
        assert (1, 2) in picks
        
    def testElementsAround(self):
        around = [x for x in f.elementsAround(0,0)]
        assert (1, 0) in around
        assert (0, 1) in around
        assert (0, 0) not in around
        assert (-1, 0) not in around
        
        around = [x for x in f.elementsAround(3,3)]
        assert (2, 2) in around
        assert (4, 3) not in around
        
    def testExistsSimple(self):
        assert f.exists("a")
        assert f.exists("aber")
        assert not f.exists("aberwasistssakjld")
    
    def testExistsComplex(self):
        assert f.exists("reist")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testField']
    unittest.main()