# Programme principal
import pygame
import math
from Game import Game

pygame.init()

#Définir les FPS
clock = pygame.time.Clock()
FPS = 60

#Générer la fenêtre du jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1200,650))

#Importer et charger l'image d'arrière plan
background = pygame.image.load("assets/bg.jpg")

#Importer la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (400, 400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2.85)

#Charger le bouton de début de partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (350, 125))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.6)
play_button_rect.y = math.ceil(screen.get_height() /2.2)

#Instanciation du jeu
game = Game()

#Boucle principale du jeu
running = True

while running:
    #Appliquer la fenêtre du jeu
    screen.blit(background, (0, -300))

    #Vérifier si le jeu a commencé
    if game.is_playing:
        #Déclencher les éléments du jeu
        game.update(screen)
    else :
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mise à jour de l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True  # La touche est active
            if event.key == pygame.K_SPACE:  # Détecte si un projectile est lancé
                if game.is_playing:
                    game.player.lance_projectile()
                else:
                    game.start()
                    game.sound.play("click")

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.is_playing and play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound.play("click")

    clock.tick(FPS)




