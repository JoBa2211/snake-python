# Importamos pygame, la biblioteca que usaremos para gráficos
import pygame

# Inicializamos pygame (siempre hay que hacer esto primero)
pygame.init()

# Definimos colores
NEGRO = (0, 0, 0)     # Fondo negro
Blanco = (255, 255, 255) #color blanco para el cuadro

# Tamaño de la ventana
ANCHO = 800
ALTO = 800
#tamaño del cuadro
tamaño_cuadro = 50

#posicion del cuadro
posicionx=(ANCHO-tamaño_cuadro)//2
posiciony=(ALTO-tamaño_cuadro)//2

#velocidad del cuadro
velocidadx=2

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Snake Python')

# Creamos un reloj para controlar los FPS
reloj = pygame.time.Clock()

# Variable para controlar el bucle principal
ejecutando = True

#ultima posicion precionada
direccion=""

#lista de las posiciones dadas
lista_posiciones=[]
posicionnueva=(0,0)

#contado cremicimiento cola
contadorcola=0
contadordenumerodecolas=0

# Bucle principal
while ejecutando:
    # Procesamos los eventos
    for evento in pygame.event.get():
        # Si el usuario cierra la ventana, terminamos el programa
        if evento.type == pygame.QUIT:
            ejecutando = False
     # Capturamos las teclas presionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        direccion="izquierda"

    if teclas[pygame.K_RIGHT]:
        direccion="derecha"
    if teclas[pygame.K_UP]:
        direccion="arriba"
    if teclas[pygame.K_DOWN]:
        direccion="abajo"

    #si la direccion se preciona se guarda la ultima
    #direccion presionada
    if direccion=="arriba":
        posiciony=posiciony-velocidadx
        
    elif direccion=="abajo":
        posiciony=posiciony+velocidadx
       
    elif direccion=="izquierda":
        posicionx=posicionx-velocidadx

    elif direccion=="derecha":
        posicionx=posicionx+velocidadx
        
    # Guardamos la posición
    posicionnueva=(posicionx,posiciony)
    lista_posiciones.append(posicionnueva)
    
    # Mantener solo las últimas 1000 posiciones para evitar problemas de memoria
    if len(lista_posiciones) > 1000:
        lista_posiciones = lista_posiciones[-1000:]
    
    contadorcola+=1

    # Llenamos la ventana con color negro
    ventana.fill(NEGRO)

    pygame.draw.rect(
        ventana,  # Superficie donde dibujar
        Blanco,  # Color del cuadrado
        [posicionx, posiciony, tamaño_cuadro, tamaño_cuadro]  # Posición y tamaño
    )
    
    # Cada 600 pasos agregamos un nuevo segmento a la cola
    if contadorcola >= 600:
        print(contadorcola)
        print("cola nueva")
        contadordenumerodecolas+=1
        contadorcola=0
    
    # Dibujamos todos los segmentos de la cola
    for i in range(contadordenumerodecolas):
        distancia = (i + 1) * 10  # Distancia entre segmentos
        if len(lista_posiciones) > distancia:
            cordenadas = lista_posiciones[-distancia]
            posicioncolax, posicioncolay = cordenadas
            pygame.draw.rect(
                ventana,
                Blanco,
                [posicioncolax, posicioncolay, tamaño_cuadro, tamaño_cuadro]
            )
        
    # Actualizamos la pantalla
    pygame.display.update()
    
    # Limitamos a 60 FPS
    reloj.tick(60)

    if posicionx<0 or posicionx>ANCHO:
        pygame.quit()
    if posiciony<0 or posiciony>ALTO:
        pygame.quit()

# Cerramos pygame
pygame.quit()