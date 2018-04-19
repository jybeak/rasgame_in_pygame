import pygame

WHITE = (255, 255, 255)
pad_width = 600
pad_heigth = 480

def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))

def player(x,y):
    global gamepad, chicken
    gamepad.blit(chicken, (x,y))

def runGame():
    global gamepad, clock, chicken, background

    x = pad_heigth *0.05
    y = pad_heigth * 0.8
    x_change = 0
    y_change = 0

    background_x = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -15
                elif event.key == pygame.K_DOWN:
                    y_change = 15
                elif event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        y += y_change
        x += x_change



        gamepad.fill(WHITE)
        back(background_x, 0)
        player(x,y)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, chicken, background

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_heigth))
    pygame.display.set_caption('ChickenGun')
    chicken = pygame.image.load('resources/images/chicken.png')
    background = pygame.image.load('resources/images/background.png')

    clock = pygame.time.Clock()
    runGame()

initGame()

