import pygame

#classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load("assets/" + sprite_name + ".png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #Démarrer l'animation
    def start_animation(self):
        self.animation = True
        self.animate()

    #définir une méthode pour animer le sprite
    def animate(self, loop=False):
        if self.animation:
            #passer à l'image suivante
            self.current_image += 1
            #vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images) :
                self.current_image = 0
                if loop == False :
                    #désactiver l'animation
                    self.animation = False
            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#fonction pour charger l'animation de la classe
def load_animation_images(sprite_name):
    images = []
    #Récupérer le chemin du dossier pour le sprite
    path = "assets/" + sprite_name + "/" + sprite_name
    #Pour chaque image dans le dossier
    for num in range(1, 25):
        image_path = pygame.image.load(path + str(num) + ".png")
        images.append(image_path)
    #Renvoie le contenu de la liste d'images
    return images

#Dictionnaire qui va contenir les images chargées de chaque sprite

animations = {
    "mummy" : load_animation_images("mummy"),
    "player" : load_animation_images('player'),
    "alien" : load_animation_images("alien")
}

