import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #画面サイズ
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像読込
    koka = pg.image.load("fig/3.png")
    koka = pg.transform.flip(koka,True,False) #画像反転
    bg_img_han = pg.transform.flip(bg_img,True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = -(tmr % 3200)

        screen.blit(bg_img, [x, -50]) #背景画貼付
        screen.blit(bg_img_han, [x + 1600, -50])
        screen.blit(bg_img, [x + 3200, -50])
        screen.blit(koka, [300, 200])
        
        pg.display.update()     
        clock.tick(200) #fps

        #if x == -800:
        #    screen.blit(bg_img_han, [x+1600, 0])

        #if x == -3200:
        #    x = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()