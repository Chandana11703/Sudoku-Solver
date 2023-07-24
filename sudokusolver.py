import sudokubrute as sbf
import socket
import multiprocessing
import time

class sudoku_solver:

    sudoku=[]
    #This function of the sudoku class takes the sudoku list and displays on the screen

    def display(self):
        print("The solved sudoku is")
        for i in range(9):
            for j in range(9):
                print(self.sudoku[i][j],end=" ")
            print()

    #This functions checks the number whether it is  present in the given row or not
   
    def not_inrow(self,row,value,occurence=0):
        occ=0
        for i in range(9):
            if(self.sudoku[row][i]==value):
                occ=occ+1
            else:
                continue
        if(occ<=occurence):
            return True
        else:
            return False
    #This function checks the number whether the number is present in the given coloumn or not
    
    def not_incoloumn(self,coloumn,value,occurence=0):
        occ=0
        for i in range(9):
            if(self.sudoku[i][coloumn]==value):
                occ=occ+1
            else:
                continue
        if(occ<=occurence):
            return True
        else:
            return False
        

    #This function checks whether the given number is present in the 3*3 matrix in an order
   
    def not_inbox(self,row,coloumn,value,occurence=0):
        occ=0
        r=int(row/3)
        c=int(coloumn/3)
        for i in range(3):
            for j in range(3):
                if(self.sudoku[(3*r)+i][(3*c)+j]==value):
                    occ=occ+1
                else:
                    continue
        if(occ<=occurence):
            return True
        else:
            return False

    #This function is designed to fill the all the empty boxes with the basic rules of the sudoku game 
    
    def basic_filling(self):
        for i in range(9):
            for j in range(9):
                if(self.sudoku[i][j]==0):
                    repeat=0
                    value=0
                    for k in range(1,10):
                        if((self.not_inrow(i,k)) and self.not_incoloumn(j,k) and self.not_inbox(i,j,k)):
                            repeat=repeat+1
                            value=k
                        else:
                            continue
                    if(repeat==1):
                        self.sudoku[i][j]=value
                        
    #This checks the rows coloums and boxes simultaneously so that different possibilities can be eliminated and the boxes can be filled as the game advances
    
    def mainfilling(self):
        for i in range(9):
            for j in range(9):
                if(self.sudoku[i][j]==0):
                    for k in range(1,10):
                        if(self.not_inbox(i,j,k)):
                            r=int(i/3)
                            c=int(j/3)
                            count1=0
                            count2=0
                            for p in range(3):
                                if(c+p!=j and (not(self.not_incoloumn(c+p,k)) or (self.sudoku[r][c+p]!=0 and self.sudoku[r+1][c+p]!=0 and self.sudoku[r+2][c+p]!=0))):count1=count1+1
                                if(r+p!=i and (self.sudoku[r+p][j]!=0 or not(self.not_inrow(r+p,k)))):count1=count1+1

                                if(r+p!=i and (self.not_inrow(r+p,k) or (self.sudoku[r+p][c]!=0 and self.sudoku[r+p][c+1]!=0 and self.sudoku[r+p][c+2]!=0))):count2=count2+1
                                if(c+p!=j and (self.sudoku[i][c+p]!=0 or not(self.not_incoloumn(c+p,k)))):count2=count2+1
                            if(count1==4 and count2==4):self.sudoku[i][j]==k

    #This function checks whether there is any empty space in the sudoku
   
    def check_zero(self):
        for i in range(9):
            for j in range(9):
                if(self.sudoku[i][j]==0):
                    return True

    #This function takes the input of the row coloumn and the value and it backtracks i.e it gives the output of whether it is correct or not
    def check_sudoku(self):
        for i in range(9):
            for j in range(9):
                if(self.sudoku[i][j]==0):
                    continue
                else:
                    if(self.not_inrow(i,self.sudoku[i][j],1) and self.not_incoloumn(j,self.sudoku[i][j],1) and self.not_inbox(i,j,self.sudoku[i][j],1)):
                        continue
                    else:
                        return False
        return True

sudoku=sudoku_solver()
s=socket.socket() #ipv4,tcp
#Socket program takes the 2 arguments types of ip address and type of connection(TCP/UDP)
#Socket program by default accepts the ipv4 address and TCP connection
s.bind(('localhost',9999))
s.listen(3)
print("Waiting for the connections")
while(1):
    c,address=s.accept()
    print("Connected with the",address)
    sudoku.sudoku=(eval(c.recv(1024).decode()))
    print("Data is received on server side succesfully")
    print(sudoku.sudoku)
    c.send(bytes("Data is received on server side succesfully","utf-8"))
    if(sudoku.check_sudoku()):
        print("Sudoku is valid") 
        for i in range(3):
            sudoku.basic_filling()
            sudoku.mainfilling()
        if(sudoku.check_zero):
            if (sbf.solveSudoku(sudoku.sudoku,0,0)):
                sudoku.display()
                print("The sudoku is solved\n\n")
            else:
                print("No solution exists")
        else:
            sudoku.display()
            print("The sudoku is solved\n\n")
        print("sending the solved sudoku")
    else:
        print("Sudoku is invalid")
        print("sending the same unsolved sudoku")
    print(sudoku.sudoku)
    c.send(bytes(str(sudoku.sudoku),'utf-8'))
    c.close()

# sudoku=sudoku_solver()
# sudoku.sudoku=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 5, 0], [5, 0, 0, 0, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# print(sudoku.check_sudoku())