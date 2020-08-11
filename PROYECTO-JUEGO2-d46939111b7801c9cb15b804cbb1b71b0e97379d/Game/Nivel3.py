import pygame
import sys
from pygame.locals import *

ancho = 720
alto = 500
a1=600
a2=300
girar = True
vez = True
moverFondo = True
puntaje=0


class Ninja(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNinjaA = pygame.image.load('ninja1.png')
        self.ImagenNinjaB = pygame.image.load('ninja2.png')
        self.ImagenNinjaC = pygame.image.load('ninja3.png')
        self.ImagenNinjaD = pygame.image.load('ninja4.png')
        self.ImagenNinjaE = pygame.image.load('ninja5.png')
        
        self.Fondo = pygame.image.load("Fondo3.gif")
        self.rectFondo = self.Fondo.get_rect()

        self.listaImagenes = [self.ImagenNinjaA, self.ImagenNinjaB, self.ImagenNinjaC,self.ImagenNinjaD,self.ImagenNinjaE]
        self.posImagen = 0

        self.ImagenNinja = self.listaImagenes [self.posImagen]
        self.rect = self.ImagenNinja.get_rect()
        
        self.rect.centerx = 20
        self.rect.centery = alto-60

        self.Vida = True

        self.velocidadNinja =20
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
        global a1,a2
        self.contadorpasos +=1
        global puntaje;
        
        if self.contadorpasos ==21:
            puntaje +=10
            
        if self.contadorpasos ==36:
            puntaje +=10
            
        if self.contadorpasos ==52:
            puntaje +=10
            
        if self.contadorpasos >=40:
            self.velocidadNinja =20
      
        print(self.contadorpasos)
        if self.rect.centerx >=ancho/2 and self.contadorpasos <=40:
            superficie.blit(self.Fondo, self.rectFondo)
            self.rectFondo.left -=20
            enemigo.rect.left -=20
            enemigo.rect2.left -=20
            enemigo.rect3.left -=20
            a1-=20
            a2-=20
            self.velocidadNinja =0
            
        else:
            superficie.blit(self.Fondo, self.rectFondo)
            

    def dibujarFondoIzquierda (self, superficie):
        global a1,a2
        self.contadorpasos -=1
            
        if self.contadorpasos <=18:
            self.velocidadNinja =20
            
        print(self.contadorpasos)
        if self.contadorpasos >=18 and self.contadorpasos <=40:
            superficie.blit(self.Fondo, self.rectFondo)
            self.rectFondo.left +=20
            enemigo.rect.left +=20
            enemigo.rect2.left +=20
            enemigo.rect3.left +=20
            a1+=20
            a2+=20
            self.velocidadNinja =0
            
            
        else:
            superficie.blit(self.Fondo, self.rectFondo)
        

    def comportamiento(self, tiempo, tiempoCambio):
        if tiempoCambio ==tiempo:
            self.posImagen +=1
            tiempoCambio +=1

            if self.posImagen > len(self.listaImagenes) -1:
                self.posImagen =0

class Enemigo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.EnemigoA = pygame.image.load('estrella1.png')
        self.EnemigoB = pygame.image.load('estrella2.png')
        self.EnemigoC = pygame.image.load('estrella3.png')

        self.listaImagenes = [self.EnemigoA, self.EnemigoB, self.EnemigoC]
        self.posImagen = 0

        self.ImagenEnemigo = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo2 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo3 = self.listaImagenes [self.posImagen]
        self.rect = self.ImagenEnemigo.get_rect()
        self.rect2 = self.ImagenEnemigo2.get_rect()
        self.rect3 = self.ImagenEnemigo3.get_rect()
        
        self.rect.centerx = 300
        self.rect.centery = alto-60
        self.rect2.centerx = 600
        self.rect2.centery = alto-60
        self.rect3.centerx = 900
        self.rect3.centery = alto-60

        self.Vida = True

        self.velocidadEnemigo =5

        self.tiempoCambioEnemigo=14

        
    def movimiento (self):
        self.sonidoEnemigo = pygame.mixer.Sound("Estrellas.wav")
        self.sonidoEnemigo.play()

        global girar
        global a1,a2

        if self.rect.x >=a2 and girar == True:
            self.rect.y +=self.velocidadEnemigo
            self.rect.x -=self.velocidadEnemigo
            self.rect2.y +=self.velocidadEnemigo
            self.rect2.x -=self.velocidadEnemigo
            self.rect3.y +=self.velocidadEnemigo
            self.rect3.x -=self.velocidadEnemigo

            
        else:
            girar = False
            
        if self.rect.x<=a1 and girar == False:
            self.rect.y -=self.velocidadEnemigo
            self.rect.x +=self.velocidadEnemigo
            self.rect2.y -=self.velocidadEnemigo
            self.rect2.x +=self.velocidadEnemigo
            self.rect3.y -=self.velocidadEnemigo
            self.rect3.x +=self.velocidadEnemigo
        
        else:
            girar = True


    def dibujar (self, superficie):
        self.ImagenEnemigo = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo2 = self.listaImagenes [self.posImagen]
        self.ImagenEnemigo3 = self.listaImagenes [self.posImagen]
        superficie.blit(self.ImagenEnemigo, self.rect)
        superficie.blit(self.ImagenEnemigo2, self.rect2)
        superficie.blit(self.ImagenEnemigo3, self.rect3)

    def comportamientoEnemigo(self, tiempo):
        if self.tiempoCambioEnemigo ==tiempo:
            self.posImagen +=1
            self.tiempoCambioEnemigo +=1

            if self.posImagen > len(self.listaImagenes) -1:
                self.posImagen =0

enemigo = Enemigo()

def Gaiden():

    global enemigo
    enJuego =True
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Juego 1")
    mifuente= pygame.font.SysFont("Arial", 60)
    mifuenteReloj= pygame.font.SysFont("Arial Black", 20)
    miTexto = mifuente.render("GAME OVER",0,(200,0,0))
    TextoGanador = mifuente.render("YOU WIN",0,(200,0,0))
    pygame.mixer.music.load("Music.mp3")
    pygame.mixer.music.play(5)

    jugador = Ninja()
    enJuego = True
    reloj = pygame.time.Clock()

    while enJuego==True :

        reloj.tick(60)

        jugador.movimiento()
        enemigo.movimiento()
        jugador.dibujarFondo(ventana)  
        global moverFondo
        global puntaje

        tiempo = int(pygame.time.get_ticks()/100)
        tiempoEnemigo = int(pygame.time.get_ticks()/100)
        Tiempo = int(pygame.time.get_ticks()/1000)

        if jugador.rect.colliderect(enemigo.rect) or jugador.rect.colliderect(enemigo.rect2) or jugador.rect.colliderect(enemigo.rect3):
            enemigo.velocidadEnemigo =0
            ventana.blit(miTexto,(200,100))
            jugador.Vida = False
            enJuego =False
            

            
        else:
            enemigo.velocidadEnemigo =5

        if jugador.rect.right>720:
            jugador.velocidadNinja =0
            ventana.blit(TextoGanador,(250,100))
            
            
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if enJuego == True:
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

        Relojtxt = mifuenteReloj.render("TIME: ",0,(0,100,200))
        ventana.blit(Relojtxt,(270,10))
        Reloj = mifuenteReloj.render(str(Tiempo),0,(0,100,200))
        ventana.blit(Reloj,(340,10))
        
        Puntajetxt = mifuenteReloj.render("SCORE: ",0,(0,100,200))
        ventana.blit(Puntajetxt,(560,10))
        TextoPuntaje = mifuenteReloj.render(str(puntaje),0,(0,100,200))
        ventana.blit(TextoPuntaje ,(650,10))

                        
                                                              
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        enemigo.comportamientoEnemigo(tiempoEnemigo)
        
        

        pygame.display.update()

Gaiden()
        
        
    
    
