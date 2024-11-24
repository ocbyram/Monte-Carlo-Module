import pandas as pd
import numpy as np
import random

class Die(): 
    
    def __init__(self,faces):
        if not isinstance(faces, np.ndarray):
            raise TypeError
        else:
            if not (len(faces) == len(set(faces))) == True:
                raise ValueError
            else:
                for each in faces:
                    weight = 1.0
                    self.weight = weight
            self.df = pd.DataFrame({'Weight':weight},index=faces)
            
    def change_weight(self,face_val, new_weight):
        if face_val not in faces:
            raise IndexError
        else:
            try:
                float(new_weight)
                self.df.loc[face_val, 'Weight'] = new_weight
            except:
                raise TypeError

    def roll(self, rolls = 1):
        weights = self.df["Weight"].values
        probabilities = weights / np.sum(weights)
        return list(np.random.choice(self.df.index, size = rolls, replace=True, p = probabilities))
    def state(self):
        return(self.df)