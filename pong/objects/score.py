from game_object import GameObject
from pygame import Rect, Surface, Vector2, draw
import pygame

# Définition de la classe Ball
class Score(GameObject):

    # Constructeur de la classe
    def __init__(self, pos=Vector2(0, 0)):
        # La position de la balle (Vecteur)
        self.pos = pos
        # Taille de l'affichage
        self.size = Vector2(300, 100)
    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen
        self.pos = Vector2(screen.get_width()/2 - self.size[0]/2, 50)
        
    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self,sj,si):
        
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(sj), 1, (255,255,255))
        self.screen.blit(text, (300,10))
        text = font.render(str(si), 1, (255,255,255))
        self.screen.blit(text, (470,10))

    # Renvoi un rectangle aux même dimensions et position que le texte
    def as_rect(self):
        return Rect(self.pos, self.size)
