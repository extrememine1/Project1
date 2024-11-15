import pygame

# Initialisation
pygame.init()

objects = []
todraw = []

# Classes
class obj:
    def __init__(self, name, x, y, image):
        self.name = name
        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_width()  # Get width of image for hitbox
        self.height = image.get_height()  # Get height of image for hitbox

    def returnHitbox(self):
        # Return the hitbox as a pygame.Rect, which is easier for collision detection
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def returnInfo(self):
        return f'{self.name}:\n Coords: ({self.x}, {self.y})'

    def returnImage(self):
        return self.image

    def retrieveCoords(self):
        return self.x, self.y

    def updateCoords(self, x, y):
        self.x = x
        self.y = y

# Functions
def moveobject(id, incrementx, incrementy):
    objects[id].updateCoords(objects[id].retrieveCoords()[0] + incrementx, objects[id].retrieveCoords()[1] + incrementy)

def check_collision(obj1, obj2):
    return obj1.returnHitbox().colliderect(obj2.returnHitbox())

def findObj(name):
    for obj in objects:
        if obj.name == name:
            return obj
    return None

# Variables
finished = False
frame = pygame.time.Clock()
screenSize = (900, 700)
screen = pygame.display.set_mode(screenSize)
treasureFound = False

# Creating Background
background = pygame.image.load('background.png').convert_alpha()
background = pygame.transform.scale(background, screenSize)

# Creating player image
playerImage = pygame.transform.scale(pygame.image.load('player.png').convert_alpha(), (35, 40))
objects.append(obj('PlayerSprite', 450 - 35 / 2, 650, playerImage))

# Creating treasure
treasureImage = pygame.transform.scale(pygame.image.load('treasure.png').convert_alpha(), (40, 35))
objects.append(obj('TreasureSprite', 432.5, 25, treasureImage))

# Sprite 1
playerImage = pygame.transform.scale(pygame.image.load('bird1.jpg').convert_alpha(), (35, 40))
objects.append(obj('Sprite1', 147.5, 310, playerImage))

# Sprite 2
playerImage = pygame.transform.scale(pygame.image.load('fish1.jpg').convert_alpha(), (35, 40))
objects.append(obj('Sprite2', 792.5, 310, playerImage))

# Creating textWin
font = pygame.font.SysFont('comicsans', 60)
textWin = font.render('Great Job!', True, (0, 0, 0))

print(objects[2].name)

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN and pygame.key.name(event.key) == 'e':
            print(f'Player Coordinates: {objects[0].retrieveCoords()}')

    pressedKeys = pygame.key.get_pressed()

    # Movements
    if pressedKeys[pygame.K_s]:
        moveobject(0, 0, 5)
    if pressedKeys[pygame.K_d]:
        moveobject(0, 5, 0)
    if pressedKeys[pygame.K_w]:
        moveobject(0, 0, -5)
    if pressedKeys[pygame.K_a]:
        moveobject(0, -5, 0)

    # Checking for collision between player and treasure
    if check_collision(objects[0], objects[1]):
        treasureFound = True
        objects[1].updateCoords(-100, -100)
        

    # Clearing Screen to Draw
    screen.fill((0, 0, 0))

    # Drawing
    screen.blit(background, (0, 0))
    for obj in objects:
        screen.blit(obj.returnImage(), obj.retrieveCoords())

    if treasureFound:
        screen.blit(textWin, (300, 300))

    # Updating
    pygame.display.flip()
    frame.tick(60)

pygame.quit()
