import pygame

#init
pygame.init()
# variable running game
isRun = True

# create  a display surface object
window_width = 500
window_length = 500
window = pygame.display.set_mode((window_width,window_length))

# object game
# position
x = 250
y = 250

# size
length = 20
width = 20

# movement speed
speed = 5 

while isRun:
    pygame.time.delay(10)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # take all keyboard press
    keys = pygame.key.get_pressed()

    # move to left
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < window_width-width:
        x += speed

    if keys[pygame.K_DOWN] and y < window_length-length:
        y += speed
    
    if keys[pygame.K_UP] and y > 0:
        y -= speed


    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(0,142,204),(x,y,width,length))
    # rendering to display
    pygame.display.update()

pygame.quit()


