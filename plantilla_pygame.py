# Plantilla básica para gráficos estáticos con Pygame
# Basada en la estructura de programarcadegames.com

import pygame

# --- Colores (R, G, B) ---
NEGRO   = (  0,   0,   0)
BLANCO  = (255, 255, 255)
ROJO    = (255,   0,   0)
VERDE   = (  0, 255,   0)
AZUL    = (  0,   0, 255)
AMARILLO= (255, 255,   0)
NARANJA = (255, 165,   0)

# --- Inicialización de Pygame ---
pygame.init()

# --- Tamaño de la ventana ---
ANCHO = 700
ALTO  = 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# --- Título de la ventana ---
pygame.display.set_caption("Mis gráficos")

# --- Bucle principal ---
hecho = False
reloj = pygame.time.Clock()

while not hecho:

    # 1) Gestión de eventos (no modificar)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # 2) Fondo de la pantalla
    pantalla.fill(BLANCO)

    # -------------------------------------------------------
    # 3) DIBUJA AQUÍ TUS FIGURAS
    # -------------------------------------------------------
# Rectángulo: pygame.draw.rect(pantalla, color, [x, y, ancho, alto], grosor)
    #   grosor=0 → relleno; grosor>0 → solo borde
    pygame.draw.rect(pantalla, AZUL, [200, 150, 250, 150], 0)
    pygame.draw.rect(pantalla, NEGRO, [215, 150, 250, 200], 2)

    
      # Elipse / círculo: pygame.draw.ellipse(pantalla, color, [x, y, ancho, alto], grosor)
    pygame.draw.ellipse(pantalla, ROJO, [355, 170, 50, 50], 0)


    # Rectángulo: pygame.draw.rect(pantalla, color, [x, y, ancho, alto], grosor)
    #   grosor=0 → relleno; grosor>0 → solo borde
    pygame.draw.rect(pantalla, NARANJA, [200, 50, 50, 100], 0)
    
     # Rectángulo: pygame.draw.rect(pantalla, color, [x, y, ancho, alto], grosor)
    
    pygame.draw.rect(pantalla, AMARILLO, [275, 200, 60, 100], 0)
    pygame.draw.rect(pantalla, NEGRO, [215, 150, 250, 150], 2)



   # Polígono: pygame.draw.polygon(pantalla, color, [[x1,y1],[x2,y2],...], grosor)
    pygame.draw.polygon(pantalla, VERDE, [[200, 150], [350, 25], [500, 150]], 0)


    # Texto en pantalla
    fuente = pygame.font.SysFont("Arial", 24)
    texto  = fuente.render("¡Llegastes,felicidades!", True, AZUL)
    pantalla.blit(texto, [50, 350])

    
    # -------------------------------------------------------
    # 4) Actualizar pantalla (no modificar)
    # -------------------------------------------------------
    pygame.display.flip()
    reloj.tick(60)

# --- Salir de Pygame ---
pygame.quit()

