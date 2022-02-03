import pygame


class MyDrop():
    def __init__(self, pos, speed_increase):
        self.radius = 0
        self.pos = pos
        self.speed_increase = speed_increase

    def increase(self):
        self.radius += self.speed_increase
        if self.radius > 100:
            return False
        self.draw()
        return True

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), self.pos, int(self.radius))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    width, height = 700, 700
    size = width, height
    screen = pygame.display.set_mode(size)

    v = 100
    fps = 60
    clock = pygame.time.Clock()

    list_drop = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                list_drop.append(MyDrop(event.pos, v / fps))
        screen.fill((0, 0, 255))
        list_drop = [i for i in list_drop if i.increase()]

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()