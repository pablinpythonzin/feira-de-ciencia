# Pygame - Pong (o jogo de tenis mais antigo dos videogames)
#
# Dois jogadores controlam raquetes e rebatem uma bola.
#   Jogador da esquerda: teclas W (sobe) e S (desce)
#   Jogador da direita:  setas para cima e para baixo
#
# A estrutura e a mesma de qualquer jogo: eventos -> atualizar -> desenhar.

import pygame

pygame.init()

LARGURA, ALTURA = 700, 500
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 50)

# Raquetes: usamos pygame.Rect (x, y, largura, altura) para guardar posicao e tamanho.
raquete_esq = pygame.Rect(30, ALTURA // 2 - 50, 15, 100)
raquete_dir = pygame.Rect(LARGURA - 45, ALTURA // 2 - 50, 15, 100)

bola = pygame.Rect(LARGURA // 2 - 10, ALTURA // 2 - 10, 20, 20)
bola_vx, bola_vy = 5, 5          # velocidade da bola em x e y

VELOCIDADE_RAQUETE = 6
pontos_esq = 0
pontos_dir = 0


def reiniciar_bola():
    """Coloca a bola no centro e inverte o lado para onde ela vai."""
    global bola_vx
    bola.center = (LARGURA // 2, ALTURA // 2)
    bola_vx = -bola_vx


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # teclas seguradas (movimento continuo enquanto a tecla esta pressionada)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_esq.top > 0:
        raquete_esq.y -= VELOCIDADE_RAQUETE
    if teclas[pygame.K_s] and raquete_esq.bottom < ALTURA:
        raquete_esq.y += VELOCIDADE_RAQUETE
    if teclas[pygame.K_UP] and raquete_dir.top > 0:
        raquete_dir.y -= VELOCIDADE_RAQUETE
    if teclas[pygame.K_DOWN] and raquete_dir.bottom < ALTURA:
        raquete_dir.y += VELOCIDADE_RAQUETE

    # mover a bola
    bola.x += bola_vx
    bola.y += bola_vy

    # bateu no teto ou no chao -> inverte o movimento vertical
    if bola.top <= 0 or bola.bottom >= ALTURA:
        bola_vy = -bola_vy

    # bateu numa raquete -> inverte o movimento horizontal
    if bola.colliderect(raquete_esq) or bola.colliderect(raquete_dir):
        bola_vx = -bola_vx

    # passou da borda -> ponto para o outro jogador
    if bola.left <= 0:
        pontos_dir += 1
        reiniciar_bola()
    if bola.right >= LARGURA:
        pontos_esq += 1
        reiniciar_bola()

    # desenhar tudo
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, raquete_esq)
    pygame.draw.rect(tela, BRANCO, raquete_dir)
    pygame.draw.ellipse(tela, BRANCO, bola)
    pygame.draw.aaline(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))
    placar = fonte.render(f"{pontos_esq}   {pontos_dir}", True, BRANCO)
    tela.blit(placar, (LARGURA // 2 - 50, 20))
    pygame.display.flip()

    relogio.tick(60)   # 60 quadros por segundo

pygame.quit()
