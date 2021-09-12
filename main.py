import pygame, sys, random
from pygame.constants import K_DOWN


from pygame.draw import ellipse

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, pong_sound, score_sound #allows python to run code without trying to find local function (simple programming solution only)
    #speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #border collision
    if ball.top <= 0 or ball.bottom >= screen_height:  #vertical/y axis
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        ball_start()
    if ball.right >= screen_width:   #horizontal/x axis
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        ball_speed_x *= -1
    
    #ball restart
        ball_start()

    #player collision pygame.mixer.Sound.play(pong_sound)
    if ball.colliderect(player) and ball_speed_x > 0:
	    if abs(ball.right - player.left) < 10:
		    ball_speed_x *= -1	
	    elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
		    ball_speed_y *= -1
	    elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
		    ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
	    if abs(ball.left - opponent.right) < 10:
		    ball_speed_x *= -1	
	    elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
		    ball_speed_y *= -1
	    elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
		    ball_speed_y *= -1

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = -1
	if player.bottom >= screen_height:
		player.bottom = screen_height -1

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
	    opponent.top = 0
    if opponent.bottom >= screen_height:
	    opponent.bottom = screen_height

def ball_start():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

#general setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock() 

#screen
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#rectangle (game)
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#colour ref
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#speed
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 8

#text
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

#sound
pong_sound = pygame.mixer.Sound("pong (1).ogg")
score_sound = pygame.mixer.Sound("score.ogg")

#loop
while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_speed -= 0.5
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_speed += 0.5
          
        
    #logic
    ball_animation()
    player_animation()
    opponent_ai()
    
   
    #visual
    screen.fill(bg_color)
    #objects (drawn)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw,ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))
    #text visual
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text,(660,470))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text,(605,470))

    #window update
    pygame.display.flip()
    clock.tick(60) #ticks per sec 