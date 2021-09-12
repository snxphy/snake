import pygame, sys
import time
import random

#general setup
pygame.init()
clock = pygame.time.Clock()
FPS = 60

#colour
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

#snake
snake_size = 10
snake_speed = 15

#font
message_font = pygame.font.SysFont("freesansbold.ttf", 30)
score_font = pygame.font.SysFont("freesansbold.ttf", 25)

#screen
screen_width = 540
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

#score
def print_score(score):
    text = score_font.render("Score: " + str(score), True, white)
    screen.blit(text, [0,0])

#snake
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():

    game_over = False
    game_close = False

    x = screen_width /2
    y = screen_height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_food_x = round(random.randrange(0, screen_width-snake_size) / 10.0) * 10.0
    target_food_y = round(random.randrange(0, screen_height-snake_size) / 10.0) * 10.0
    
    #loop
    while not game_over:

        while game_close:
            screen.fill(black)
            game_over_message = message_font.render("Game Over", True, red)
            screen.blit(game_over_message, [screen_width / 3, screen_height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over= True
                        game_close = False
                    if event.key == pygame.K_r:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False



        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()

            #movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
            
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
            
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
            
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        screen.fill(black)
        pygame.draw.rect(screen, green, [target_food_x, target_food_y, snake_size, snake_size])
        
        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()
        if x == target_food_x and y == target_food_y:
            target_food_x = round(random.randrange(0, screen_width-snake_size) / 10.0) * 10.0
            target_food_y = round(random.randrange(0, screen_height-snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.display.flip
    pygame.quit()
    sys.exit()
run_game()