import pygame

class Score():
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def render_score(self, score):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(score, True, color=(255,255,255))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)