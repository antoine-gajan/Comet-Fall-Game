#Programme avec la classe Game
import pygame
from Player import Player
from Monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sound import SoundManager

class Game :
    def __init__(self):
        #définir si notre jeu a commencé
        self.is_playing = False
        # Instanciation du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #générer l'évènement
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        #mettre le score à 0
        self.multiplicateur = 1
        self.score = 0
        #générer les sons
        self.sound = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        "Remise du jeu à 0"
        self.all_monsters = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound.play("game_over")

    def add_score(self, point=10):
        self.score += point

    def update(self, screen):
        # Afficher le score sur l'écran
        police = pygame.font.Font("assets/Roboto-Light.ttf", 25)
        score_text = police.render(f"Score : {self.score}", False,(0,0,0))
        screen.blit(score_text, (20, 20))

        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Dessiner l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        #Actualiser l'animation du joueur
        self.player.update_animation()

        # Dessiner l'ensemble des images du groupe de monstres
        self.all_monsters.draw(screen)

        #Ensemble d'images des comètes
        self.comet_event.all_comets.draw(screen)

        # Actualiser la barre de vie du joueur
        self.player.update_heath_bar(screen)
        self.comet_event.update_bar(screen)

        # Vérifier si le joueur veut aller à gauche ou à droite
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.move_right()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monstre in self.all_monsters:
            monstre.move()
            monstre.update_animation()
            monstre.update_health_bar(screen)

        for comet in self.comet_event.all_comets:
            comet.fall(self.comet_event)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        monster = monster_class_name.__call__(self)
        self.all_monsters.add(monster)