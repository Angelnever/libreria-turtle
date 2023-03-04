
from asyncio import events
from enemy import enemy
from fire import fire
import pygame

ANCHO = 800
LARGO = 600
#fps
FPS = 60
#colores
NEGRO =(0,0,0)
BLANCO =(255,255,255)
ROJO =(255,0,0)
H_FA2F22F =(250,47,47)
VERDE =(0,255,0)
AZUL =(0,0,255)
#fuentes

consolas = pygame.font.match_font("consolas")
Times = pygame.font.match_font("times")
arial = pygame.font.match_font("arial")
courier = pygame.font.match_font("courier")
#clase jugador
class player(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        self.image = pygame.image.load("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/nave-espacial.png")
        #seleccionamos el rectangulo sprite
        self.rect = self.image.get_rect()
        #centar rectangulo posiscion
        self.rect.center = (400,550)
        #velocidad inicial
        self.velocidad_x = 0
        self.velocidad_y = 0
    
    def update(self):
        #asignamos velocidad cada que se ejecuta el ciclo
        self.velocidad_x = 0
        self.velocidad_y = 0
        #cadencia
        self.cadencia = 300
        #obtenemos ultimo disparo
        self.ultimate = pygame.time.get_ticks()
        
        #variable para pulsar tecla
        teclas = pygame.key.get_pressed()
        
        #asignacion movimiento izq
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
                    
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
               
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        #tecla espacioa
        if teclas[pygame.K_SPACE]:
            tiempo = pygame.time.get_ticks()
            if tiempo + self.ultimate > self.cadencia:
              # self.disparos()    
                self.disparos()
                self.disparos2() 
                self.ultimate = tiempo
                laser.play()  
             
            
         #Actualizamos la posicion del personaje    
        self.rect.x += self.velocidad_x    
        self.rect.y += self.velocidad_y
        
    #limitantes borde
    #b izq y der
        if self.rect.left < 0:
            self.rect.left=0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            
    #BRODE UP Y DOWN
            
        if self.rect.bottom > LARGO:
            self.rect.bottom = LARGO
            
        if self.rect.top < 0:
            self.rect.top = 0
        
    def disparos(self):
        bala = fire(self.rect.centerx -20 , self.rect.centery)
        Balas.add(bala)
    def disparos2(self):
        bala = fire(self.rect.centerx +20 , self.rect.centery)
        Balas.add(bala)
         

class inicio():
    pygame.init()
     
#Sonidos ambiente
ambiente = pygame.mixer.Sound("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/daylight-14872.mp3")
#cambio volumen

#sonidop disparo
laser = pygame.mixer.Sound("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/shoot02wav-14562.mp3")
#sonidos puntos
puntos = pygame.mixer.Sound("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/collectcoin-6075.mp3")

pygame.mixer.music.set_volume(0.1)

ambiente.play()

#dibujamos la pantalla del jugador
  
pantalla = pygame.display.set_mode((ANCHO,LARGO))

#fondo videojuego

fondo = pygame.transform.scale(pygame.image.load("C:/Users/Angel/Desktop/PAGINAS WEB/turtle/videojuego/1.-videojuego/fond.jpg").convert(),(1000,600))
#inicio del videojuego
#titulo ventana
pygame.display.set_caption("Spaces")
# estableciendo FPS

clock = pygame.time.Clock()

Jugador = pygame.sprite.Group()
Balas = pygame.sprite.Group()
Enemigos = pygame.sprite.Group()
#add sprites 

jugadores = player()
Jugador.add(jugadores)

#sistema de puntuacion
puntuacion = 0
def texto(pantalla,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True,color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    pantalla.blit(superficie,rectangulo)
    

ejecutando = True

#ciclo de ejecutado videojuego

while ejecutando:
    clock.tick(FPS)
    pantalla.blit(fondo,(0,0))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            ejecutando = False
    
    #muestra puntuacion
    texto(pantalla,Times,str(puntuacion).zfill(6),BLANCO,50,700,50)
    #actualizacion de sprites        
    Jugador.update()
    Enemigos.update()
    Balas.update()
    
    #colisiones
    colision_nave = pygame.sprite.groupcollide(Enemigos,Jugador,False,False)
    Colision_bala = pygame.sprite.groupcollide(Enemigos,Balas,True,True)
    
    #condicion colision
    if colision_nave:
        puntuacion -= 10  
        
          
    if puntuacion < 0:
        puntuacion = 0
        break
    
    if Colision_bala:
        puntuacion += 30
        puntos.play()
  
    if puntuacion > 1000:
        jugadores.cadencia + 500
        
    #condicionar aparicion
    if not Enemigos:
        for x in range(10):
            enemigos = enemy()
            Enemigos.add(enemigos)
    #dibujando sprite en ventana
    Jugador.draw(pantalla)
    Enemigos.draw(pantalla)
    Balas.draw(pantalla)
    pygame.display.flip()