# Pygame - Jogo da cobrinha (Snake)
#
# O pygame serve para criar jogos. Todo jogo tem a mesma estrutura basica:
#   1. Preparar a tela e as variaveis
#   2. Repetir para sempre (o "game loop"):
#        - ler o que o jogador aperta
#        - atualizar as posicoes
#        - desenhar tudo de novo na tela

import pygame
import random

pygame.init()

# --- Configuracoes ---
LARGURA, ALTURA = 600, 400
TAMANHO = 20            # tamanho de cada "quadradinho" da cobra
VELOCIDADE = 10         # quadros por segundo (quanto maior, mais rapido)

PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
BRANCO = (255, 255, 255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cobrinha")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 36)


def posicao_comida_aleatoria():
    x = random.randrange(0, LARGURA, TAMANHO)
    y = random.randrange(0, ALTURA, TAMANHO)
    return [x, y]


def jogar():
    # A cobra e uma lista de posicoes [x, y]. O primeiro item e a cabeca.
    cobra = [[100, 100], [80, 100], [60, 100]]
    dx, dy = TAMANHO, 0           # direcao inicial: andando para a direita
    comida = posicao_comida_aleatoria()
    pontos = 0

    rodando = True
    while rodando:
        # 1. Eventos (teclado, fechar janela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -TAMANHO
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, TAMANHO
                elif evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -TAMANHO, 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = TAMANHO, 0

        # 2. Atualizar: calcula a nova cabeca e coloca no inicio da lista
        nova_cabeca = [cobra[0][0] + dx, cobra[0][1] + dy]
        cobra.insert(0, nova_cabeca)

        # Se comeu a comida, ganha ponto e nasce comida nova.
        # Se nao comeu, remove o ultimo pedaco (a cobra "anda").
        if nova_cabeca == comida:
            pontos += 1
            comida = posicao_comida_aleatoria()
        else:
            cobra.pop()

        # 3. Verificar se perdeu (bateu na parede ou em si mesma)
        bateu_parede = (
            nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA
            or nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA
        )
        if bateu_parede or nova_cabeca in cobra[1:]:
            rodando = False

        # 4. Desenhar
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, (comida[0], comida[1], TAMANHO, TAMANHO))
        for parte in cobra:
            pygame.draw.rect(tela, VERDE, (parte[0], parte[1], TAMANHO, TAMANHO))
        texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto, (10, 10))
        pygame.display.flip()

        relogio.tick(VELOCIDADE)

    # Tela de fim de jogo
    tela.fill(PRETO)
    msg = fonte.render(f"Fim de jogo! Pontos: {pontos}", True, BRANCO)
    tela.blit(msg, (LARGURA // 2 - 150, ALTURA // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


if __name__ == "__main__":
    jogar()
