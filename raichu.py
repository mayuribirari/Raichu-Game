#
# raichu.py : Play the game of Raichu
#
# Mayuri Birari : mbirari@iu.edu
# Himani Patil : hipatil@iu.edu
# Gnaneswari Lolugu : gnlolugu@iu.edu
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import copy
import sys
import time


def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))


def convert_to_board(board,N):
    newList=[]
    for i in range(N):
        newList.append([board[t+(i*N)] for t in range(N)])
    return newList

def print_board(board,N):
    for i in board:
        print(i)

def valid_index(pos, n):
        return 0 <= pos[0] < n  and 0 <= pos[1] < n



def raichu_create(board,N):
    for i in range(0,N):
        if board[0][i] in "wW":
            board[0][i]="@"
    for i in range(N-1,-1,-1):
        if board[N-1][i] in "bB":
            board[N-1][i]="$"
    return board
    
def pichu_moves_white(board,N,player):
    pichu_loc_list=find_loc_pichu_white(board)
    succ=[]
    valid_moves=[]    
    board_new = copy.deepcopy(board)
    row=0
    col=0

    for row,col in pichu_loc_list:
        board_new = copy.deepcopy(board)
        
        if valid_index((row+1,col-1),N):
            if(board_new[row+1][col-1]  in "."):
                if(row+1==7):
                    board_new[row+1][col-1]="@"
                    board_new[row][col]="."
                else:
                    board_new[row+1][col-1]="w"
                    board_new[row][col]="."

                #print(print_board(board_new,N))
                succ.append(board_new)
            elif board_new[row+1][col-1]  in "b" and valid_index((row+2,col-2),N) :
                if board_new[row+2][col-2] in ".":
                    if (row+2==7):
                        board_new[row+2][col-2]="@"
                        board_new[row][col]="."
                        board_new[row+1][col-1]="."
                        
                    else:

                        board_new[row+2][col-2]="w"
                        board_new[row][col]="."
                        board_new[row+1][col-1]="."
                else:
                    continue
                #print(print_board(board_new,N))
                succ.append(board_new)
    

    for row,col in pichu_loc_list:
        board_new = copy.deepcopy(board)
        if valid_index((row+1,col+1),N):
            if(board_new[row+1][col+1]  in "."):
                if(row+1==7):
                    board_new[row+1][col+1]="@"
                    board_new[row][col]="."
                else:
                    board_new[row+1][col+1]="w"
                    board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif board_new[row+1][col+1]  in "b" and valid_index((row+2,col+2),N) :
                if board_new[row+2][col+2] in ".":
                    if (row+2==7):
                        board_new[row+2][col+2]="@"
                        board_new[row][col]="."
                        board_new[row+1][col+1]="."
                        
                    else:
                        board_new[row+2][col+2]="w"
                        board_new[row][col]="."
                        board_new[row+1][col+1]="."
                else: 
                    continue
                    #print(print_board(board_new,N))
                succ.append(board_new)
    return succ
    

       
def pichu_moves_black(board,N,player):
    pichu_loc_list=find_loc_pichu_black(board)
    succ=[]
    valid_moves=[]    
    row=0
    col=0
    for row,col in pichu_loc_list:
        board_new = copy.deepcopy(board)
        
        if valid_index((row-1,col-1),N):
            if(board_new[row-1][col-1]  in "."):
                if(row-1==0):
                    board_new[row-1][col-1]="$"
                    board_new[row][col]="."
                else:
                    board_new[row-1][col-1]="b"
                    board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif board_new[row-1][col-1]  in "w" and valid_index((row-2,col-2),N):
                if board_new[row-2][col-2] in ".":
                    if (row-2==0):
                        board_new[row-2][col-2]="@"
                        board_new[row][col]="."
                        board_new[row-1][col-1]="."
                    else:
                        board_new[row-2][col-2]="b"
                        board_new[row][col]="."
                        board_new[row-1][col-1]="."
                #print(print_board(board_new,N))
                else: 
                    continue
                succ.append(board_new)

    for row,col in pichu_loc_list:
        board_new = copy.deepcopy(board)
        if valid_index((row-1,col+1),N):
            if(board_new[row-1][col+1]  in "."):
                if(row-1==0):
                    board_new[row-1][col+1]="$"
                    board_new[row][col]="."
                else:
                    board_new[row-1][col+1]="b"
                    board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif board_new[row-1][col+1]  in "w" and valid_index((row-2,col+2),N):
                if board_new[row-2][col+2] in ".":
                    if(row-1==0):
                        board_new[row-2][col+2]="$"
                        board_new[row][col]="."
                    else:
                        board_new[row-2][col+2]="b"
                        board_new[row][col]="."
                        board_new[row-1][col+1]="."
                else: 
                    continue
                    #print(print_board(board_new,N))
                succ.append(board_new)

    return succ
    

def pikachu_moves_white(board,N,player):
    pikachu_loc_list=find_loc_pikachu_white(board)
    succ=[]
    valid_moves=[]    
    board_new = copy.deepcopy(board)
    row=0
    col=0
    ###########################################
    #below
    
    for row,col in pikachu_loc_list:  
        
        board_new = copy.deepcopy(board)  
                               
        if valid_index((row+1,col),N):                                    
            if(board_new[row+1][col]  in "."):
                if(row+1==7):
                    board_new[row+1][col]="@"
                    board_new[row][col]="."
                else:
                    board_new[row+1][col]="W"
                    board_new[row][col]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        elif board_new[row+1][col]  in "bB" and valid_index((row+2,col),N) :
            if board_new[row+2][col] == '.':
                if(row+2==7):
                    board_new[row+2][col]="@"
                    board_new[row][col]="."
                    board_new[row+1][col]="."
                else:
                    board_new[row+2][col]="W"
                    board_new[row][col]="."
                    board_new[row+1][col]="."
                if valid_index((row+3,col),N) and board_new[row+3][col] == '.':
                    board_new[row+3][col]="W"
                    board_new[row][col]="."
                    board_new[row+1][col]="."
            #print(print_board(board_new,N))
            succ.append(board_new)

        if valid_index((row+2,col),N):
             if(board_new[row+1][col]  in "."):
                if board_new[row+2][col] == '.':
                    if(row+2==7):
                        board_new[row+2][col]="@"
                        board_new[row][col]="."
                    else:
                        board_new[row+2][col]="W"
                        board_new[row][col]="."
                elif (board_new[row+2][col]  in "bB"):
                    if valid_index((row+3,col),N) and board_new[row+3][col] == '.':

                        board_new[row+3][col]="W"
                        board_new[row][col]="."
                        board_new[row+2][col]="."
                        
        

    #################################################
    #right
    for row,col in pikachu_loc_list:
        board_new = copy.deepcopy(board)
        if valid_index((row,col+1),N) and board_new[row][col+1]  in "bB" and valid_index((row,col+2),N) and board_new[row][col+2]  in "." :
            board_new[row][col+2]="W"
            board_new[row][col]="."
            board_new[row][col+1]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        elif valid_index((row,col+1),N) and board_new[row][col+1]  in "." and valid_index((row,col+2),N) and board_new[row][col+2]  in "bB" and  valid_index((row,col+3),N) and board_new[row][col+2] in ".":
            board_new[row][col+3]="W"
            board_new[row][col]="."
            board_new[row][col+2]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
      
        else:
            if valid_index((row,col+1),N) and  board_new[row][col+1] in "." :

                board_new[row][col+1]="W"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            
            board_new = copy.deepcopy(board)
            if valid_index((row,col+2),N) and board_new[row][col+2] in "." :
                board_new[row][col+2]="W"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)

    #######################################################
    #left
    for row,col in pikachu_loc_list:
        board_new = copy.deepcopy(board)
        if valid_index((row,col-1),N) and board_new[row][col-1]  in "bB" and valid_index((row,col-2),N) and  board_new[row][col-2]  in "." :
            board_new[row][col-2]="W"
            board_new[row][col]="."
            board_new[row][col-1]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        elif valid_index((row,col-1),N) and board_new[row][col-1]  in "." and valid_index((row,col-2),N) and board_new[row][col-2]  in "bB" and valid_index((row,col-3),N) and board_new[row][col-2] in ".":
            board_new[row][col-3]="W"
            board_new[row][col]="."
            board_new[row][col-2]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        
        else:
            if valid_index((row,col-1),N) and  board_new[row][col-1] in "." :

                board_new[row][col-1]="W"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            
            board_new = copy.deepcopy(board)
            if valid_index((row,col-2),N) and board_new[row][col-2] in "." :
                board_new[row][col-2]="W"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)

 

    return succ








def pikachu_moves_black(board,N,player):
    pikachu_loc_list=find_loc_pikachu_black(board)
    succ=[]
    valid_moves=[]    
    board_new = copy.deepcopy(board)
    row=0
    col=0
    ###########################################
    #top
    
    for row,col in pikachu_loc_list:
        board_new = copy.deepcopy(board)

        if valid_index((row-1,col),N):                                    
            if(board_new[row-1][col]  in "."):
                if(row-1==0):
                    board_new[row-1][col]="$"
                    board_new[row][col]="."
                else:
                    board_new[row-1][col]="B"
                    board_new[row][col]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        elif board_new[row-1][col]  in "wW" and valid_index((row-2,col),N) :
            if board_new[row-2][col] == '.':
                if(row-2==0):
                    board_new[row-2][col]="$"
                    board_new[row][col]="."
                    board_new[row-1][col]="."
                else:
                    board_new[row-2][col]="B"
                    board_new[row][col]="."
                    board_new[row-1][col]="."
                if valid_index((row-3,col),N) and board_new[row-3][col] == '.':
                    board_new[row-3][col]="B"
                    board_new[row][col]="."
                    board_new[row+1][col]="."
            #print(print_board(board_new,N))
            succ.append(board_new)

        if valid_index((row-2,col),N):
             if(board_new[row-1][col]  in "."):
                if board_new[row-2][col] == '.':
                    if(row-2==0):
                        board_new[row-2][col]="$"
                        board_new[row][col]="."
                    else:
                        board_new[row-2][col]="B"
                        board_new[row][col]="."
                elif (board_new[row-2][col]  in "wW"):
                    if valid_index((row-3,col),N) and board_new[row-3][col] == '.':

                        board_new[row-3][col]="B"
                        board_new[row][col]="."
                        board_new[row-2][col]="."
                        
        
        
                
    #################################################
    #right
    for row,col in pikachu_loc_list:
        board_new = copy.deepcopy(board)
        if valid_index((row,col+1),N) and board_new[row][col+1]  in "wW" and valid_index((row,col+2),N) and board_new[row][col+2]  in "." :
                
            board_new[row][col+2]="B"
            board_new[row][col]="."
            board_new[row][col+1]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        elif valid_index((row,col+1),N) and board_new[row][col+1]  in "." and valid_index((row,col+2),N) and board_new[row][col+2]  in "wW" and  valid_index((row,col+3),N) and board_new[row][col+2] in ".":
            board_new[row][col+3]="B"
            board_new[row][col]="."
            board_new[row][col+2]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
      
        else:
            if valid_index((row,col+1),N) and  board_new[row][col+1] in "." :

                board_new[row][col+1]="B"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            
            board_new = copy.deepcopy(board)
            if valid_index((row,col+2),N) and board_new[row][col+2] in "." :
                board_new[row][col+2]="B"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
       
    ###################################################
    #left
    for row,col in pikachu_loc_list:
        board_new = copy.deepcopy(board)
        if valid_index((row,col-1),N) and board_new[row][col-1]  in "wW" and valid_index((row,col-2),N) and  board_new[row][col-2]  in "." :
            board_new[row][col-2]="B"
            board_new[row][col]="."
            board_new[row][col-1]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        elif valid_index((row,col-1),N) and board_new[row][col-1]  in "." and valid_index((row,col-2),N) and board_new[row][col-2]  in "wW" and valid_index((row,col-3),N) and board_new[row][col-2] in ".":
            board_new[row][col-3]="B"
            board_new[row][col]="."
            board_new[row][col-2]="."
            #print(print_board(board_new,N))
            succ.append(board_new)
        
        else:
            if valid_index((row,col-1),N) and  board_new[row][col-1] in "." :

                board_new[row][col-1]="B"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            
            board_new = copy.deepcopy(board)
            if valid_index((row,col-2),N) and board_new[row][col-2] in "." :
                board_new[row][col-2]="B"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
    return succ

def raichu_moves_white(board,N,player):
    raichu_loc_list=find_loc_raichu_white(board)
    succ=[]
    #forward
    for row,col in raichu_loc_list:
        for i in range(row+1, N):
            board_new = copy.deepcopy(board)
            if  valid_index((i,col),N) and board[i][col]==".":
           
                board_new[i][col]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((i,col),N) and board_new[i][col] in "bB$":
                
                j=i+1
                while( valid_index((j,col),N) and board_new[j][col] in "."):
                    
                    board_new[j][col]="@"
                    board_new[row][col]="."
                    board_new[i][col]="."
                    for k in range(i,j):
                        board_new[k][col]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j+=1

                else:
                    break
            else:
                break
            
    #backward
        for i in range(row-1, -1, -1):
            board_new = copy.deepcopy(board)
            if  valid_index((i,col),N) and board_new[i][col]==".":
                board_new[i][col]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((i,col),N) and board_new[i][col] in "bB$":
                j=i-1
                while( valid_index((j,col),N) and board_new[j][col] in "."):
                    
                    board_new[j][col]="@"
                    board_new[row][col]="."
                    board_new[i][col]="."
                    
                    for k in range(i,j,-1):
                        board_new[k][col]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j-=1

                else:
                    break
            else:
                break
                

    #left
        for i in range(col-1, -1, -1):
            board_new = copy.deepcopy(board)
            if valid_index((row,i),N)  and board_new[row][i]==".":
                board_new[row][i]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif board_new[row][i] in "bB$":
                j=i-1
                while( valid_index((row,j),N) and board_new[row][j] in "."):
                    board_new[row][j]="@"
                    board_new[row][col]="."
                    board_new[row][i]="."
                    for k in range(i,j,-1):
                        board_new[row][k]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j-=1

                else:
                    break
            else:
                break
   
           

    
    # going right
        for i in range(col+1, N):
            
            board_new = copy.deepcopy(board)
            if board_new[row][i]==".":
                board_new[row][i]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)

            elif board_new[row][i] in "bB$":
                j=i+1
                while( valid_index((row,j),N) and board_new[row][j] in "."):
                    board_new[row][j]="@"
                    board_new[row][col]="."
                    board_new[row][i]="."
                    for k in range(i,j):
                        board_new[row][k]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j+=1

                else:
                    break
            else:
                break
   


    # diagonally going forward left
        ro=row
        column=col
        while (ro+1<= N-1 and column-1>=0):
            ro += 1
            column -= 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "bB$":
                removeRow = ro
                removeColumn = column
                while (ro+1<= N-1 and column-1>=0):
                    ro += 1
                    column -= 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="@"
                        board_new[row][col]="."
                        board_new[removeRow][removeColumn]="."
                        for l,k in zip(range(row,ro),range(col,column,-1)):
                            board_new[l][k]="."
                        #print(print_board(board_new,N))
                        succ.append(board_new)
                        
                    else:
                        
                        ro= N
                        column = -1
                        break

            else:
                break
        
        # diagonally going forward right
        ro=row
        column=col
        while (ro+1<= N-1 and column+1<=N):
            ro += 1
            column += 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "bB$":
                removeRow = ro
                removeColumn = column
                while (ro+1<= N-1 and column+1<=N-1):
                    ro += 1
                    column += 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="@"
                        board_new[row][col]="."
                        board_new[removeRow][removeColumn]="."
                        #print(print_board(board_new,N))
                        for l,k in zip(range(row,ro),range(col,column)):
                            board_new[l][k]="."
                        succ.append(board_new)
                        
                    else:
                        
                        ro= N
                        column = N
                        break

            else:
                break
        
        # diagonally going backward left
        ro=row
        column=col
        while (ro-1>=0 and column-1>=0):
            ro -= 1
            column -= 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "bB$":
                removeRow = ro
                removeColumn = column
                while (ro-1>=0 and column-1>=0):
                    ro -= 1
                    column -= 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="@"
                        board_new[row][col]="."
                        board_new[removeRow][removeColumn]="."
                        #print(print_board(board_new,N))
                        for l,k in zip(range(row,ro,-1),range(col,column,-1)):
                            board_new[l][k]="."
                        succ.append(board_new)
                        
                    else:
                        
                        ro= -1
                        column = -1
                        break

            else:
                break

        # diagonally going backward right
        ro=row
        column=col
        while (ro-1>=0 and column-1<=N-1):
            ro -= 1
            column += 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="@"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "bB$":
                removeRow = ro
                removeColumn = column
                while (ro-1>=0 and column+1<=N-1):
                    ro -= 1
                    column += 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="@"
                        board_new[row][col]="."
                        board_new[removeRow][removeColumn]="."
                        #print(print_board(board_new,N))
                        for l,k in zip(range(row,ro,-1),range(col,column)):
                            board_new[l][k]="."
                        succ.append(board_new)
                       
                    else:
                        
                        ro= -1
                        column = N
                        break

            else:
                break
    return succ



def raichu_moves_black(board,N,player):
    raichu_loc_list=find_loc_raichu_black(board)
    succ=[]
    #backward
    for row,col in raichu_loc_list:
        for i in range(row+1, N):
            board_new = copy.deepcopy(board)
            if  valid_index((i,col),N) and board[i][col]==".":
                
                board_new[i][col]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((i,col),N) and board_new[i][col] in "wW@":
                
                j=i+1
                while( valid_index((j,col),N) and board_new[j][col] in "."):
                    
                    board_new[j][col]="$"
                    board_new[row][col]="."
                    board_new[i][col]="."
                    for k in range(i,j):
                        board_new[k][col]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j+=1

                else:
                    break
            else:
                break
            
    #forward
        for i in range(row-1, -1, -1):
            board_new = copy.deepcopy(board)
            if  valid_index((i,col),N) and board_new[i][col]==".":
                board_new[i][col]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((i,col),N) and board_new[i][col] in "wW@":
                
                j=i-1
                while( valid_index((j,col),N) and board_new[j][col] in "."):
                  
                    board_new[j][col]="$"
                    board_new[row][col]="."
                    board_new[i][col]="."
                    for k in range(i,j,-1):
                        board_new[k][col]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j-=1

                else:
                    break
            else:
                break
                

    #left
        for i in range(col-1, -1, -1):
            board_new = copy.deepcopy(board)
            if valid_index((row,i),N)  and board_new[row][i]==".":
                board_new[row][i]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif board_new[row][i] in "wW@":
                j=i-1
                while( valid_index((row,j),N) and board_new[row][j] in "."):
                    board_new[row][j]="$"
                    board_new[row][col]="."
                    board_new[row][i]="."
                    for k in range(i,j,-1):
                        board_new[row][k]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j-=1

                else:
                    break
            else:
                break
   
           

    
    # going right
        for i in range(col+1, N):
            
            board_new = copy.deepcopy(board)
            if board_new[row][i]==".":
                board_new[row][i]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)

            elif board_new[row][i] in "wW@":
                j=i+1
                while( valid_index((row,j),N) and board_new[row][j] in "."):
                    board_new[row][j]="$"
                    board_new[row][col]="."
                    board_new[row][i]="."
                    for k in range(i,j):
                        board_new[row][k]="."
                    #print(print_board(board_new,N))
                    succ.append(board_new)
                    j+=1

                else:
                    break
            else:
                break
   


    # diagonally going backward left
        ro=row
        column=col
        while (ro+1<= N-1 and column-1>=0):
            ro += 1
            column -= 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "wW@":
                removeRow = ro
                removeColumn = column
                while (ro+1<= N-1 and column-1>=0):
                    ro += 1
                    column -= 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="$"
                        board_new[row][col]="."
                        board_new[removeRow][removeColumn]="."
                        for l,k in zip(range(row,ro),range(col,column,-1)):
                            board_new[l][k]="."
                        #print(print_board(board_new,N))
                        succ.append(board_new)
                        
                    else:
                        
                        ro= N
                        column = -1
                        break

            else:
                break
        
        # diagonally going backward right
        ro=row
        column=col
        while (ro+1<= N-1 and column+1<=N):
            ro += 1
            column += 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "wW@":
                del_row = ro
                del_col = column
                while (ro+1<= N-1 and column+1<=N):
                    ro += 1
                    column += 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="$"
                        board_new[row][col]="."
                        board_new[del_row][del_col]="."
                        for l,k in zip(range(row,ro),range(col,column)):
                            board_new[l][k]="."
                        #print(print_board(board_new,N))
                        succ.append(board_new)
                        
                    else:
                        
                        ro= N
                        column = N
                        break

            else:
                break
        
        # diagonally going forward left
        ro=row
        column=col
        while (ro-1>=0 and column-1>=0):
            ro -= 1
            column -= 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "wW@":
                del_row = ro
                del_col = column
                while (ro-1>=0 and column-1>=0):
                    ro -= 1
                    column -= 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="$"
                        board_new[row][col]="."
                        board_new[del_row][del_col]="."
                        #print(print_board(board_new,N))
                        for l,k in zip(range(row,ro,-1),range(col,column,-1)):
                            board_new[l][k]="."
                        succ.append(board_new)
                        
                    else:
                        
                        ro= -1
                        column = -1
                        break

            else:
                break

        # diagonally going forward right
        ro=row
        column=col
        while (ro-1>=0 and column-1<=N-1):
            ro -= 1
            column += 1
            board_new = copy.deepcopy(board)
            if valid_index((ro,column),N) and board_new[ro][column] == ".":
                board_new[ro][column]="$"
                board_new[row][col]="."
                #print(print_board(board_new,N))
                succ.append(board_new)
            elif valid_index((ro,column),N)  and board_new[ro][column] in "wW@":
                del_row = ro
                del_col = column
                while (ro-1>=0 and column+1<=N-1):
                    ro -= 1
                    column += 1
                    if board_new[ro][column]==".":
                        board_new[ro][column]="$"
                        board_new[row][col]="."
                        board_new[del_row][del_col]="."
                        ##print(print_board(board_new,N))
                        for k in range(i,j,-1):
                            board_new[k][col]="."
                        succ.append(board_new)
                        for l,k in zip(range(row,ro,-1),range(col,column)):
                            board_new[l][k]="."
                    else:
                        
                        ro= -1
                        column = N
                        break

            else:
                break
    return succ

import time
def successors(board, player,N):

    
    a=time.time()
    successor = []
    if player == "w":
        successor= pichu_moves_white(board,N,player)
        successor.extend(pikachu_moves_white(board,N,player))
        successor.extend(raichu_moves_white(board,N,player))
       
            
    else:
        successor= pichu_moves_black(board,N,player)
        successor.extend(pikachu_moves_black(board,N,player))
        successor.extend(raichu_moves_black(board,N,player))
        
        
    b=time.time()
    c=a-b
    #print("time for succc",c)
    
    return successor

import numpy as np

def evalulation_function(board_input, player):
    # calculate the heuristic according to the given board and player
    board=np.matrix(board_input)
    N = board.shape[0]

    count_ppichus = np.char.count(board,"w")
    sum_player_pichus = np.sum(count_ppichus)

    count_ppikachus = np.char.count(board, "W")
    sum_player_pikachus = np.sum(count_ppikachus)

    count_praichus = np.char.count(board, "@")
    sum_player_raichus = np.sum(count_praichus)

    count_opichus = np.char.count(board, "b")
    sum_opponent_pichus = np.sum(count_opichus)

    count_opikachus = np.char.count(board,"B")
    sum_opponent_pikachus = np.sum(count_opikachus)
    
    count_oraichus = np.char.count(board, "$")
    sum_opponent_raichus = np.sum(count_oraichus)

    pichu_weight = 20
    pikachu_weight = 50
    raichu_weight = 80
    

    evaluated_value =   pichu_weight * (sum_player_pichus - sum_opponent_pichus) + pikachu_weight * (sum_player_pikachus - sum_opponent_pikachus) + raichu_weight * (sum_player_raichus - sum_opponent_raichus) 
    
    sum_of_player_rows = 0 
    if player == "w" or player == "W" or player =="@":
        temp1 = find_loc_pichu_white(board_input) + find_loc_pikachu_white(board_input) + find_loc_raichu_white(board_input)
        #print(temp1)
        for i in range(len(temp1)):
            sum_of_player_rows = sum_of_player_rows + temp1[i][0]
    elif player == "b" or player == "B" or player == "$":
        temp2 = find_loc_pichu_black(board_input) + find_loc_pikachu_black(board_input) + find_loc_raichu_black(board_input)
        for i in range(len(temp2),-1,-1):
            sum_of_player_rows = sum_of_player_rows + temp2[i][0]  
    
    evaluated_value = evaluated_value + sum_of_player_rows
    
    return evaluated_value

def find_loc_raichu_white(board):
    pichu_loc=[]
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] in '@':
                pichu_loc.append((r,c))
    return pichu_loc


def find_loc_raichu_black(board):
    pichu_loc=[]
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] in '$':
                pichu_loc.append((r,c))
    return pichu_loc


def find_loc_pichu_white(board):
    pichu_loc=[]
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] in 'w':
                pichu_loc.append((r,c))
    return pichu_loc





def find_loc_pichu_black(board):
    pichu_loc=[]
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] in 'b':
                pichu_loc.append((r,c))
    return pichu_loc


def find_loc_pikachu_white(board):
    pichu_loc=[]
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] in 'W':
                pichu_loc.append((r,c))
    return pichu_loc

def find_loc_pikachu_black(board):
    pichu_loc=[]
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] in 'B':
                pichu_loc.append((r,c))
    return pichu_loc


 # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    #board = board.split("'")[1]

def check_goal_state(board):
    
    
    count_ppichus = np.char.count(board,"w")
    count_ppikachus = np.char.count(board, "W")
    count_praichus = np.char.count(board, "@")
    count_opichus = np.char.count(board, "b")
    count_opikachus = np.char.count(board,"B")
    count_oraichus = np.char.count(board, "$")

    white_pawn_count = np.sum(count_ppichus) + np.sum(count_ppikachus) + np.sum(count_praichus)
    black_pawn_count = np.sum(count_opichus) + np.sum(count_opikachus) + np.sum(count_oraichus)
    
    
    if white_pawn_count==0 or black_pawn_count==0:
        return True
    else:
        return False

def min_value(board, player, h, alpha, beta):
    if h==0 or check_goal_state(board):
        return evalulation_function(board, player)
    else:
        for successor in successors(board, player,N):
            lst2=[]
            lst2.append(max_value(successor, player, h-1, alpha, beta))
            beta = min(lst2)
        if alpha >= beta:
            return beta
        return beta  
    
def max_value(board, player, h, alpha, beta):
    if h==0 or check_goal_state(board):
        return evalulation_function(board, player)
    # terminating condition can be when all the pieces of a player is removed 
    else:
        for successor in successors(board, player,N):
            lst=[]
            lst.append(min_value(successor, player, h-1, alpha, beta))
        alpha = max(lst)
        if alpha >= beta:
            return alpha
        return alpha
    

def minimax(board, h, player):
    # with depth limitation and alpha beta pruning
    res = ()
    lst3=[]
    for successor in successors(board, player,N):
        res = (min_value(successor, player, h-1, -np.inf, np.inf), successor)
        lst3.append(res)
    return max(lst3, key = s_key)[1]

def s_key(tup):
    return tup[0]

def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    #board = board.split("'")[1]
    board_arr = np.array([list(board[i:i+N]) for i in range(0, len(board), N)]) # converting the flattened board in str format to 2d array

    horizon=3
    next_best_board =  minimax(board_arr, horizon, player)
    board = "".join([s for s in next_best_board.flatten()])
    yield board

if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")
    #find_best_move(board, N, player, timelimit)
    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    
    #print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
       print(new_board)
