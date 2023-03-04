import pygame

#dimensiones d ela ventana 
ANCHO = 800
LARGO = 600
#colores a utilizar
NEGRO =(0,0,0)
BLANCO =(255,255,255)
ROJO =(255,0,0)
H_FA2F22F =(250,47,47)
VERDE =(0,255,0)
AZUL =(0,0,255)

class fire(pygame.sprite.Sprite):
    def __init__(self, x,y):
    
        super().__init__()
        self.image = pygame.image.load("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/disparo.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        
    def update(self):
        self.rect.y -= 10
        
        if self.rect.bottom < 0:
            self.kill 