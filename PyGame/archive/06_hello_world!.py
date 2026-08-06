import pygame as pg
from time import sleep

pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Hello World!")

# text
fontObj = pg.font.Font(None, 70)
textSurfaceObj = fontObj.render("Hello World!", True, "#e87ffd")
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (screen.get_width() / 2, screen.get_height() * 0.4)

# music
musicFile = r"D:\Audio\0. Music\16-Bit Action\LOOP_Up for the Challenge.wav"
musicObj = pg.mixer.music
musicObj.load(musicFile)

# sound
soundFile = r"D:\Audio\0. FX\BOUZOUKI\GAME_MENU_SCORE_SFX001221.wav"
soundObj = pg.mixer.Sound(soundFile)

soundObj.play()

musicPlaying = False
def playMusic():
    sleep(3)
    musicObj.play(-1, 0.0, 2000)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill("#F4FF61")
    screen.blit(textSurfaceObj, textRectObj)
    
    pg.display.flip()
    
    if musicPlaying == False:
        musicPlaying = True
        playMusic()
    
        
    
pg.quit()
