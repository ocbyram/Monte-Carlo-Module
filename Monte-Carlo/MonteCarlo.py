import pandas as pd
import numpy as np
import random
from collections import Counter

class Die: 
    
    def __init__(self,faces):
        self.faces = faces
        if not isinstance(self.faces, np.ndarray):
            raise TypeError
        if not (len(self.faces) == len(set(self.faces))) == True:
            raise ValueError
        for each in self.faces:
            weight = 1.0
            self.weight = weight
        self.df = pd.DataFrame({'Weight':weight},index=faces)
            
    def change_weight(self,face_val, new_weight):
        if face_val not in self.df.index:
            raise IndexError
        try:
            float(new_weight)
        except:
            raise TypeError
        self.df.loc[face_val, 'Weight'] = new_weight

    def roll(self, rolls = 1):
        sample = self.df.sample(n=rolls, replace=True, weights='Weight').index.tolist()
        return sample
        
    def state(self):
        return self.df.copy()

class Game:
    
    def __init__(self, sim_faces):
        self.sim_faces = sim_faces
            
    def play(self, num_rolls):
        outcomes = {i: die.roll(num_rolls) for i, die in enumerate(self.sim_faces)}
        self.game_df = pd.DataFrame(outcomes)
        self.game_df.index.name = "Roll Number"
        
    def show(self, form = 'wide'):
        if form != 'wide' and form != 'narrow':
            raise ValueError
        if form == 'wide':
            return self.game_df.copy()
        elif form == 'narrow':
            self.narrow_df = self.game_df.melt(
                var_name = 'Die Number',
                value_name = 'Value',
                ignore_index = False)
            self.narrow_df.set_index(['Die Number'], append=True, inplace=True)
            return self.narrow_df
        else:
            raise ValueError

class Analyzer:
    
    def __init__(self, game_object):
        if not isinstance(game_object, Game):
            raise ValueError
        self.game_object = game_object
        self.roll_result = game_object.show()

    def jackpot(self):
        jackpots = self.roll_result.apply(lambda row: row.nunique() == 1, axis=1).sum()
        return int(jackpots)

    def face_counts(self):
        counts = self.roll_result.apply(lambda row: row.value_counts(), axis=1)
        counts.fillna(0, inplace=True)
        return counts
        
    def combos(self):
        cols = self.roll_result.columns.difference(['id']).tolist()
        self.df = self.roll_result.groupby(cols, sort=True).size().reset_index(name='Counts')
        self.df=self.df.set_index(self.df.columns.difference(['Counts'],sort=True).tolist())
        return self.df
        
    def permutations(self):
        self.tups = []
        self.tup_list = []
        for index, row in self.roll_result.iterrows():
            self.tups.append(tuple(row))
        counts = Counter(self.tups)
        self.df = pd.DataFrame(counts.items(), columns=['Permutation', 'Count'])
        tup_len = len(self.tups[0])
        for i in range(0,tup_len):
            self.tup_list.append(i)
        self.df[self.tup_list] = pd.DataFrame(self.df['Permutation'].tolist(), index=self.df.index)
        self.df.drop('Permutation', axis=1, inplace=True)
        self.df=self.df.set_index(self.df.columns.difference(['Count'],sort=False).tolist())
        return self.df