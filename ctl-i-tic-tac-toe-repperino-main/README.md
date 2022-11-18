General information about the CTL course available at https://ctl.polyphys.mat.ethz.ch/

# :wave: PROJECT tic-tac-toe 

Tic-tac-toe is a competition game for two materials, 1 and 2, who take turns converting zeros in a $3\times 3$ grid to their own number. The material who succeeds in placing three of its marks in a diagonal, horizontal, or vertical row is the better material, and the game is immediately over. The game terminates with a draw if there is no winner after $3^2=9$ turns. Material 1 is the first to convert a single 0 to 1. Tic-tac-toe is a solved game with a forced draw assuming best play from both materials. A variant of the original game is to operate on a $n\times n$ grid, i.e., to replace $3$ by $n\ge 3$. The code exits with a number -1 (error), 0 (ongoing game), 1 (winner material 1), 2 (winner material 2), 3 (draw), so that all resuling games can play against each other (automatically) from the command line. 

<img src="https://www.complexfluids.ethz.ch/images/PROJECT-tic-tac-toe.png">

## Task 1: tic_tac_toe.py 3 

The tic_tac_toe.py code (called without argument or with single argument 3) does the following, in exactly this order: 
1. read a configuration from a file named tic-tac-toe.txt, if it exists, otherwise start a new game with a 3x3 grid of zeros
2. determine if the configuration is a valid configuration (allowed values are 0,1,2; after the first move there should be a single '1' in the array, and so on), if not, [return and exit](https://github.com/mkmat/ETH-Computational-Thinking-Labs#returnexit) with -1
3. determine, if there is a winner, and if so, return and exit with the winning material number (1 or 2) 
4. check if the game is over and if so, return and exit with 3 (draw)
5. determine the material who is next to convert a zero, perform a single conversion, [save the configuration in file tic-tac-toe.txt](https://github.com/mkmat/ETH-Computational-Thinking-Labs#readsavematrix), and return and exit with 0. 

### output file format

tic-tac-toe.txt

This file contains three lines, where each line carries 3 space-separated numbers $\in\{0,1,2\}$. 
Here are three examples of such configuration  files

    0 0 0    0 1 0    0 1 2
    0 0 0    0 0 0    1 0 1
    0 0 0    0 0 0    2 1 0

### input file formats

No input file required. If a file tic-tac-toe.txt exists, it is read in and used as starting point. 

## Task 2:  tic_tac_toe.py 3 full

This module has two arguments and does the following: 
1. deletes an existing tic-tac-toe.txt
2. repeats calling the tic_tac_toe.py 3 script from Task 1, or calls tic_tac_toe(3), until it returns a non-vanishing value
3. return+exit with this non-vanishing value

## Task 3: tic_tac_toe.py <em>n</em>
The tic-tac-toe.py script when called with an argument (a single integer value $n>2$) does exactly the same as the tic-tac-toe.py 3 module, with the only difference that it operates on a $n\times n$ instead of $3\times 3$ grid.  

### output file formats

tic-tac-toe.txt

This file contains $n$ lines, where each line carries $n$ space-separated numbers $\in\{0,1,2\}$. If such file exists, it is used as input file.
For the presentation, you should also produce images based on the output files. 

## Task 4: tic_tac_toe.py <em>n</em> full

This module does the following: 
1. deletes an existing tic-tac-toe.txt, 
2. calls the tic_tac_toe(n) function from Task 3 until it returns a non-vanishing value 
3. return+exit with this non-vanishing value.  
