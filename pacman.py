#!/usr/bin/env python3

import time
import pygame
import numpy as np 
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

# fps=50
# reloj = pygame.time.Clock()

tampantalla_x=1200
tampantalla_y=700
anchocelda=40
altocelda=40
nfilas=17
ncolumnas=25
lista=[list(range(ncolumnas))for _ in range(nfilas)]
listarandom=[list(range(tampantalla_x))for _ in range(tampantalla_x)]
for i in range (tampantalla_x):
    for j in range (tampantalla_x):
            listarandom[i][j]=random.random()
listapuntos=[list(range(ncolumnas))for _ in range(nfilas)]

pygame.display.set_caption('Videojuego de Pacman de Juan')
ventana= pygame.display.set_mode((tampantalla_x,tampantalla_y))

coloreado1=pygame.Color(0,255,0)        # Verde
coloreado2=pygame.Color(255,255,0)      # Amarillo
coloreado3=pygame.Color(0,255,255)      # Cyan
coloreado4=pygame.Color(0,0,255)        # Azul

colorfondo=pygame.Color(0,0,0)          # Negro
coloreado5=pygame.Color(50,50,50)       # Gris
colorComecoco=pygame.Color(255,255,0)   # Comecoco
colorPinky=pygame.Color(255,100,100)    # Pinky
colorBlinky=pygame.Color(255,0,0)       # Blinky
colorInky=pygame.Color(10,255,255)      # Inky
colorClyde=pygame.Color(200,100,0)      # Clyde

sonidosalida = pygame.mixer.Sound("sonidos/pacman-dies.mp3")
sonidopunto =  pygame.mixer.Sound("sonidos/disparo.wav")

def dibujacomecoco(x,y,color):
    pygame.draw.circle(ventana,color,(x,y),20,width=0)

def dibujacoco(x,y,color):
    pygame.draw.circle(ventana,color,(x,y),20,width=0)
    rectpinky= pygame.Rect(x-20,y,40,20)
    pygame.draw.rect(ventana, color, rectpinky,width=0)
    pygame.display.flip()

def distancia(x0, y0, x1, y1):
    distancia = ((x1-x0)**2 + (y1-y0)**2)**0.5
    return distancia


for j in range (nfilas):
    for i in range (ncolumnas):
        #print(i,j)
        rectangulo = pygame.Rect(i*anchocelda,j*altocelda,anchocelda,altocelda)
        #pygame.draw.rect(ventana,coloreado5,rectangulo,width=1)

for i in range (nfilas):
    for j in range (ncolumnas):
        if i==0 or j==0 or i==nfilas-1 or j==ncolumnas-1:
            lista[i][j]=0
        elif i%2==0 and j%2==0:
            lista[i][j]=0    
        else:
            lista[i][j]=1


# for i in range (nfilas):
#     lista [i][2]=0
# for j in range (ncolumnas):
#     lista [2][j]=0


for i in range (nfilas):
    for j in range (ncolumnas):
        if lista[i][j]==0:
            rectangulo = pygame.Rect(j*anchocelda,i*altocelda,anchocelda,altocelda)
            pygame.draw.rect(ventana,coloreado4,rectangulo,width=1)
        else:
            pygame.draw.circle(ventana,coloreado2,(j*anchocelda+anchocelda/2,i*altocelda+altocelda/2),2,width=1)
print (lista)


for i in range (nfilas):
    for j in range (ncolumnas):
        listapuntos[i][j]=lista[i][j]

contador=0
salto=10
saltox=0
saltoy=0
saltoxPinky=0
saltoyPinky=0
saltoxBlinky=0
saltoyBlinky=0
saltoxInky=0
saltoyInky=0
saltoxClyde=0
saltoyClyde=0


PosComecoco=[5*anchocelda+anchocelda/2,5*altocelda+altocelda/2]
PosPinky=[11*anchocelda+anchocelda/2,11*altocelda+altocelda/2]
PosBlinky=[13*anchocelda+anchocelda/2,13*altocelda+altocelda/2]
PosInky=[15*anchocelda+anchocelda/2,15*altocelda+altocelda/2]
PosClyde=[17*anchocelda+anchocelda/2,15*altocelda+altocelda/2]

direc="stop"
direcBlinky="right"
direcPinky="left"
direcInky="left"
direcClyde="rigt"

marcador=0

retraso=0.03

running = True
while running:
    puntos=0
    for i in range (nfilas):
        for j in range (ncolumnas):
            if listapuntos[i][j]==1:
                pygame.draw.circle(ventana,coloreado2,(j*anchocelda+anchocelda/2,i*altocelda+altocelda/2),2,width=1)
                puntos = puntos + 1
            if listapuntos[i][j]==0:
                pygame.draw.circle(ventana,colorfondo,(j*anchocelda+anchocelda/2,i*altocelda+altocelda/2),2,width=1)
    pygame.display.flip()


    dibujacomecoco(PosComecoco[0],PosComecoco[1], colorComecoco)
    dibujacoco(PosPinky[0],PosPinky[1], colorPinky)
    dibujacoco(PosBlinky[0],PosBlinky[1], colorBlinky)
    dibujacoco(PosInky[0],PosInky[1], colorInky)
    dibujacoco(PosClyde[0],PosClyde[1], colorClyde)

    pygame.display.flip()

    time.sleep(retraso)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_q:
                pygame.mixer.Sound.play(sonidosalida)
                running = False
            if event.key == pygame.K_UP or event.key == pygame.K_k:
                direc="up"
            if event.key == pygame.K_DOWN or event.key == pygame.K_j:
                direc="down"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                direc="right"
            if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                direc="left"
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_u:
                direc="stop"

    saltoxant=saltox
    saltoyant=saltoy

    if (PosComecoco[0]-anchocelda/2)%anchocelda==0:
        icelda=int((PosComecoco[1]-altocelda/2)/altocelda)
        jcelda=int((PosComecoco[0]-anchocelda/2)/anchocelda)
        if direc=="up":
            if lista[icelda-1][jcelda]==1:
                saltoy=-salto
                saltox=0
            if (PosComecoco[1]-altocelda/2)%altocelda==0 and lista[icelda-1][jcelda]==0:
                saltoy=0
                saltox=0
        if direc=="down":
            if lista[icelda+1][jcelda]==1:
                saltoy=salto
                saltox=0
            if lista[icelda+1][jcelda]==0:
                saltoy=0
                saltox=0
        if direc=="stop":
            saltoy=0
            saltox=0

    if (PosComecoco[1]-altocelda/2)%altocelda==0:
        icelda=int((PosComecoco[1]-altocelda/2)/altocelda)
        jcelda=int((PosComecoco[0]-anchocelda/2)/anchocelda)
        if direc=="right":
            if lista[icelda][jcelda+1]==1:
                saltox=salto
                saltoy=0
            if lista[icelda][jcelda+1]==0:
                saltox=0
                saltoy=0
        if direc=="left":
            if lista[icelda][jcelda-1]==1:
                saltox=-salto
                saltoy=0
            if (PosComecoco[0]-anchocelda/2)%anchocelda==0 and lista[icelda][jcelda-1]==0:
                saltox=0
                saltoy=0
        if direc=="stop":
            saltoy=0
            saltox=0
    
        if (direc=="up" or direc=="down") and (lista[icelda-1][jcelda]==0 and lista[icelda+1][jcelda]==0):
            saltoy=saltoyant
            saltox=saltoxant

        if (direc=="left" or direc=="right") and (lista[icelda][jcelda-1]==0 and lista[icelda][jcelda+1]==0):
            saltoy=saltoyant
            saltox=saltoxant

        if listapuntos[icelda][jcelda]==1:
            listapuntos[icelda][jcelda]=0
            marcador=marcador+1
            pygame.mixer.Sound.play(sonidopunto)


#COCOS
#Blinky    
    saltoxantBlinky=saltoxBlinky
    saltoyantBlinky=saltoyBlinky

    if (PosBlinky[0]-anchocelda/2)%anchocelda==0:
        iceldaBlinky=int((PosBlinky[1]-altocelda/2)/altocelda)
        jceldaBlinky=int((PosBlinky[0]-anchocelda/2)/anchocelda)
        if direcBlinky=="up":
            if lista[iceldaBlinky-1][jceldaBlinky]==1:
                saltoyBlinky=-salto
                saltoxBlinky=0
            if (PosBlinky[1]-altocelda/2)%altocelda==0 and lista[iceldaBlinky-1][jceldaBlinky]==0:
                saltoyBlinky=0
                saltoxBlinky=0
        if direcBlinky=="down":
            if lista[iceldaBlinky+1][jceldaBlinky]==1:
                saltoyBlinky=salto
                saltoxBlinky=0
            if lista[iceldaBlinky+1][jceldaBlinky]==0:
                saltoyBlinky=0
                saltoxBlinky=0
        if direcBlinky=="stop":
            saltoyBlinky=0
            saltoxBlinky=0

    if (PosBlinky[1]-altocelda/2)%altocelda==0:
        iceldaBlinky=int((PosBlinky[1]-altocelda/2)/altocelda)
        jceldaBlinky=int((PosBlinky[0]-anchocelda/2)/anchocelda)
        if direcBlinky=="right":
            if lista[iceldaBlinky][jceldaBlinky+1]==1:
                saltoxBlinky=salto
                saltoyBlinky=0
            if lista[iceldaBlinky][jceldaBlinky+1]==0:
                saltoxBlinky=0
                saltoyBlinky=0
        if direcBlinky=="left":
            if lista[iceldaBlinky][jceldaBlinky-1]==1:
                saltoxBlinky=-salto
                saltoyBlinky=0
            if (PosBlinky[0]-anchocelda/2)%anchocelda==0 and lista[iceldaBlinky][jceldaBlinky-1]==0:
                saltoxBlinky=0
                saltoyBlinky=0

        if (direcBlinky=="up" or direcBlinky=="down") and (lista[iceldaBlinky-1][jceldaBlinky]==0 and lista[iceldaBlinky+1][jceldaBlinky]==0):
            saltoyBlinky=saltoyantBlinky
            saltoxBlinky=saltoxantBlinky

        if (direcBlinky=="left" or direcBlinky=="right") and (lista[iceldaBlinky][jceldaBlinky-1]==0 and lista[iceldaBlinky][jceldaBlinky+1]==0):
            saltoyBlinky=saltoyantBlinky
            saltoxBlinky=saltoxantBlinky

#Pinky    
    saltoxantPinky=saltoxPinky
    saltoyantPinky=saltoyPinky

    if (PosPinky[0]-anchocelda/2)%anchocelda==0:
        iceldaPinky=int((PosPinky[1]-altocelda/2)/altocelda)
        jceldaPinky=int((PosPinky[0]-anchocelda/2)/anchocelda)
        if direcPinky=="up":
            if lista[iceldaPinky-1][jceldaPinky]==1:
                saltoyPinky=-salto
                saltoxPinky=0
            if (PosPinky[1]-altocelda/2)%altocelda==0 and lista[iceldaPinky-1][jceldaPinky]==0:
                saltoyPinky=0
                saltoxPinky=0
        if direcPinky=="down":
            if lista[iceldaPinky+1][jceldaPinky]==1:
                saltoyPinky=salto
                saltoxPinky=0
            if lista[iceldaPinky+1][jceldaPinky]==0:
                saltoyPinky=0
                saltoxPinky=0
        if direcPinky=="stop":
            saltoyPinky=0
            saltoxPinky=0

    if (PosPinky[1]-altocelda/2)%altocelda==0:
        iceldaPinky=int((PosPinky[1]-altocelda/2)/altocelda)
        jceldaPinky=int((PosPinky[0]-anchocelda/2)/anchocelda)
        if direcPinky=="right":
            if lista[iceldaPinky][jceldaPinky+1]==1:
                saltoxPinky=salto
                saltoyPinky=0
            if lista[iceldaPinky][jceldaPinky+1]==0:
                saltoxPinky=0
                saltoyPinky=0
        if direcPinky=="left":
            if lista[iceldaPinky][jceldaPinky-1]==1:
                saltoxPinky=-salto
                saltoyPinky=0
            if (PosPinky[0]-anchocelda/2)%anchocelda==0 and lista[iceldaPinky][jceldaPinky-1]==0:
                saltoxPinky=0
                saltoyPinky=0

        if (direcPinky=="up" or direcPinky=="down") and (lista[iceldaPinky-1][jceldaPinky]==0 and lista[iceldaPinky+1][jceldaPinky]==0):
            saltoyPinky=saltoyantPinky
            saltoxPinky=saltoxantPinky

        if (direcPinky=="left" or direcPinky=="right") and (lista[iceldaPinky][jceldaPinky-1]==0 and lista[iceldaPinky][jceldaPinky+1]==0):
            saltoyPinky=saltoyantPinky
            saltoxPinky=saltoxantPinky

#Inky    
    saltoxantInky=saltoxInky
    saltoyantInky=saltoyInky

    if (PosInky[0]-anchocelda/2)%anchocelda==0:
        iceldaInky=int((PosInky[1]-altocelda/2)/altocelda)
        jceldaInky=int((PosInky[0]-anchocelda/2)/anchocelda)
        if direcInky=="up":
            if lista[iceldaInky-1][jceldaInky]==1:
                saltoyInky=-salto
                saltoxInky=0
            if (PosInky[1]-altocelda/2)%altocelda==0 and lista[iceldaInky-1][jceldaInky]==0:
                saltoyInky=0
                saltoxInky=0
        if direcInky=="down":
            if lista[iceldaInky+1][jceldaInky]==1:
                saltoyInky=salto
                saltoxInky=0
            if lista[iceldaInky+1][jceldaInky]==0:
                saltoyInky=0
                saltoxInky=0
        if direcInky=="stop":
            saltoyInky=0
            saltoxInky=0

    if (PosInky[1]-altocelda/2)%altocelda==0:
        iceldaInky=int((PosInky[1]-altocelda/2)/altocelda)
        jceldaInky=int((PosInky[0]-anchocelda/2)/anchocelda)
        if direcInky=="right":
            if lista[iceldaInky][jceldaInky+1]==1:
                saltoxInky=salto
                saltoyInky=0
            if lista[iceldaInky][jceldaInky+1]==0:
                saltoxInky=0
                saltoyInky=0
        if direcInky=="left":
            if lista[iceldaInky][jceldaInky-1]==1:
                saltoxInky=-salto
                saltoyInky=0
            if (PosInky[0]-anchocelda/2)%anchocelda==0 and lista[iceldaInky][jceldaInky-1]==0:
                saltoxInky=0
                saltoyInky=0

        if (direcInky=="up" or direcInky=="down") and (lista[iceldaInky-1][jceldaInky]==0 and lista[iceldaInky+1][jceldaInky]==0):
            saltoyInky=saltoyantInky
            saltoxInky=saltoxantInky

        if (direcInky=="left" or direcInky=="right") and (lista[iceldaInky][jceldaInky-1]==0 and lista[iceldaInky][jceldaInky+1]==0):
            saltoyInky=saltoyantInky
            saltoxInky=saltoxantInky


#Clyde    
    saltoxantClyde=saltoxClyde
    saltoyantClyde=saltoyClyde

    if (PosClyde[0]-anchocelda/2)%anchocelda==0:
        iceldaClyde=int((PosClyde[1]-altocelda/2)/altocelda)
        jceldaClyde=int((PosClyde[0]-anchocelda/2)/anchocelda)
        if direcClyde=="up":
            if lista[iceldaClyde-1][jceldaClyde]==1:
                saltoyClyde=-salto
                saltoxClyde=0
            if (PosClyde[1]-altocelda/2)%altocelda==0 and lista[iceldaClyde-1][jceldaClyde]==0:
                saltoyClyde=0
                saltoxClyde=0
        if direcClyde=="down":
            if lista[iceldaClyde+1][jceldaClyde]==1:
                saltoyClyde=salto
                saltoxClyde=0
            if lista[iceldaClyde+1][jceldaClyde]==0:
                saltoyClyde=0
                saltoxClyde=0
        if direcClyde=="stop":
            saltoyClyde=0
            saltoxClyde=0

    if (PosClyde[1]-altocelda/2)%altocelda==0:
        iceldaClyde=int((PosClyde[1]-altocelda/2)/altocelda)
        jceldaClyde=int((PosClyde[0]-anchocelda/2)/anchocelda)
        if direcClyde=="right":
            if lista[iceldaClyde][jceldaClyde+1]==1:
                saltoxClyde=salto
                saltoyClyde=0
            if lista[iceldaClyde][jceldaClyde+1]==0:
                saltoxClyde=0
                saltoyClyde=0
        if direcClyde=="left":
            if lista[iceldaClyde][jceldaClyde-1]==1:
                saltoxClyde=-salto
                saltoyClyde=0
            if (PosClyde[0]-anchocelda/2)%anchocelda==0 and lista[iceldaClyde][jceldaClyde-1]==0:
                saltoxClyde=0
                saltoyClyde=0

        if (direcClyde=="up" or direcClyde=="down") and (lista[iceldaClyde-1][jceldaClyde]==0 and lista[iceldaClyde+1][jceldaClyde]==0):
            saltoyClyde=saltoyantClyde
            saltoxClyde=saltoxantClyde

        if (direcClyde=="left" or direcClyde=="right") and (lista[iceldaClyde][jceldaClyde-1]==0 and lista[iceldaClyde][jceldaClyde+1]==0):
            saltoyClyde=saltoyantClyde
            saltoxClyde=saltoxantClyde





    if distancia(PosPinky[0],PosPinky[1],PosComecoco[0],PosComecoco[1])<20:
        pygame.mixer.Sound.play(sonidosalida)
        running = False
    if distancia(PosInky[0],PosInky[1],PosComecoco[0],PosComecoco[1])<20:
        pygame.mixer.Sound.play(sonidosalida)
        running = False
    if distancia(PosBlinky[0],PosBlinky[1],PosComecoco[0],PosComecoco[1])<20:
        pygame.mixer.Sound.play(sonidosalida)
        running = False
    if distancia(PosClyde[0],PosClyde[1],PosComecoco[0],PosComecoco[1])<20:
        pygame.mixer.Sound.play(sonidosalida)
        running = False
                

    # if listarandom[int(PosComecoco[0])][int(PosComecoco[1])] < 0.1 and not direcBlinky == "left":
    #     direcBlinky="right"
    # if listarandom[int(PosComecoco[0])][int(PosComecoco[1])] > 0.9 and not direcBlinky == "right":
    #     direcBlinky="left"
    # if listarandom[int(PosComecoco[0])][int(PosComecoco[1])] < 0.05 and not direcBlinky == "down":
    #     direcBlinky="up"
    # if listarandom[int(PosComecoco[0])][int(PosComecoco[1])] > 0.95 and not direcBlinky == "up":
    #     direcBlinky="down"

    x=random.random()
    if x < 0.25 and not direcBlinky == "left" and PosBlinky[0]<PosComecoco[0]:
        direcBlinky="right"
    if x > 0.75 and not direcBlinky == "right" and PosBlinky[0]>PosComecoco[0]:
        direcBlinky="left"
    if x < 0.25 and not direcBlinky == "down" and PosBlinky[1]>PosComecoco[1]:
        direcBlinky="up"
    if x > 0.75 and not direcBlinky == "up" and PosBlinky[1]<PosComecoco[1]:
        direcBlinky="down"

    y=random.random()
    if y < 0.1 and not direcPinky == "left" and PosPinky[0]<PosComecoco[0]:
        direcPinky="right"
    if y > 0.9 and not direcPinky == "right" and PosPinky[0]>PosComecoco[0]:
        direcPinky="left"
    if y < 0.05 and not direcPinky == "down" and PosPinky[1]>PosComecoco[1]:
        direcPinky="up"
    if y > 0.95 and not direcPinky == "up" and PosPinky[1]<PosComecoco[1]:
        direcPinky="down"

    z=random.random()
    if z < 0.1 and not direcInky == "left" and PosInky[0]<PosComecoco[0]:
        direcInky="right"
    if z > 0.9 and not direcInky == "right" and PosInky[0]>PosComecoco[0]:
        direcInky="left"
    if z < 0.05 and not direcInky == "down" and PosInky[1]>PosComecoco[1]:
        direcInky="up"
    if z > 0.95 and not direcInky == "up" and PosPinky[1]<PosComecoco[1]:
        direcInky="down"


    x=random.random()
    if x < 0.1 and not direcClyde == "left":
        direcClyde="right"
    if x > 0.9 and not direcClyde == "right":
        direcClyde="left"
    if x < 0.05 and not direcClyde == "down":
        direcClyde="up"
    if x > 0.95 and not direcClyde == "up":
        direcClyde="down"



    dibujacomecoco((PosComecoco[0]),(PosComecoco[1]), colorfondo)
    dibujacoco(PosPinky[0],PosPinky[1], colorfondo)
    dibujacoco(PosBlinky[0],PosBlinky[1], colorfondo)
    dibujacoco(PosInky[0],PosInky[1], colorfondo)
    dibujacoco(PosClyde[0],PosClyde[1], colorfondo)

    pygame.display.flip()


# CONTROL:
    fuente = pygame.font.SysFont('times new roman', 20)
    marcador1_surface = fuente.render('MARCADOR = '+ str(marcador) +'  ', True, coloreado2)
    marcador1_rect = marcador1_surface.get_rect()
    marcador1_rect.midtop = (tampantalla_x*0.9, tampantalla_y/20)
    pygame.draw.rect(ventana,colorfondo,marcador1_rect)
    ventana.blit(marcador1_surface, marcador1_rect)

    fuente = pygame.font.SysFont('times new roman', 20)
    marcador2_surface = fuente.render('  Faltan  = '+ str(puntos) +'  ', True, coloreado2)
    marcador2_rect = marcador2_surface.get_rect()
    marcador2_rect.midtop = (tampantalla_x*0.9, tampantalla_y/10)
    pygame.draw.rect(ventana,colorfondo,marcador2_rect)
    ventana.blit(marcador2_surface, marcador2_rect)

    PosComecoco[0]=PosComecoco[0] + saltox
    PosComecoco[1]=PosComecoco[1] + saltoy
    PosBlinky[0]=PosBlinky[0] + saltoxBlinky
    PosBlinky[1]=PosBlinky[1] + saltoyBlinky
    PosPinky[0]=PosPinky[0] + saltoxPinky
    PosPinky[1]=PosPinky[1] + saltoyPinky
    PosInky[0]=PosInky[0] + saltoxInky
    PosInky[1]=PosInky[1] + saltoyInky
    PosClyde[0]=PosClyde[0] + saltoxClyde
    PosClyde[1]=PosClyde[1] + saltoyClyde

    if puntos==0:
        
        fuente = pygame.font.SysFont('times new roman', 60)
        gameover_surface = fuente.render('NIVEL COMLETADO', True, coloreado2)
        gameover_rect = gameover_surface.get_rect()
        gameover_rect.midtop = (tampantalla_x/2, tampantalla_y/2)
        ventana.blit(gameover_surface, gameover_rect)
        pygame.display.flip()

        time.sleep(2)

        fuente = pygame.font.SysFont('times new roman', 60)
        gameover_surface = fuente.render('NIVEL COMLETADO', True, colorfondo)
        gameover_rect = gameover_surface.get_rect()
        gameover_rect.midtop = (tampantalla_x/2, tampantalla_y/2)
        ventana.blit(gameover_surface, gameover_rect)
        pygame.display.flip()

        retraso=retraso*0.75
        PosComecoco=[5*anchocelda+anchocelda/2,5*altocelda+altocelda/2]
        PosPinky=[11*anchocelda+anchocelda/2,11*altocelda+altocelda/2]
        PosBlinky=[13*anchocelda+anchocelda/2,13*altocelda+altocelda/2]
        PosInky=[15*anchocelda+anchocelda/2,15*altocelda+altocelda/2]
        PosClyde=[17*anchocelda+anchocelda/2,15*altocelda+altocelda/2]

        direc="stop"
        direcBlinky="right"
        direcPinky="left"
        direcInky="left"
        direcClyde="rigt"

        for i in range (nfilas):
            for j in range (ncolumnas):
                listapuntos[i][j]=lista[i][j]



        





time.sleep(2)
fuente = pygame.font.SysFont('times new roman', 60)
gameover_surface = fuente.render('GAME OVER', True, coloreado2)
gameover_rect = gameover_surface.get_rect()
gameover_rect.midtop = (tampantalla_x/2, tampantalla_y/2)
ventana.blit(gameover_surface, gameover_rect)
pygame.display.flip()
time.sleep(3)


