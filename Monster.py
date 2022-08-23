import pygame
import random
import animation

class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 300)
        self.rect.y = 450 - offset
        self.loot_amount = 10
        self.start_animation()

    #Définir la vitesse du monstre
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1,speed)

    #Définir le nombre de points
    def set_loot_amount(self, amount):
        self.loot_amount = amount

    #Mise à jour de l'animation
    def update_animation(self):
        self.animate(loop=True)

    #Mise à jour de la barre de vie du monstre
    def update_health_bar(self, surface):
        #définir une couleur pour la barre de vie
        bar_color = (111, 210, 46)
        #définir couleur arrière plan
        background_bar_color = (60, 63, 60)
        #définir la position, la largeur et l'épaisseur de la jauge
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        #définir la position, la largeur et l'épaisseur de l'arrière plan
        background_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        #déssiner la barre de vie et son arrière plan
        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, damage):
        self.health -= damage
        #vérifier si sa nouvelle vie est supérieure à 0
        if self.health <= 0 :
            #Ajouter le nombre de points
            self.game.add_score(self.game.multiplicateur * self.loot_amount)
            # si la barre d'évènement est chargé
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()
            else:
             #réapparition comme un nouveau monstre
                self.rect.x = 900 + random.randint(0, 300)
                self.health = self.max_health
                self.velocity = self.default_speed

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else : #infliger des dégats au joueur
            self.game.player.damage(self.attack)

#définir une classe pour la momie

class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (250, 250), 100)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)
