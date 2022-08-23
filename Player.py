#Programme avec la classe Player
import pygame.sprite
from Projectile import Projectile
import animation

class Player (animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.game = game

    def update_animation(self):
        self.animate()

    def update_heath_bar(self, surface):
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def damage(self, damage):
        if self.health - damage > 0:
            self.health -= damage
        else :
            self.game.game_over()

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x+= self.velocity

    def lance_projectile(self):
        self.all_projectiles.add(Projectile(self))
        #lancer l'animation
        self.start_animation()
        self.game.sound.play("tir")
