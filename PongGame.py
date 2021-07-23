import pygame

pygame.init()

# Colour
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (124, 252, 0)
BLUE = (0, 191, 255)
ORANGE = (255, 140, 0)

# Screen
src_width = src_height = 600

screen = pygame.display.set_mode((src_width, src_height))
pygame.display.set_caption('Pong')
score_player_one = 0
score_player_two = 0
screen.fill(BLACK)

# Positional Variables

paddle_x = 0
paddle_y = 300
second_paddle_x = 596
second_paddle_y = 300
paddle_dx = paddle_dy = 1
ball_x = 200
ball_y = 300
ball_dx = 0
ball_dy = 0

# Miscellaneous Variables
colour = BLUE
radius = 10
width = 4
height = 100
winner = "blue"
writecolor = WHITE
retrycolor = WHITE
scored = False

# ScoreBoard
font = pygame.font.Font('freesansbold.ttf', 32)

#Text
start = font.render('Press Space to Start', True, WHITE, BLACK)
startRect = start.get_rect()
startRect.center = (300, 550)

run = True
while run == True:
    screen.fill(BLACK)
    pygame.draw.circle(screen, colour, (ball_x, ball_y), radius, radius-1)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, width, height))
    pygame.draw.rect(screen, ORANGE, (second_paddle_x, second_paddle_y, width, height))

    #Text for Player_One's Score
    player_one = font.render(str(score_player_one), True, WHITE, BLACK)
    player_oneRect = player_one.get_rect()
    player_oneRect.center = (200, 20)

    #Text for Player_Two's score
    player_two = font.render(str(score_player_two), True, WHITE, BLACK)
    player_twoRect = player_one.get_rect()
    player_twoRect.center = (400, 20)

    screen.blit(player_one, player_oneRect)
    screen.blit(player_two, player_twoRect)

    #End Screen Winner Text
    text = font.render(winner, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (300, 300)
    write = font.render('Quit?', True, writecolor, BLACK)
    writeRect = write.get_rect()
    writeRect.center = (400, 500)
    retry = font.render('Retry?', True, retrycolor, BLACK)
    retryRect = retry.get_rect()
    retryRect.center = (200, 500)

    key = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    retrycolor = WHITE
    writecolor = WHITE
    if (ball_dx == 0 and ball_dy == 0) or scored == True:
        screen.blit(start, startRect)

    if key[pygame.K_SPACE]:
        ball_dx = 1
        ball_dy = 1
        scored = False

    if -paddle_dx < paddle_y < 500 + paddle_dx:
        if key[pygame.K_w]:
            paddle_y -= paddle_dy

        if key[pygame.K_s]:
            paddle_y += paddle_dy

    if -paddle_dx == paddle_y:
        paddle_y = 0
    if paddle_y == (src_height - height) + paddle_dx:
        paddle_y = 500

    if -paddle_dx < second_paddle_y < 500 + paddle_dx:
        if key[pygame.K_UP]:
            second_paddle_y -= paddle_dy

        if key[pygame.K_DOWN]:
            second_paddle_y += paddle_dy

    if -paddle_dx == second_paddle_y:
        second_paddle_y = 0
    if second_paddle_y == (src_height - height) + paddle_dx:
        second_paddle_y = 500

    ball_x += ball_dx
    ball_y += ball_dy
    if ball_y < 0 + radius or ball_y > 600 - radius:
        ball_dy *= -1
    if ball_x == 600:
        ball_dy = ball_dx = 0
        score_player_one += 1
        ball_x = 200
        ball_y = 300
        ball_dx *= -1
        start = font.render('Press Space to Continue', True, WHITE, BLACK)
        scored = True

    if ball_x == 0:
        score_player_two += 1
        ball_x = 200
        ball_y = 300
        ball_dx *= -1
        ball_dy = ball_dx = 0
        start = font.render('Press Space to Continue', True, WHITE, BLACK)
        scored = True

    if ball_x - radius == 585 and second_paddle_y <= ball_y - radius <= second_paddle_y + height:
        if second_paddle_y <= ball_y < second_paddle_y + (height//2):
            ball_dy = abs(ball_dx)
            ball_dy *= -1
            ball_dx *= -1
            colour = ORANGE
        if second_paddle_y + (height//2) < ball_y <= second_paddle_y + height:
            ball_dy = abs(ball_dx)
            ball_dx *= -1
            colour = ORANGE
        if ball_y == second_paddle_y + (height//2):
            ball_dy *= -1
            ball_dx *= -1
            colour = ORANGE

    if ball_x - radius == 5 and paddle_y <= ball_y - radius <= paddle_y + height:
        if paddle_y <= ball_y < paddle_y + (height // 2):
            ball_dy = abs(ball_dx)
            ball_dy *= -1
            ball_dx *= -1
            colour = BLUE
        if paddle_y + (height // 2) < ball_y <= paddle_y + height:
            ball_dy = abs(ball_dx)
            ball_dx *= -1
            colour = BLUE
        if ball_y == paddle_y + (height // 2):
            ball_dy *= -1
            ball_dx *= -1
            colour = BLUE

    if score_player_one > score_player_two:
        winner = "Blue Won the Game"

    if score_player_two > score_player_one:
        winner = "Orange Won the Game"

    if score_player_one == 10 or score_player_two == 10:
        ball_dx = 0
        ball_dy = 0
        screen.fill(BLACK)
        screen.blit(text, textRect)
        screen.blit(write, writeRect)
        screen.blit(retry, retryRect)

        if 145 <= pos[0] <= 255 and 485 <= pos[1] <= 515:
            retrycolor = BLUE
            if click[0] == 1:
                score_player_one = 0
                score_player_two = 0
                
        if 355 <= pos[0] <= 445 and 485 <= pos[1] <= 515:
            writecolor = ORANGE
            if click[0] == 1:
                run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
quit()
