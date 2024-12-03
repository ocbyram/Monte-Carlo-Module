import pandas as pd
import numpy as np
import random
from collections import Counter

class Die: 
    """Description: Creates a die based on a numpy array of faces inout by the user

    Methods:
    - __init__(): This initializes the die (creates it) and sets the default weights
                    as 1.

    - change_weight(): This allows the user to change the weight of any of the die
                         faces.

    - roll(): This allows the user to roll the die and returns a list of outcomes.

    - state(): This returns a dataframe of die rolls and outcomes. 
    """
    
    def __init__(self,faces):
        
        """Purpose: creates a die with the faces input as the argument. Initializes
        default weight for each face as 1.0.

        Arguments: faces: a numpy array of die faces. Must be numpy array
        and values must be distinct.

        Outcome: a private dataframe with faces and weights.
        faces are in the index.
        """
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
        """
        Purpose: A method to change the weight of a single face

        Arguments: face_val: the face value that the user would like to be changed (integer or string)
                new_weight: the new weight the user would like the face to have (integer)

        Outcome: changed weight for one face of the die
    
        """
        if face_val not in self.df.index:
            raise IndexError
        try:
            float(new_weight)
        except:
            raise TypeError
        self.df.loc[face_val, 'Weight'] = new_weight

    def roll(self, rolls = 1):
        """
        Purpose: a method to roll the die one or more times

        Arguments: rolls: how many times the die is to be rolled (integer). Defaults to 1.

        Outcome: a list of roll outcomes
    
        """
        sample = self.df.sample(n=rolls, replace=True, weights='Weight').index.tolist()
        return sample
        
    def state(self):
        """
        Purpose: a method to show die's current status

        Arguments: none

        Outcome: a copy of the private die dataframe
    
        """
        return self.df.copy()

class Game:
    """Description: A game where the user can roll one ore more die at a time.

    Methods:
    - __init__(): This initializes the list of instantiated die

    - play(): a play method so users can roll the die

    - show(): A method to show the user the results of the most recent play
    """
    def __init__(self, sim_faces):
        """
        Purpose: an initializer for the dice

        Arguments: sim_faces: a list of instantiated dice

        Outcome: returns the list of instantiated dice
    
        """
        self.sim_faces = sim_faces
            
    def play(self, num_rolls):
        """
        Purpose: a play method so users can roll the die

        Arguments: num_rolls: the number of times a user would like
                    the die to be rolled (integer)
            
        Outcome: a dataframe in wide format and the roll number
        as a named index, columns for each die number (using its list index
        as the column name), and the face rolled in that instance in each
        cell
    
        """
        outcomes = {i: die.roll(num_rolls) for i, die in enumerate(self.sim_faces)}
        self.game_df = pd.DataFrame(outcomes)
        self.game_df.index.name = "Roll Number"
        
    def show(self, form = 'wide'):
        """
        Purpose: A method to show the user the results of the most recent play

        Arguments: form: What form the user would like the dataframe in.
                default is wide, other option is narrow. If anything else
                is passed, there is a value error. (string)

        Outcome: a dataframe in either wide or narrow format of roll number,
                die number, and the face rolled in that instance.
    
        """
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
    """Description: An Analyzer object that takes the results of a single game and computes
                    various descriptive statistical properties about it

    Methods:
    - __init__(): initializes the game_object argument

    - jackpot(): counts the number of times all faces of die rolled are the same. 
                    Computes how many times there is a jackpot in a game.

    - face_counts(): Computes how many times a given face is rolled in each event

    - combos(): Computes the distinct combinations of faces rolled, along with their
                counts

    - permutations(): Computes the distinct permutations of faces rolled, along with their
                        counts
    """
    
    def __init__(self, game_object):
        """
        Purpose: initializes the game_object argument

        Arguments: game_object: a game object. Throws a `ValueError` if
                    the passed value is not a Game object.

        Outcome: an instantiated game object
    
        """
        if not isinstance(game_object, Game):
            raise ValueError
        self.game_object = game_object
        self.roll_result = game_object.show()

    def jackpot(self):
        """
        Purpose: counts the number of times all faces of die rolled are the same. 
                    Computes how many times there is a jackpot in a game.
    
        Arguments: none
    
        Outcome: an integer with the number of times a jackpot was rolled in a game
        
        """
        jackpots = self.roll_result.apply(lambda row: row.nunique() == 1, axis=1).sum()
        return int(jackpots)

    def face_counts(self):
        """
        Purpose: Computes how many times a given face is rolled in each event
    
        Arguments: none
    
        Outcome: a dataframe of results with an index of the roll number, face values as
                    columns, and count values in the cells
        
        """
        counts = self.roll_result.apply(lambda row: row.value_counts(), axis=1)
        counts.fillna(0, inplace=True)
        return counts
        
    def combos(self):
        """
        Purpose: Computes the distinct combinations of faces rolled, along with their
                    counts
    
        Arguments: none
    
        Outcome: a dataframe of results with a MultiIndex of distinct combinations
                    and a column for the associated counts
        
        """
        cols = self.roll_result.columns.difference(['id']).tolist()
        self.df = self.roll_result.groupby(cols, sort=True).size().reset_index(name='Counts')
        self.df=self.df.set_index(self.df.columns.difference(['Counts'],sort=True).tolist())
        return self.df
        
    def permutations(self):
        """
        Purpose: Computes the distinct permutations of faces rolled, along with their
                        counts
    
        Arguments: none
    
        Outcome: a dataframe of results with a MultiIndex of distinct permutations
                    and a column for the associated counts
        
        """
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