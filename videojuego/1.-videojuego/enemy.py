import random
import pygame

ANCHO = 800
LARGO = 600

NEGRO =(0,0,0)
BLANCO =(255,255,255)
ROJO =(255,0,0)
H_FA2F22F =(250,47,47)
VERDE =(0,255,0)
AZUL =(0,0,255)

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        #herredar la variable de la clase sprite
        super().__init__()
        
        #cargar enemigo
        self.image = pygame.image.load("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/enemigo.png")
        #obtener el rectangulo del sprite
        self.rect = self.image.get_rect()
        #posicion map
        self.rect.center = (200,500)
        
        #aleatoria
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)
        
        #movimiento personaje
        self.velocidad_x = random.randrange(1,10)
        self.velocidad_y = random.randrange(1,10)
        
        
    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #limite rango izq
        
        if self.rect.left < 0 :
            self.velocidad_x += 1
        #limite rango der    
        if self.rect.right > ANCHO :
            self.velocidad_x -= 1
        #limite inferior
        if self.rect.bottom > LARGO:
            self.velocidad_y -=1
        #limite superior
        if self.rect.top < 0:
            self.velocidad_y += 1
        
