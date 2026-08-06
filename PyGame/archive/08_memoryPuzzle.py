import pygame, sys, random
from pygame.locals import *

FPS = 30
WIN_WIDTH = 640
WIN_HEIGHT = 480
REVEAL_SPEED = 8
BOX_SIZE = 40
GAP_SIZE = 10
BOARD_WIDTH = 4
BOARD_HEIGHT = 4
assert (BOARD_WIDTH * BOARD_HEIGHT) %2 == 0, "Board needs to have an even number of boxes for pairs of matches."
X_MARGIN = int((WIN_WIDTH - (BOARD_WIDTH * (BOX_SIZE + GAP_SIZE))) / 2)
Y_MARGIN = int((WIN_HEIGHT - (BOARD_HEIGHT * (BOX_SIZE + GAP_SIZE))) / 2)

# Colors        r    g    b
GRAY        = (100, 100, 100)
NAVY_BLUE   = ( 60,  60, 100)
WHITE       = (255, 255, 255)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
BLUE        = (  0,   0, 255)
YELLOW      = (255, 255,   0)
ORANGE      = (255, 128,   0)
PURPLE      = (255,   0, 255)
CYAN        = (  0, 255, 255)

BgColor = NAVY_BLUE
LightBgColor = GRAY
BoxColor = WHITE
HighLightColor = BLUE

DONUT = "donut" 
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"

AllColors = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
AllShapes = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(AllColors) * len(AllShapes) * 2 >= BOARD_WIDTH * BOARD_HEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global fpsClock, screen
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    mouseX = 0
    mouseY = 0
    
    pygame.display.set_caption("Memory Puzzle")

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    
    firstSelection = None
    
    screen.fill(BgColor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False
        
        screen.fill(BgColor)
        drawBoard(mainBoard, revealedBoxes)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True
                
        boxX, boxY = getBoxAtPixel(mouseX, mouseY)
        if boxX != None and boxY != None:
            # the mouse is currently over a box.
            if not revealedBoxes[boxX][boxY]:
                drawHighlightBox(boxX, boxY)
            if not revealedBoxes[boxX][boxY] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxX, boxY)])
                revealedBoxes[boxX][boxY] = True # set the box as "revealed"
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxX, boxY)
                else: # the current box was the second one to be clicked
                    # check if there is a match between the two icons
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxX, boxY)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # icons don't match. Re-cover both selections
                        pygame.time.wait(1000) # wait 1s in milliseconds
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxX, boxY)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxX][boxY] = False
                    elif hasWon(revealedBoxes): # check if all pairs found
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)
                        
                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation
                        startGameAnimation(mainBoard)
                    firstSelection = None # reset firstSelection variable
                    
        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        fpsClock.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARD_WIDTH):
        revealedBoxes.append([val] * BOARD_HEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = [] 
    for color in AllColors:
        for shape in AllShapes:
            icons.append((shape, color))

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARD_WIDTH * BOARD_HEIGHT / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)
    
    # create the board data structure, with randomly placed icons
    board = []
    for x in range(BOARD_WIDTH):
        column = []
        for y in range(BOARD_HEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner list have a most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append((theList[i:i + groupSize]))
    return result


def leftTopCoordsOfBox(boxX, boxY):
    # convert board coordinates to pixel coordinates
    left = boxX * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    top = boxY * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    return(left, top)


def getBoxAtPixel(x, y):
    for boxX in range(BOARD_WIDTH):
        for boxY in range(BOARD_HEIGHT):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            boxRect = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            if boxRect.collidepoint(x, y):
                return( boxX, boxY)
    return( None, None)


def drawIcon(shape, color, boxX, boxY):
    quarter =   int(BOX_SIZE * 0.25)
    half =      int(BOX_SIZE * 0.5)

    left, top = leftTopCoordsOfBox(boxX, boxY)
    # draw the shape
    if shape == DONUT:
        pygame.draw.circle(screen, color, (left + half, top + half), half - 5)
        pygame.draw.circle(screen, BgColor, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(screen, color, (left + quarter, top + quarter, BOX_SIZE - half, BOX_SIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(screen, color, ((left + half, top), (left + BOX_SIZE - 1, top + half), 
                                            (left + half, top + BOX_SIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.line(screen, color, (left, top + i), (left + i, top))
            pygame.draw.line(screen, color, (left + i, top + BOX_SIZE - 1), (left + BOX_SIZE - 1, top + 1))
    elif shape == OVAL:
        pygame.draw.ellipse(screen, color, (left, top + quarter, BOX_SIZE, half))

        
def getShapeAndColor(board, boxX, boxY):
    # shape value for x, y spot is stored in board [x][y][0]
    # color value for x, y spot is stored in board [x][y][1]
    return board[boxX][boxY][0], board[boxX][boxY][1]


def drawBoxCovers(board, boxes, coverage):
    # draws boxes being covered/revealed. "boxes" is a list
    # of two - item lists, which have the x & y spot of the box
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(screen, BgColor, (left, top, BOX_SIZE, BOX_SIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(screen, BoxColor, (left, top, coverage, BOX_SIZE))
    pygame.display.update()
    fpsClock.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # do the "box reveal" animation
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, - REVEAL_SPEED):
        drawBoxCovers(board, boxesToReveal, coverage)
        

def coverBoxesAnimation(board, boxesToCover):
    # do the "cover boxes" animation
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        drawBoxCovers(board, boxesToCover, coverage)
        
        
def drawBoard(board, revealed):
    # draws all of the boxes in their covered or revealed state
    for boxX in range(BOARD_WIDTH):
        for boxY in range(BOARD_HEIGHT):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            if not revealed[boxX][boxY]:
                # draw covered box
                pygame.draw.rect(screen, BoxColor, (left, top, BOX_SIZE, BOX_SIZE))
            else:
                # draw the revealed icon
                shape, color = getShapeAndColor(board, boxX, boxY)
                drawIcon(shape, color, boxX, boxY)

                
def drawHighlightBox(boxX, boxY):
    left, top = leftTopCoordsOfBox(boxX, boxY)
    pygame.draw.rect(screen, HighLightColor, (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE +10), 4)

    
def startGameAnimation(board):
    # randomly reveal the boxes 8 at a time
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            boxes.append((x,y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)
        
        
def gameWonAnimation(board):
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LightBgColor
    color2 = BgColor
    
    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        screen.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)

        
def hasWon(revealedBoxes):
    # return True if all the boxes has been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            return False # return False if any boxes are covered
    return True

if __name__ == "__main__":
    main()