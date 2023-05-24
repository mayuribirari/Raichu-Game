
### Description: 
The problem statement states that we need to find the next best move that can be played by the computer for a given board. We have 3 different pieces which are Raichus, Pikachus and pichus which behave differently. We have to write a heuristic which returns the next best move after evaluating all the possible moves according to the conditions given for raichu, pichu and pikachu. 

### Various functions and steps that I have used and considered to solve this problem are:

#### Create raichu:
This function creates a raichu whenever pichu or pikachu of black or white player reaches opposite end of opponents board.

#### Check_goal_state: 
Returns a bool value based on the count of white pawns and black pawns. Function returns true if the count of either of white pawns or black pawns is 0 else returns false.

#### Min_value:
This function returns the minimum of it’s utilities of it’s successors which is calculated based on the evaluation function.

#### Max_value:
This function returns the maximum of the utilities of it’s successors which is calculated based on the evaluation function.

#### Minimax:
Minimax uses the depth limitation and alpha beta pruning and chooses the next best move.

#### Successor Function: 
The resulting board and the move done to achieve the board will be appended. We return a list of all the possible boards for a given board. The functions pichu_moves_white, pikachu_moves_white, raichu_moves_white, pichu_moves_black, pikachu_moves_black, raichu_moves_black functions are used to find all the possible successors. Each of these functions returns a list of all possible moves that can be made by each piece.

#### Evaluation function:
We have implemented the static evaluation function. It is the sum of features. In our case we have used the number of pieces of white and black as our features. We have given weights to pichus, pikachus and raichus and we are adding the difference of sum of our pichus, pikachus and raichus and the sum of opponent pichus, pikachus and raichus and multiplying them with the respective weights to find the evaluated value. 
We have optimized the evaluated value by adding an operation of our own. We are calculating the sum of the distances that each player has traveled from their base positions with the help of functions find_loc_pichu_white, find_loc_pikachu_white, find_loc_raichu_white, find_loc_pichu_black, find_loc_pikachu_ black, find_loc_raichu_ black. This would give us how close that player is to becoming a raichu. Greater the evaluated value, means more chances of winning the game.

For example, the weights of pichus,pikachus and raichus = 20, 50, 80 respectively

Evaluated value = [20(difference of sum of our pichus and sum of opponent pichus) + 50(difference of sum of our pikachus and sum of opponent pikachus) + 80(difference of sum of our raichus and sum of opponent raichus).

Evaluated value = Evaluated value + sum of distances of each player from their base positions.
