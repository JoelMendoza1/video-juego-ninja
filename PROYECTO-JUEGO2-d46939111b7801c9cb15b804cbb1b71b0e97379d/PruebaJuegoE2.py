import pygame
import time
import sys
from pygame.locals import *


ancho = 720
alto = 350
girar = True
vez = True
moverFondo = True


class Ninja(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNinjaA = pygame.image.load('ninja1.gif')
        self.ImagenNinjaB = pygame.image.load('ninja2.gif')
        self.ImagenNinjaC = pygame.image.load('ninja3.gif')
        self.ImagenNinjaD = pygame.image.load('ninja4.gif')
        self.ImagenNinjaE = pygame.image.load('ninja5.gif')
        
        self.Fondo = pygame.image.load("Fondo2.gif")
        self.rectFondo = self.Fondo.get_rect()

        self.listaImagenes = [self.ImagenNinjaA, self.ImagenNinjaB, self.ImagenNinjaC,self.ImagenNinjaD,self.ImagenNinjaE]
        self.posImagen = 0

        self.ImagenNinja = self.listaImagenes [self.posImagen]
        self.rect = self.ImagenNinja.get_rect()
        
        self.rect.centerx = 20
        self.rect.centery = alto-60

        self.Vida = True

        self.velocidadNinja =3
        self.contadorpasos =1
        global enemigo

    def movimiento (self):
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left =0
                self.contadorpasos =1
            elif self.rect.right>720:
                self.contadorpasos =57
                self.rect.left =700

    def dibujar (self, superficie):
        self.ImagenNinja = self.listaImagenes [self.posImagen]
        superficie.blit(self.ImagenNinja, self.rect)

    def dibujarFondo (self, superficie):
        superficie.blit(self.Fondo, self.rectFondo)
        

    def dibujarFondoDerecha (self, superficie):
        self.contadorpasos +=1
        if self.contadorpasos >=130:
            self.velocidadNinja =3
      
        print(self.contadorpasos)
        if self.rect.centerx >=ancho/2 and self.contadorpasos <=130:
            superficie.blit(self.Fondo, self.rectFondo)
            self.rectFondo.left -=20
            enemigo.rect.left -=20
            enemigo.rect2.left -=20
            enemigo.rect3.left -=20
            enemigo.rect4.left -=20
            enemigo.rect5.left -=20
            enemigo.rect6.left -=20
            self.velocidadNinja =0
            
        else:
            superficie.blit(self.Fondo, self.rectFondo)
            

    def dibujarFondoIzquierda (self, superficie):
        self.contadorpasos -=1
            
        if self.contadorpasos <=108:
            self.velocidadNinja =3
            
        print(self.contadorpasos)
        if self.contadorpasos >=108 and self.contadorpasos <=130:
            superficie.blit(self.Fondo, self.rectFondo)
            self.rectFondo.left +=20
            enemigo.rect.left +=20
            enemigo.rect2.left +=20
            enemigo.rect3.left +=20
            enemigo.rect4.left +=20
            enemigo.rect5.left +=20
            enemigo.rect6.left +=20
            self.velocidadNinja =0
            
            
        else:
            superficie.blit(self.Fondo, self.rectFondo)
        

    def comportamiento(self, tiempo, tiempoCambio):
        if tiempoCambio ==tiempo:
            self.posImagen +=1
            tiempoCambio +=1

            if self.posImagen > len(self.listaImagenes) -1:
                self.posImagen =0

    def colisiones (self):
        if self.rect.colliderect(enemigo.rect) or self.rect.colliderect(enemigo.rect2) or self.rect.colliderect(enemigo.rect3)or self.rect.colliderect(enemigo.rect4)or self.rect.colliderect(enemigo.rect5)or self.rect.colliderect(enemigo.rect6):
            enemigo.velocidadEnemigo =0
            enJuego =False
                        
        else:
            enemigo.velocidadEnemigo =3

class Enemigo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.EnemigoA = pygame.image.load('estrella1.gif')
        self.EnemigoB = pygame.image.load('estrella2.gif')
        self.EnemigoC = pygame.image.load('estrella3.gif')

        self.listaImagenes = [self.EnemigoA, self.EnemigoB, self.EnemigoC]
        self.posImagen = 0

        self.ImagenEnemigo = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo2 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo3 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo4 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo5 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo6 = self.listaImagenes [self.posImagen]
        self.rect = self.ImagenEnemigo.get_rect()
        self.rect2 = self.ImagenEnemigo2.get_rect()
        self.rect3 = self.ImagenEnemigo3.get_rect()
        self.rect4 = self.ImagenEnemigo.get_rect()
        self.rect5 = self.ImagenEnemigo2.get_rect()
        self.rect6 = self.ImagenEnemigo3.get_rect()
        
        self.rect.centerx = 300
        self.rect.centery = alto-50
        self.rect2.centerx = 400
        self.rect2.centery = alto-100
        self.rect3.centerx = 500
        self.rect3.centery = alto-150
        self.rect4.centerx = 600
        self.rect4.centery = alto-50
        self.rect5.centerx = 700
        self.rect5.centery = alto-100
        self.rect6.centerx = 800
        self.rect6.centery = alto-150

        self.Vida = True

        self.velocidadEnemigo =5

        self.tiempoCambioEnemigo=14

        

    def movimientoE2 (self):

        global girar 

        if self.rect.y <=240 and girar == True:
            self.rect.y +=self.velocidadEnemigo
            self.rect2.y +=self.velocidadEnemigo
            self.rect3.y +=self.velocidadEnemigo
            self.rect4.y +=self.velocidadEnemigo
            self.rect5.y +=self.velocidadEnemigo
            self.rect6.y +=self.velocidadEnemigo
            
        else:
            girar = False
            
        if self.rect.y>=-10 and girar == False:
            self.rect.y -=self.velocidadEnemigo
            self.rect2.y -=self.velocidadEnemigo
            self.rect3.y -=self.velocidadEnemigo
            self.rect4.y -=self.velocidadEnemigo
            self.rect5.y -=self.velocidadEnemigo
            self.rect6.y -=self.velocidadEnemigo
        
        else:
            girar = True        
        
                    
            
        

        
            


    def dibujar (self, superficie):
        self.ImagenEnemigo = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo2 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo3 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo4 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo5 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo6 = self.listaImagenes [self.posImagen]
        superficie.blit(self.ImagenEnemigo, self.rect)
        superficie.blit(self.ImagenEnemigo2, self.rect2)
        superficie.blit(self.ImagenEnemigo3, self.rect3)
        superficie.blit(self.ImagenEnemigo4, self.rect4)
        superficie.blit(self.ImagenEnemigo5, self.rect5)
        superficie.blit(self.ImagenEnemigo6, self.rect6)

    def comportamientoEnemigo(self, tiempo):
        if self.tiempoCambioEnemigo ==tiempo:
            self.posImagen +=1
            self.tiempoCambioEnemigo +=1

            if self.posImagen > len(self.listaImagenes) -1:
                self.posImagen =0

enemigo = Enemigo()

def Gaiden():

    global enemigo
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Juego 1")
    mifuente= pygame.font.SysFont("Arial", 60)
    mifuenteReloj= pygame.font.SysFont("Arial Black", 30)
    miTexto = mifuente.render("GAME OVER",0,(200,0,0))
    TextoGanador = mifuente.render("YOU WIN",0,(200,0,0))

    jugador = Ninja()
    enJuego = True
    reloj = pygame.time.Clock()

    while True :

        reloj.tick(60)

        jugador.movimiento()
        jugador.colisiones()
        jugador.movimiento()
        enemigo.movimientoE2()
        jugador.dibujarFondo(ventana)  
        global moverFondo

        tiempo = int(pygame.time.get_ticks()/100)
        tiempoEnemigo = int(pygame.time.get_ticks()/100)
        Tiempo = int(pygame.time.get_ticks()/1000)



        if jugador.rect.right>720:
            jugador.velocidadNinja =0
            ventana.blit(TextoGanador,(250,100))
            
            
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()


        if evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:
                jugador.rect.left -= jugador.velocidadNinja
                tiempoCambio = tiempo
                jugador.comportamiento(tiempo, tiempoCambio)
                jugador.dibujarFondoIzquierda(ventana)
                        

            elif evento.key == K_RIGHT:
                jugador.rect.right += jugador.velocidadNinja
                tiempoCambio = tiempo
                jugador.comportamiento(tiempo, tiempoCambio)
                jugador.dibujarFondoDerecha(ventana)


            elif evento.key == K_UP:
                jugador.rect.y -= jugador.velocidadNinja

        Reloj = mifuenteReloj.render(str(Tiempo),0,(200,200,0))
        ventana.blit(Reloj,(340,10))                

                        
                                                              
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        enemigo.comportamientoEnemigo(tiempoEnemigo)
        
        

        pygame.display.update()

Gaiden()
        
        
    
    
