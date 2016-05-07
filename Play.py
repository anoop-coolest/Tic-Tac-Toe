'''
Created on 12-Sep-2015

It is a module for the player on the virtual side
'''

import random
class Player:
    def __init__(self):
        '''Set the board'''
        self.winningSet=[[0,3,6],[0,4,8],[0,1,2],[1,4,7],[2,5,8],[2,4,6],[6,7,8],[3,4,5]]
        self.lastMove=-1
        self.opponentLastMove=-1
        self.moves=[]
        self.corner=[0,2,6,8]
        self.numMoves=0
        self.opponentMoves=[]
        self.board=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.emptyPositions=[0,1,2,3,4,5,6,7,8]
        
        
    def ckeckIfWinning(self,lastMove,moves):
        ''' 
        Check if I am winning by comparing with winningSet
        For the previous entry check whether there is any way to achieve a combination in winningset
        '''
        for i in range(8):
            if lastMove in self.winningSet[i]:
                tmp=list(self.winningSet[i])
                tmp.remove(lastMove)
                for j in range(len(moves)):
                    if moves[j] in tmp:
                        tmp.remove(moves[j])
                        if tmp[0] in self.emptyPositions:
                            print("I Move To:",tmp[0])
                            return tmp[0]
        return -1
    
    
    
    
        
        
    def move(self):
        '''I move and change the board'''
        pos=Player.decideNext(self)
        self.lastMove=pos
        self.moves.append(pos)
        self.board[pos]=0
        self.numMoves=self.numMoves+1
        if self.numMoves<=8 and pos!=-1:
            try:
                self.emptyPositions.remove(pos)
                print("I move to:",pos)
                print("State of board is:",self.board)
                return Player.opponentMove(self)
            except ValueError:
                pass
        else:
            print("Match Over,state of board is:",self.board)
        
        
        
    def opponentMove(self):
        '''You move and change the board'''
        print("Where do you want to move:")
        position=int(input())
        try:
            self.emptyPositions.remove(position)
            self.opponentMoves.append(position)
            self.opponentLastMove=position
            self.board[position]=1
            self.numMoves=self.numMoves+1
        except ValueError:
            print("Position already filled,please try again")
            return Player.opponentMove(self)
        if self.numMoves>8:
            print("Game Over")
            print("State of game is:",self.board)
        else:
            return Player.move(self)
        
        
    def decideNext(self):
        '''Decide where to move next'''
        pos=Player.ckeckIfWinning(self,self.lastMove,self.moves)
        if pos!=-1:
            ''' If I am winning'''
            self.lastMove=pos
            self.moves.append(pos)
            self.board[pos]=0
            self.numMoves=self.numMoves+1
            print("I move to:",pos)
            print("I Win You Lose,hahahahahaha")
            return -1
        else:
            ''' If Not'''
            pos=Player.ckeckIfWinning(self, self.opponentLastMove, self.opponentMoves)
        if pos!=-1:
            ''' If You Are Winning Then I Have to Stop You From winning'''
            return pos 
        else:
            '''If not then play My Next Move'''
            if self.numMoves==0:
                '''Move to a corner position as it gives more advantage to win'''
                pos=self.corner[random.randint(0,len(self.corner)-1)]
            else:
                
                if ((self.lastMove+7)%8) in self.emptyPositions:
                    pos=self.emptyPositions.index((self.lastMove+7)%8)
                else:
                    pos=random.randint(0,len(self.emptyPositions)-1)
            return self.emptyPositions[pos]

        

    def startGame(self):
        '''Start The Game'''
        
        '''This is just to increase the interactivity of the game'''
        '''Actual user input wont make any difference to who is gonna start'''
        '''It would all depend on the random number generated'''
        print("Lets toss to see who moves first")
        print("Heads(H) or Tails(T)")
        a=raw_input()
        h=random.randint(0,1)
        if h==0:
            Player.opponentMove(self)
        else:
            Player.move(self)
        
        
print("Welcome to the game of tic-tac-toe in virtual World!!!")
p=Player()
p.startGame()

    
            
