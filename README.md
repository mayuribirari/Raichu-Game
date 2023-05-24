# Raichu-Game
Raichu is a popular childhood game played on an n × n grid (where n ≥ 8 is an even number) with three kinds of
pieces (Pichus, Pikachus, and Raichus) of two different colors (black and white). Initially the board starts empty,
except for a row of white Pikachus on the second row of the board, a row of white Pichus on the third row of the
board, and a row of black Pichus on row n − 2 and a row of black Pikachus on row n − 1:

![image](https://github.com/mayuribirari/Raichu-Game/assets/49620045/cfcc946c-6a66-443d-8176-0e51e7e060da)

Two players alternate turns, with White going first.
In any given turn, a player can choose a single piece of their color and move it according to the rules of that
piece.
A Pichu can move in one of two ways:
• one square forward diagonally, if that square is empty.
• “jump” over a single Pichu of the opposite color by moving two squares forward diagonally, if that
square is empty. The jumped piece is removed from the board as soon as it is jumped.
For example, for the highlighted Pichu in the following board at left, there are two possible moves, shown in
the right two boards:

![image](https://github.com/mayuribirari/Raichu-Game/assets/49620045/257ce1d9-668b-467a-98f8-f19dd62da5a3)

A Pikachu can move in one of two ways:
• 1 or 2 squares either forward, left, or right (but not diagonally) to an empty square, as long as all
squares in between are also empty.
• “jump” over a single Pichu/Pikachu of the opposite color by moving 2 or 3 squares forward, left or
right (not diagonally), as long as all of the squares between the Pikachu’s start position and jumped
piece are empty and all the squares between the jumped piece and the ending position are empty. The
jumped piece is removed as soon as it is jumped.
For example, for the highlighted Pikachu in the following board at left, here are some (not all) possible
moves:

![image](https://github.com/mayuribirari/Raichu-Game/assets/49620045/d8f2a27b-d64f-4058-982d-24abad5037c5)

A Raichu is created when a Pichu or Pikachu reaches the opposite side of the board (i.e. when a Black
Pichu or Pikachu reaches row 1 or a white Pichu or Pikachu reaches row n). When this happens, the Pichu
or Pikachu is removed from the board and subsituted with a Raichu. Raichus can move as follows:
• any number of squares forward/backward, left, right or diagonally, to an empty square, as long as all
squares in between are also empty.
• “jump” over a single Pichu/Pikachu/Raichu of the opposite color and landing any number of squares
forward/backward, left, right or diagonally, as long as all of the squares between the Raichu’s start
position and jumped piece are empty and all the squares between the jumped piece and the ending
position are empty. The jumped piece is removed as soon as it is jumped.

For example, some (not all) possible moves of the highlighted white Raichu are:

![image](https://github.com/mayuribirari/Raichu-Game/assets/49620045/67edb7bf-e582-4797-b720-4985564061a7)

Note the hierarchy: Pichus can only capture Pichus, Pikachus can capture Pichus or Pikachus, while Raichus
can capture any piece. The winner is the player who first captures all of the other player’s pieces.
Your task is to write a Python program that plays Raichu well. Your program should accept a command
line argument that gives the current state of the board as a string of .’s, w’s, W’s, b’s, B’s, @’s, and $’s, which
indicate which squares have no piece, a white Pichu, a white Pikachu, a black Pichu, a black Pikachu, a
white Raichu and a black Raichu respectively, in row-major order. For example, if n = 8, then the encoding
of the start state of the game would be:

........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........

More precisely, your program will be called with four command line parameters: (1) the value of n, (2) the
current player (w or b), (3) the state of the board, encoded as above, and (4) a time limit in seconds. 

python3 ./raichu.py 8 w '........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........' 10

![image](https://github.com/mayuribirari/Raichu-Game/assets/49620045/2d13714e-c1a9-46bf-abd6-ce3433c583e0)

