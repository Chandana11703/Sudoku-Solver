import socket
import pygame
from pygame.locals import *
import time

class sudoku:
    solution=[[0 for i in range(9)] for j in range(9)]
    sudoku=[[0 for i in range(9)] for j in range(9)]
    selected=None
    done=0
    start=None
    play_time=None
    final_time=None

    def request(self):
        c=socket.socket()
        c.settimeout(10)
        try:
            c.connect(('localhost',9999))#127.0.0.1
        except:
            print("Check your connection with server")
        print("Connected with server")
        c.send(bytes(str(self.sudoku),'utf-8'))
        print(c.recv(1024).decode())
        print("The solved sudoku is")
        try:
            self.solution=(eval(c.recv(1024).decode()))
        except:
            print("The solution doesnot exist")
        print(self.solution)
        for i in range(9):
            for j in range(9):
                if(s.solution[i][j]==0):
                    s.done=3
                else:
                    continue

    def gui(self):
        def format_time(secs):
            sec = secs%60
            minute = secs//60
            mat = "Time  " + str(minute) + ":" + str(sec)
            return mat

        def intro():
            logo = pygame.image.load('logo.jpg')
            logo = pygame.transform.scale(logo, (450,200))
            developer_message=font1.render("Developed by",1,(0,0,0))
            name=font1.render("Narra Chandana",1,(0,0,0))
            reg=font1.render("124003065",1,(0,0,0))
            window.blit(developer_message,(170,420))
            window.blit(name,(160,450))
            window.blit(reg,(170,480))
            window.blit(logo,(0,0))

        colour=(250,250,250)
        pygame.init()
        width,height=450,450
        window=pygame.display.set_mode((width,height+70))
        pygame.display.set_caption("Fun sudoku")
        window.fill(colour)
        font1=pygame.font.SysFont('Comic Sans MS',20)
        font2=pygame.font.SysFont('Comic Sans MS',35)
        correctnumber = pygame.font.SysFont("comicsans", 40)
        wrongnumber = pygame.font.SysFont("comicsans", 40)

        intro()
        pygame.display.update()
        time.sleep(5)

        def draw_window():
            window.fill((250,250,250))
            for i in range(10):
                if(i%3==0):
                    pygame.draw.line(window,(10,10,10),((width/9)*i,0),((width/9)*i,height),5)
                    pygame.draw.line(window,(10,10,10),(0,(height/9)*i),(width,(height/9)*i),5)
                else:
                    pygame.draw.line(window,(10,10,10),((width/9)*i,0),((width/9)*i,height),2)
                    pygame.draw.line(window,(10,10,10),(0,(height/9)*i),(width,(height/9)*i),2)
            
            if(s.done==0):
                text1 = font1.render("Enter Sudoku you want to play", 1, (0,0,0))
                text2=font1.render("Click on Filled once you filled",1,(0,0,0))
                window.blit(text1,(0, 450))
                window.blit(text2,(0,482))
                done=font2.render("Filled",1,(0,0,0))
                window.blit(done,(355,455))
                pygame.draw.rect(window,(0,0,0),(350,455,100,50),2)
                for i in range(9):
                    for j in range(9):
                        if(s.sudoku[i][j]==0 or s.sudoku[i][j]==None):
                            continue
                        else:
                            number=correctnumber.render(str(s.sudoku[i][j]), 1, (0,0,0))
                            window.blit(number,((j*50)+15,(i*50)-5))
            
            elif(s.done==1):
                done=font1.render("Solution",1,(0,0,0))
                window.blit(done,(360,465))
                s.play_time = round(time.time() - s.start)
                pygame.draw.rect(window,(0,0,0),(350,455,100,50),2)
                time_message=font2.render(format_time(s.play_time), 1, (0,0,0))
                # window.blit(time_message,(10, 460))
                total=True
                for i in range(9):
                    for j in range(9):
                        if(s.sudoku[i][j]==s.solution[i][j]):
                            continue
                        else:
                            total=False
                    if total==False:
                        break
                
                if(total==True):
                    if(s.final_time==None):
                        s.final_time=time_message
                    window.fill((250,250,250))
                    nosol=font2.render("Congrats!!",1,(0,0,0))
                    window.blit(nosol,(150,200))
                    window.blit(s.final_time,(150,245))
                    s.selected=None
                else:
                    for i in range(9):
                        for j in range(9):
                            if(s.sudoku[i][j]==0 or s.sudoku[i][j]==None):
                                continue
                            elif(s.sudoku[i][j]==s.solution[i][j]):
                                number=correctnumber.render(str(s.sudoku[i][j]), 1, (0,0,0))
                                window.blit(number,((j*50)+15,(i*50)-5))
                            else:
                                number=wrongnumber.render(str(s.sudoku[i][j]), 1, (250,0,0))
                                window.blit(number,((j*50)+15,(i*50)-5))
            
            elif(s.done==2):
                for i in range(9):
                    for j in range(9):
                        number=correctnumber.render(str(s.solution[i][j]), 1, (0,0,0))
                        window.blit(number,((j*50)+15,(i*50)-5))
                final_message=font2.render("Final solution...", 1, (0,0,0))
                window.blit(final_message,(10, 460))
            
            elif(s.done==3):
                window.fill((250,250,250))
                nosol=font2.render("No solution exists!!",1,(250,0,0))
                window.blit(nosol,(80,200))
                s.selected=None
            
            if(s.selected!=None):
                pygame.draw.rect(window,(250,0,0),(s.selected[0]*50,s.selected[1]*50,50,50),3)

        def click_input():
            draw_window()
            run=True
            while run:
                draw_window()
                for event in pygame.event.get():
                    key=None
                    if event.type == pygame.QUIT:
                        run = False
                    if(event.type == pygame.KEYDOWN):
                        print("Key entered detected")
                        if event.key == pygame.K_1:
                            key = 1
                        if event.key == pygame.K_2:
                            key = 2
                        if event.key == pygame.K_3:
                            key = 3
                        if event.key == pygame.K_4:
                            key = 4
                        if event.key == pygame.K_5:
                            key = 5
                        if event.key == pygame.K_6:
                            key = 6
                        if event.key == pygame.K_7:
                            key = 7
                        if event.key == pygame.K_8:
                            key = 8
                        if event.key == pygame.K_9:
                            key = 9
                        if event.key == pygame.K_DELETE:
                            key = None
                        s.sudoku[s.selected[1]][s.selected[0]]=key
                        print(key,"appended")
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if((pos[0])>350 and (pos[0]<450) and (pos[1]>455 and pos[1]<505)):
                            print("Done working")
                            s.done=s.done+1
                            if(s.done==1):
                                s.request()
                                s.start=time.time()
                        elif(int(pos[0]/50)<9 and int(pos[1]/50)<9):
                            print("boxes working")
                            print("you clicked on ",int(pos[0]/50),int(pos[1]/50))
                            s.selected=(int(pos[0]/50),int(pos[1]/50))
                    pygame.display.update()
        click_input()
        pygame.quit()
s=sudoku()
# s.request()
s.gui()

