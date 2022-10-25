import pygame
import QuadTree
import random
import pygame

tree = QuadTree.Node(400.0, 300.0, 200.0)

for i in range(0, 20):
    x = random.randrange(201, 600)
    y = random.randrange(101, 500)
    tree.addPoint(QuadTree.Point(x, y))

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    screen.fill((0, 50, 255))
    tree.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tree.printInfo()
            running = False
