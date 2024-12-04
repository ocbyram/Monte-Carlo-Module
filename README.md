# Monte-Carlo-Module 
# DS5100 Final Project

## Metadata

Project Name: Monte Carlo Simulator

Author: Olivia Byram (ocb3wv)

## Synopsis

### Installation

```
pip install -e .
```

### Importing

```
import Monte_Carlo.MonteCarlo
from Monte_Carlo.MonteCarlo import Die, Game, Analyzer
```

### Code Use Examples

## API Description

### Die Class

    """Description: Creates a die based on a numpy array of faces inout by the user

    Methods:
    - __init__(): This initializes the die (creates it) and sets the default weights
                    as 1.

    - change_weight(): This allows the user to change the weight of any of the die
                         faces.

    - roll(): This allows the user to roll the die and returns a list of outcomes.

    - state(): This returns a dataframe of die rolls and outcomes. 
    """

**Die Class Methods:**

*__init__()*

        """Purpose: creates a die with the faces input as the argument. Initializes
        default weight for each face as 1.0.

        Arguments: faces: a numpy array of die faces. Must be numpy array
        and values must be distinct.

        Outcome: a private dataframe with faces and weights.
        faces are in the index.
        """

*change_weight()*

        """
        Purpose: A method to change the weight of a single face

        Arguments: face_val: the face value that the user would like to be changed (integer or string)
                new_weight: the new weight the user would like the face to have (integer)

        Outcome: changed weight for one face of the die
    
        """

*roll()*

        """
        Purpose: a method to roll the die one or more times

        Arguments: rolls: how many times the die is to be rolled (integer). Defaults to 1.

        Outcome: a list of roll outcomes
    
        """

*state()*

        """
        Purpose: a method to show die's current status

        Arguments: none

        Outcome: a copy of the private die dataframe
    
        """


### Game Class

    """Description: A game where the user can roll one ore more die at a time.

    Methods:
    - __init__(): This initializes the list of instantiated die

    - play(): a play method so users can roll the die

    - show(): A method to show the user the results of the most recent play
    """

*__init__()*

        """
        Purpose: an initializer for the dice

        Arguments: sim_faces: a list of instantiated dice

        Outcome: returns the list of instantiated dice
    
        """

*play()*

        """
        Purpose: a play method so users can roll the die

        Arguments: num_rolls: the number of times a user would like
                    the die to be rolled (integer)
            
        Outcome: a dataframe in wide format and the roll number
        as a named index, columns for each die number (using its list index
        as the column name), and the face rolled in that instance in each
        cell
    
        """

*show()*

        """
        Purpose: A method to show the user the results of the most recent play

        Arguments: form: What form the user would like the dataframe in.
                default is wide, other option is narrow. If anything else
                is passed, there is a value error. (string)

        Outcome: a dataframe in either wide or narrow format of roll number,
                die number, and the face rolled in that instance.
    
        """

### Analyzer Class
