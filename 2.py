import pygame

size = input().split()
size, cnt = size
size_cletka = int(size) / int(cnt)


def draw(screen):
    pygame.Surface.fill(screen, (0, 0, 0), (0, 0, int(size), int(size)))
    for i in range(0, int(cnt), 2):
        pygame.Surface.fill(screen, (255, 255, 255), (0, i * int(size_cletka), int(size_cletka), int(size_cletka)))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((int(size), int(size)))
    pygame.display.set_caption('Шахматная клетка')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()


