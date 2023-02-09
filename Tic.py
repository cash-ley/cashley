import pygame, sys

pygame.init()

#Initialize Colors
black = (0, 0, 0)
white = (255, 255, 255)

#Set environment variables
running = True
gameended = False
#replayclick = False
turn = 'X' #Initialize x for first turn
hpos = 0 #Column
vpos = 0 #Row
count = 0
winner = False
width = 400 #Screen width/height
margin = 50 #Board margins
box = int((width - 2 * margin) / 3) #Box width/height

#Create Screen/Window
screen = pygame.display.set_mode((width, width))
screen.fill(black)
pygame.display.set_caption("Tic-Tac-Toe")

#Set font sizes
fx = pygame.font.SysFont('comic sans', 120)
fo = pygame.font.SysFont('comic sans', 120)
fc = pygame.font.SysFont('comic sans', 50)
pgo = pygame.font.SysFont('comic sans', 50)

#Set font colors
fsx = fx.render("X", True, (255, 255, 255), (0, 0, 0))
fso = fo.render("O", True, (200, 0, 0), (0, 0, 0))
fblack = fx.render("X", True, (0, 0, 0), (0, 0, 0)) #paint black over boxes

#Set up game messages
pfont = pgo.render("Play again? [Y]/[N]", True, (0, 0, 0), (255, 255, 255))
nowin = fc.render("Nobody wins.", True, (0, 0, 0), (255, 255, 255))

#Draw Board
pygame.draw.line(screen, "white", (margin + box, margin),
                 (margin + box, margin + (3 * box)), 5)
pygame.draw.line(screen, "white", (margin, margin + box),
                 (margin + (3 * box), margin + box), 5)
pygame.draw.line(screen, "white", (margin, margin + (2 * box)),
                 (margin + (3 * box), margin + (2 * box)), 5)
pygame.draw.line(screen, "white", (margin + (2 * box), margin),
                 (margin + (2 * box), margin + (3 * box)), 5)

#Initialize Game State
gamestate = ["", "", "", "", "", "", "", "", "","",""]

def advanceturn(currentturn):
  nextturn = ""
  if currentturn == "X":
    nextturn = "O"
  elif currentturn == "O":
    nextturn = "X"
  return nextturn

#Find the BoxClick findbc()
def findbc(mouseX, mouseY):
    boxclick = 0
    #global replayclick
    global running
    hpos = 0
    vpos = 0
    global gameended
    global gamestate
    global turn

    #Check to see if game is still active
    if gameended == True:
      #Game is over, check for Play Again Yes/No
      print("Checking for Y/N")
      #Check for Y/N click
      if mouseX > (206) and mouseX < (244): 
        if mouseY > (352) and mouseY < (384):
          replayclick = True
          print("Y was Clicked")
          #If yes, reset game board
          gamestate = ["", "", "", "", "", "", "", "", "","",""]
          turn ="O"
          screen.fill(black)
          pygame.draw.line(screen, "white", (margin + box, margin),
                 (margin + box, margin + (3 * box)), 5)
          pygame.draw.line(screen, "white", (margin, margin + box),
                 (margin + (3 * box), margin + box), 5)
          pygame.draw.line(screen, "white", (margin, margin + (2 * box)),
                 (margin + (3 * box), margin + (2 * box)), 5)
          pygame.draw.line(screen, "white", (margin + (2 * box), margin),
                 (margin + (2 * box), margin + (3 * box)), 5) 
          gameended = False
          print("Starting new game")
          #print(gamestate)
          #print(turn)
          boxclick = 9
          hpos = 0
          vpos = 4
      elif mouseX > (259) and mouseX < (301):
        if mouseY > (352) and mouseY < (384):
          replayclick = False
          #If No, end the game
          boxclick = 10
          hpos = 1
          vpos = 4
          running = False
    elif gameended == False: 
        #Game is running, identify the box for the click locations         
        # 0 | 3 | 6
        #-----------
        # 1 | 4 | 7
        #-----------
        # 2 | 5 | 8
        
        if mouseX < (margin + box):
          if mouseY < (margin + box):
              boxclick = 0
              hpos = 0
              vpos = 0
          elif mouseY < (margin + 2 * box):
              boxclick = 1
              hpos = 0
              vpos = 1
          elif mouseY < (margin + 3 * box):
              boxclick = 2
              hpos = 0
              vpos = 2
        elif mouseX < (margin + 2 * box):
            if mouseY < (margin + box):
              boxclick = 3
              hpos = 1
              vpos = 0
            elif mouseY < (margin + 2 * box):
              boxclick = 4
              hpos = 1
              vpos = 1
            elif mouseY < (margin + 3 * box):
              boxclick = 5
              hpos = 1
              vpos = 2
        elif mouseX < (margin + 3 * box):
          if mouseY < (margin + box):
              boxclick = 6
              hpos = 2
              vpos = 0
          elif mouseY < (margin + 2 * box):
              boxclick = 7
              hpos = 2
              vpos = 1
          elif mouseY < (margin + 3 * box):
              boxclick = 8
              hpos = 2
              vpos = 2
    return boxclick, hpos, vpos

while running:
    mouseP = ()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
            mouseP = pygame.mouse.get_pos()
            mouseX = mouseP[0]
            mouseY = mouseP[1]
            boxclick = findbc(mouseX, mouseY)
            hpos = boxclick[1]
            vpos = boxclick[2]  
            if gameended == True:
              print("Game Over")
            elif gameended == False:
              print("Turn: ", turn)
              #Check to see if it is X's turn
              if turn == 'X':
                if gamestate[boxclick[0]] == "":
                  gamestate[boxclick[0]] = "X"
                  screen.blit(fsx, (margin + 20 + (hpos*box), margin + 10 + (vpos*box)))
                  turn = advanceturn(turn)
                elif gamestate[boxclick[0]] != "":
                  print("Pick an empty box")
              #Check to see if it is O's turn
              elif turn == 'O':
                if gamestate[boxclick[0]] == "":
                  gamestate[boxclick[0]] = "O"
                  screen.blit(fso, (margin + 20 + (hpos*box), margin + 10 + (vpos*box)))
                  turn = advanceturn(turn)
                elif gamestate[boxclick[0]] != "":
                  print("Pick an empty box")

              #Check and mark winners   
              #Set congratulations text
              winner = advanceturn(turn)
              congrats = fc.render(f"Congrats! {winner} won!", True, (0, 0, 0), (255, 255, 255))
              if gamestate[0] != "":
                
                if gamestate[0] == gamestate[1] == gamestate[2]:
                  pygame.draw.line(screen, "red", (margin + 0.5*box, margin),
                   (margin + 0.5*box, margin + (3 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
                elif gamestate[0] == gamestate[3] == gamestate[6]:
                  pygame.draw.line(screen, "red", (margin + 0*box, margin+0.5*box),
                   (margin + (3*box), margin + (0.5 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
                elif gamestate[0] == gamestate[4] == gamestate[8]:
                  pygame.draw.line(screen, "red", (margin + 0*box, margin),
                   (margin + (3*box), margin + (3 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
              if gamestate[4] != "":
                #congrats = fc.render(f"Congrats! {turn} loses! Hahaha", True, (0, 0, 0), (255, 255, 255))
                if gamestate[3] == gamestate[4] == gamestate[5]:
                  pygame.draw.line(screen, "red", (margin + 1.5*box, margin),
                   (margin + 1.5*box, margin + (3 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
                elif gamestate[1] == gamestate[4] == gamestate[7]:
                  pygame.draw.line(screen, "red", (margin + 0*box, margin+1.5*box),
                   (margin + (3*box), margin + (1.5 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
                elif gamestate[2] == gamestate[4] == gamestate[6]:
                  pygame.draw.line(screen, "red", (margin + 3*box, margin),
                   (margin , margin + (3 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
              if gamestate[8] != "":
                #congrats = fc.render(f"Congrats! {turn} loses! Hahaha", True, (0, 0, 0), (255, 255, 255))
                if gamestate[2] == gamestate[5] == gamestate[8]:
                  pygame.draw.line(screen, "red", (margin + 0*box, margin+2.5*box),
                   (margin + (3*box), margin + (2.5 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
                elif gamestate[6] == gamestate[7] == gamestate[8]:
                  pygame.draw.line(screen, "red", (margin + (2.5*box), margin),
                   (margin + (2.5*box), margin + (3 * box)), 5)
                  screen.blit(congrats, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True
                elif gamestate[8] != "" and gamestate[7] != "" and gamestate[6] != ""   and gamestate[5] != "" and gamestate[4] != "" and gamestate[3] != "" and gamestate[2] != "" and gamestate[1] != "" and gamestate[0] != "" and gameended != True:
                  screen.blit(nowin, (1, 1))
                  screen.blit(pfont, (1,350))
                  gameended = True



                
    pygame.display.update()
