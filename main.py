import pygame
import random


class Bird1:
    def __init__(self):
        self.x = 750
        self.y = random.randint(0, game.height / 2)
        self.image = pygame.image.load("bird1.png")
        self.image2 = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image2.get_rect()
        self.speed = 5

    def show(self):
        game.window.blit(self.image2, (self.x, self.y))

    def fly(self):
        self.x -= self.speed

    def hunt(self):
        if pygame.Rect.colliderect(Gun().rect, self.rect):
            return True
        else:
            return False


class Bird2:
    def __init__(self):
        self.x = -50
        self.y = random.randint(0, game.height / 2)
        self.image = pygame.image.load("bird2.png")
        self.image2 = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image2.get_rect()
        self.speed = 5

    def show(self):
        game.window.blit(self.image2, (self.x, self.y))

    def fly(self):
        self.x += self.speed

    def hunt(self):
        if pygame.Rect.colliderect(Gun().rect, self.rect):
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.x = game.width / 2
        self.y = game.height / 2
        self.score = 0
        self.shot = 3
        self.image = pygame.image.load("shooter.png")
        self.image2 = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image2.get_rect()
        self.sound = pygame.mixer.Sound("1.mp3")

    def show(self):
        game.window.blit(self.image2, (self.x, self.y))

    def shoot(self):
        self.sound.play()
        self.shot -= 1


class Game:
    def __init__(self):
        self.init = pygame.init()
        self.font = pygame.font.Font(None, 40)
        self.width = 700
        self.height = 500
        self.height = 500
        self.fps = 30
        self.window = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption("Bird Shot")
        self.icon = pygame.display.set_icon(pygame.image.load("icon.jpg"))
        self.bg = pygame.image.load("bg.jpg")
        self.bg2 = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clock = pygame.time.Clock()

    def pLay(self):
        pygame.mouse.set_visible(False)
        gun = Gun()
        birds1 = []
        birds2 = []

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    gun.x = pygame.mouse.get_pos()[0]
                    gun.y = pygame.mouse.get_pos()[1]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    gun.shoot()

                    for bird in birds1:
                        if bird.hunt() == True:
                            gun.score += 1
                            gun.shot += 2
                            birds1.remove(bird)

                    for bird in birds2:
                        if bird.hunt() == True:
                            gun.score += 1
                            gun.shot += 2
                            birds2.remove(bird)
            self.window.blit(self.bg2, (0, 0))
            gun.show()
            if random.random() < 0.03:
                birds1.append(Bird1())
            for bird in birds1:
                bird.show()
                bird.fly()
            if random.random() < 0.03:
                birds2.append(Bird2())
            for bird in birds2:
                bird.show()
                bird.fly()

            text = game.font.render(f"Score: {gun.score}", True, (0, 0, 0))
            game.window.blit(text, (0, 0))

            text = game.font.render(f"Shoot: {gun.shot}", True, (0, 0, 0))
            game.window.blit(text, (580, 0))

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = Game()
    game.pLay()
