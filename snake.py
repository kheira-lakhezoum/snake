import pygame
import random
import sys

pygame.init()

# Titre
pygame.display.set_caption('Snake')

# Dimension de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))

# Temps
fps = pygame.time.Clock()
vitesse = 15

# Couleurs
rouge = (255, 0, 0)
noir = (0, 0, 0)
green = (58, 157, 35)

# Surface
bricks_x = 32
bricks_y = 24

brick_l = largeur // bricks_x
brick_h = hauteur // bricks_y

# Snake
snake = [
    [bricks_x // 4, bricks_y // 2],
    [bricks_x // 4 - 1, bricks_y // 2],
    [bricks_x // 4 - 2, bricks_y // 2]
]
direction = [1, 0]

# Apple
apple = [bricks_x // 2, bricks_y // 2]

# Score initial
score = 0

def draw_snake():
    snake_color = pygame.Color(0, 0, 0)
    for cell in snake:
        cell_snake = pygame.Rect((cell[0] * brick_h, cell[1] * brick_l), (brick_h, brick_l))
        pygame.draw.rect(ecran, snake_color, cell_snake)

def draw_apple():
    apple_color = pygame.Color(255, 0, 0)
    apple_bricks = pygame.Rect((apple[0] * brick_l, apple[1] * brick_h), (brick_l, brick_h))
    pygame.draw.rect(ecran, apple_color, apple_bricks)

def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, noir)
    ecran.blit(text, (10, 10))

def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, noir)
    ecran.blit(text, (largeur // 3, hauteur // 3))
    draw_score()  # Afficher le score à l'écran lors du Game Over
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]

    # Mettre à jour la position du serpent
    nouvelle_tete = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

    # Vérifier les conditions de fin de jeu
    if (
        nouvelle_tete in snake[1:]  # Si la nouvelle tête est dans le corps du serpent
        or nouvelle_tete[0] < 0 or nouvelle_tete[0] >= bricks_x  # Si la tête touche les bords horizontaux
        or nouvelle_tete[1] < 0 or nouvelle_tete[1] >= bricks_y  # Si la tête touche les bords verticaux
    ):
        game_over()  # Appeler la fonction game_over si les conditions de fin de jeu sont remplies

    # Mettre à jour la position de la pomme si le serpent l'a mangée
    if nouvelle_tete == apple:
        # Ajouter un segment au serpent
        snake.append(snake[-1])
        apple = [random.randint(0, bricks_x - 1), random.randint(0, bricks_y - 1)]
        # Augmenter le score
        score += 1

    # Supprimer la queue du serpent
    snake.pop()

    # Insérer la nouvelle tête du serpent
    snake.insert(0, nouvelle_tete)

    # Dessiner le serpent, la pomme et le score
    ecran.fill(green)
    draw_snake()
    draw_apple()
    draw_score()
    pygame.display.update()

    # Contrôler la fréquence d'images par seconde
    fps.tick(vitesse)

pygame.quit()
