
import pygame, sys, random

pygame.init()
screen_height, screen_width=400,600

screen = pygame.display.set_mode((600,400))

pygame.display.set_caption("ping pong")
clock = pygame.time.Clock()

def ball_animation():
    global ball_speed_x, ball_speed_y,player_score,opponent_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        opponent_score+=1
        restart()
    if ball.right >= screen_width:
        player_score+=1
        restart() 
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
        

def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def restart():
    global ball_speed_x,ball_speed_y
    
    ball.center= (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


ball = pygame.Rect(screen_width / 2, screen_height / 2, 7,7)
player = pygame.Rect(590,200, 5,50)
opponent = pygame.Rect(10, 200,5,50)
    
ball_speed_x = 3 *random.choice((1,-1))
ball_speed_y = 3 *random.choice((1,-1))
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

run = True
ballalive=True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:#player speed chenged(0 innitially) it until key is pressed
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6
    
    #Game Logic
    ball_animation()
    player_animation()                             #player speed constantly adding
    opponent_ai()

    # Visuals 
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)   #player rect
    pygame.draw.rect(screen, light_grey, opponent) #opponent rect
    pygame.draw.ellipse(screen, light_grey, ball)  #ball
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

    player_text = basic_font.render(f'{player_score}',False,light_grey)
    screen.blit(player_text,(270,10))

    opponent_text = basic_font.render(f'{opponent_score}',False,light_grey)
    screen.blit(opponent_text,(315,10))
    
    pygame.display.flip()
    clock.tick(60)   

pygame.quit()