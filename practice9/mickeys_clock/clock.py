import pygame
import datetime
from pathlib import Path

path = Path(__file__).parent/"images"

pygame.init()
screen = pygame.display.set_mode((1200,700))
white = (255,255,255)

base = pygame.image.load(path/"clock.png").convert_alpha()
mouse = pygame.image.load(path/"mUmrP.png").convert_alpha()
hand_l = pygame.image.load(path/"hand_left.png").convert_alpha()
hand_r = pygame.image.load(path/"hand_right.png").convert_alpha()
hand_s = pygame.image.load(path/"hand_right.png").convert_alpha() 


resized_bg = pygame.transform.scale(base, (800,600))
resized_mouse = pygame.transform.scale(mouse,(350,350))


hand_l_base = pygame.transform.scale(hand_l,(80,80))
hand_r_base = pygame.transform.scale(hand_r,(100,100))

CLOCK_CENTER = (600,320)
clock = pygame.time.Clock()

MIN_HAND_CENTER = (610, 280) 
HOUR_HAND_CENTER = (605, 290)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second

    min_angle = -(m*6 + s*0.1)
    h_angle   = -(h*30 + m*0.5)

    rotated_mins  = pygame.transform.rotate(hand_l_base, min_angle)
    rotated_hours = pygame.transform.rotate(hand_r_base, h_angle)

    mins_rect   = rotated_mins.get_rect(center=MIN_HAND_CENTER)
    hours_rect  = rotated_hours.get_rect(center=HOUR_HAND_CENTER)

    screen.fill(white)
    bg_rect = resized_bg.get_rect(center=CLOCK_CENTER)
    mouse_rect = resized_mouse.get_rect(center=CLOCK_CENTER)
    screen.blit(resized_bg, bg_rect)
    screen.blit(resized_mouse, mouse_rect)
    screen.blit(rotated_hours, hours_rect)
    screen.blit(rotated_mins, mins_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()