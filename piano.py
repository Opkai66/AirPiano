import pygame;
from pygame.locals import *
import serial
import sys;
from playsound import playsound

ser =serial.Serial("COM7",9600)
Oflag = ser.isOpen()
if Oflag == 1:
    sys.stdout.write('open success!')
else:
    sys.stdout.write('open failed :(')

pygame.init();
pygame.mixer.init();

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Piano")

clock = pygame.time.Clock()

dflag =0
dflag_size = 50
datao = 'aipitch'    
i=0;
dex=1
data = ""
note = 0
s = 0
while True:
    while ser.inWaiting() > 0:
        for index in range(10):
            data = ser.readline()
            dflag += dflag
            # read rate control
        if data != '':
            data = bytes.decode(data)
            sys.stdout.write(data)
# input check---------------------------------
            i=data.find("+")-1
            while (data[i] >='0') & (data[i] <='9'):
              
              note += (int(data[i]))*dex
              dex=dex*10
              i=i-1
            dex=1
            if  'C' in data:
                sound=pygame.mixer.Sound("wk_mc.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if 'D' in data:
                sound=pygame.mixer.Sound("wk_md.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if 'E' in data:
                sound=pygame.mixer.Sound("wk_me.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if  'F' in data:
                sound=pygame.mixer.Sound("wk_mf.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if 'G' in data:
                sound=pygame.mixer.Sound("wk_mg.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if 'A' in datao:
                sound=pygame.mixer.Sound("wk_ma.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if 'B' in data:
                sound=pygame.mixer.Sound("wk_mb.wav");
                sound.play();
                #play sound

                pygame.display.flip()
            sys.stdout.write("%d\r\n"%(note))
            note=0
            
    for event in pygame.event.get():
        pygame.display.flip()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
   
        ''''''
        #s = data[i] - '0'
    
        #-----------key linked-------------
        if event.type == KEYDOWN:
            #if 'pitch' in datao:
                #note_1 =  True

            if event.key == K_1 or 'C' in data:
                sound=pygame.mixer.Sound("wk_mc.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if event.key == K_2 or 'D' in data:
                sound=pygame.mixer.Sound("wk_md.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if event.key == K_3 or 'E' in datao:
                sound=pygame.mixer.Sound("wk_me.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if event.key == K_4 or 'F' in datao:
                sound=pygame.mixer.Sound("wk_mf.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if event.key == K_5 or 'G' in datao:
                sound=pygame.mixer.Sound("wk_mg.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if event.key == K_6 or 'A' in datao:
                sound=pygame.mixer.Sound("wk_ma.wav");
                sound.play();
                #play sound

                pygame.display.flip()

            if event.key == K_7 or 'B' in datao:
                sound=pygame.mixer.Sound("wk_mb.wav");
                sound.play();
                #play sound

                pygame.display.flip()

        clock.tick(10)

    











                
