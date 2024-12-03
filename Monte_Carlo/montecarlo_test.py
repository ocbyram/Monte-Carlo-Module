import pandas as pd
import numpy as np
import random
from collections import Counter
from MonteCarlo import Die, Game, Analyzer

import unittest

class DieTestSuite(unittest.TestCase):
    
    def test_init(self):
        DieTest = Die(np.array([1,2,3,4,5,6]))
        test = isinstance(DieTest, Die)
        message = "Die was not created"
        self.assertTrue(test, message)

    def test_weight(self):
        DieTest2 = Die(np.array([1,2,3,4,5,6]))
        DieTest2.change_weight(1,5)
        test2 = DieTest2.state().loc[1, 'Weight'] == 5
        message = "Weight of die face was not changed"
        self.assertTrue(test2, message)

    def test_roll(self):
        DieTest3 = Die(np.array([1,2,3,4,5,6]))
        test3 = isinstance(DieTest3.roll(10),list)
        message = "This is not a list"
        self.assertTrue(test3, message)

    def test_state(self):
        DieTest4 = Die(np.array([1,2,3,4,5,6]))
        test4 = isinstance(DieTest4.state(), pd.DataFrame)
        message = "This is not a dataframe"
        self.assertTrue(test4, message)

class GameTestSuite(unittest.TestCase):
    
    def test_init(self):
        DieTest = Die(np.array([1,2,3,4,5,6]))
        GameTest = Game([DieTest])
        test = isinstance(GameTest, Game)
        message = "Game was not initialized"
        self.assertTrue(test, message)

    def test_play(self):
        DieTest2 = Die(np.array([1,2,3,4,5,6]))
        GameTest = Game([DieTest2])
        GameTest.play(10)
        show_df = GameTest.show()
        test2 = isinstance(show_df, pd.DataFrame)
        message = "This is not a dataframe"
        self.assertTrue(test2, message)

    def test_show(self):
        DieTest3 = Die(np.array([1,2,3,4,5,6]))
        GameTest2 = Game([DieTest3])
        GameTest2.play(10)
        show_df2 = GameTest2.show()
        test3 = isinstance(show_df2, pd.DataFrame)
        message = "This is not a dataframe"
        self.assertTrue(test3, message)

class AnalyzerTestSuite(unittest.TestCase):
    
    def test_init(self):
        DieTest = Die(np.array([1,2,3,4,5,6]))
        GameTest = Game([DieTest])
        GameTest.play(10)
        AnalyzeTest = Analyzer(GameTest)
        test = isinstance(AnalyzeTest, Analyzer)
        message = "Analyze was not initialized"
        self.assertTrue(test, message)
        
    def test_jackpot(self):
        DieTest2 = Die(np.array([1,2,3,4,5,6]))
        GameTest2 = Game([DieTest2])
        GameTest2.play(10)
        AnalyzeTest2 = Analyzer(GameTest2)
        jackpot = AnalyzeTest2.jackpot()
        test2 = isinstance(jackpot, int)
        message = "This is not an integer"
        self.assertTrue(test2, message)
        
    def test_face_counts(self):
        DieTest3 = Die(np.array([1,2,3,4,5,6]))
        GameTest3 = Game([DieTest3])
        GameTest3.play(10)
        AnalyzeTest3 = Analyzer(GameTest3)
        counts = AnalyzeTest3.face_counts()
        test3 = isinstance(counts, pd.DataFrame)
        message = "This is not a dataframe"
        self.assertTrue(test3, message)

    def test_combos(self):
        DieTest4 = Die(np.array([1,2,3,4,5,6]))
        GameTest4 = Game([DieTest4])
        GameTest4.play(10)
        AnalyzeTest4 = Analyzer(GameTest4)
        df = AnalyzeTest4.combos()
        test4 = isinstance(df, pd.DataFrame)
        message = "This is not a dataframe"
        self.assertTrue(test4, message)
        
    def test_permutations(self):
        DieTest5 = Die(np.array([1,2,3,4,5,6]))
        GameTest5 = Game([DieTest5])
        GameTest5.play(10)
        AnalyzeTest5 = Analyzer(GameTest5)
        df2 = AnalyzeTest5.permutations()
        test5 = isinstance(df2, pd.DataFrame)
        message = "This is not a dataframe"
        self.assertTrue(test5, message)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)