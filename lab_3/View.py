import pygame
from RedBlackTree import *
from Car import Car
from random import randint


class View:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        pygame.init()
        pygame.font.init()
        self.size = self.width, self.height = 1000, 500
        self.screen = pygame.display.set_mode(self.size)
        self.running = True
        pygame.display.set_caption("Kaelesty's RedBlackTree View")

        self.BLACK_RGB = (0, 0, 0)
        self.RED_RBG = (255, 80, 80)
        self.WHITE_RBG = (255, 255, 255)
        self.font = pygame.font.SysFont('Comic Sans MS', 12)

    def drawTree(self, treeRoot):
        x, y = self.width // 2, 30
        self.drawNode(treeRoot.root, x, y, x, y, None, 6, True)

    def drawNode(self, node, x, y, parentX, parentY, isLeft, nesting, isFirst=False):
        pygame.draw.line(
            self.screen,
            self.BLACK_RGB,
            (x, y), (parentX, parentY), 1
        )
        if isinstance(node, rbtLeaf):
            pygame.draw.rect(
                self.screen,
                self.BLACK_RGB,
                pygame.Rect(x - 10, y - 10, 20, 20)
            )
            text = self.font.render("L", True, self.WHITE_RBG)
        else:
            pygame.draw.circle(
                self.screen,
                self.BLACK_RGB if node.color == BLACK else self.RED_RBG,
                (x, y), 20
            )
            text = self.font.render(("R" if node.isRoot else "") + str(node.car.price), True, self.BLACK_RGB, self.WHITE_RBG)
            newY = y + 50
            self.drawNode(node.left, x - 20 * nesting - (100 if isFirst else 0), newY, x, y, True, nesting - 1)
            self.drawNode(node.right, x + 20 * nesting + (100 if isFirst else 0), newY, x, y, False, nesting - 1)

        self.screen.blit(text, (x - 5, y - 10))

    def run(self, tree):

        while self.running:
            self.screen.fill((255, 255, 255))

            self.drawTree(tree)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        tree.insert(self.getRandomCar())

            self.clock.tick(self.fps)
            pygame.display.flip()

        pygame.quit()

    def getRandomCar(self):
        return Car(
            f"brand #{randint(0, 50)}",
            randint(0, 50),
            randint(0, 50),
            randint(0, 50),
            randint(0, 50),
        )
