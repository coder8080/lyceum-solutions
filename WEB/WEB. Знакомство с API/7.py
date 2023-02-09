import os
import sys
import pygame
import requests

image_url = 'https://downloader.disk.yandex.ru/preview/6593b4cc9cc5cd79e9b666836b754af9d5f772d927af627326e186c57ada0838/63d2accf/2CSengZHSqTQmjmnyj59q0_njftZcX2zK--FoBP_pKZ4GMh6o85fxRiSuLdi2CnZb61WlLsONre6WhPnUf05Jw%3D%3D?uid=0&filename=map.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048'
response = requests.get(image_url)
if not response:
    print('Ошибка')
    sys.exit(1)
image_filename = 'image.jpg'
image_file = open(image_filename, 'wb')
image_file.write(response.content)
image_file.close()
del image_file

pygame.init()
screen = pygame.display.set_mode((650, 347))
screen.blit(pygame.image.load(image_filename), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(image_filename)
