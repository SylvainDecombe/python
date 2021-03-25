from game_object import GameObject
from objects.paddle import Paddle
from pygame.surface import Surface
from objects.ball import Ball
from pygame import font
from objects.score import Score
import time
import pygame

# Une classe qui va gérer la logique du jeu


class Game(GameObject):
    # On crée nos objets
    ball = Ball()
    player_paddle = Paddle(ball, True)
    enemy_paddle = Paddle(ball, False)
    score = Score()
    score_player = 0
    score_ia = 0

    # Indique si la boucle de jeu doit tourner ou non
    should_run = True

    # Lance les init de chaque objet au démarrage du jeu
    def init(self, screen: Surface):
        self.ball.init(screen)
        self.player_paddle.init(screen)
        self.enemy_paddle.init(screen)        
        self.score.init(screen)

    # Lance les update de chaque objet à chaque frame et gère la
    # relation entre les objets
    def update(self):
        self.ball.update()
        self.player_paddle.update()
        self.enemy_paddle.update()
        self.score.update(self.score_player,self.score_ia)

        # gestion de la collision entre ball et les paddles
        if self.ball.pos[0] == 0 and not self.player_paddle.as_rect().colliderect(self.ball.as_rect()):
            self.score_ia += 1
        if self.ball.pos[0] == 800 and not self.enemy_paddle.as_rect().colliderect(self.ball.as_rect()):
            self.score_player += 1

    def end_game(self):
        if self.score_ia == 5 or self.score_player == 5 :
            return True

        
