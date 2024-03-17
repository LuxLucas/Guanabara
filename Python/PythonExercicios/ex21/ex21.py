import pygame

#   Inicia a música
pygame.init()
pygame.mixer.music.load('Woodkid - Run Boy Run.mp3')
pygame.mixer.music.play()

#   Executa o programa até a música acabar
while True:
    if not pygame.mixer.music.get_busy():
        break

print('FIM')
