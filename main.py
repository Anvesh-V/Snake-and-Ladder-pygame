import pygame
from sys import exit
from random import randint


def board():
    for i in range(10):
        for j in range(10):
            screen.blit(box_surf, (40 + (i * 41), 40 + (j * 41)))
            if j % 2 == 1:
                numb = defont.render(f'{9 - j}{i}', True, 'black')
            else:
                numb = defont.render(f'{9 - j}{9 - i}', True, 'black')
            screen.blit(numb, (40 + (i * 41), 40 + (j * 41)))


def snake_lad_board():
    screen.blit(pygame.transform.rotozoom(snake_surf, 302, 0.38), player_pos('52'))
    screen.blit(pygame.transform.rotozoom(snake_surf, 205, 0.38), player_pos('59'))  # 56
    screen.blit(pygame.transform.rotozoom(snake_surf, 270, 0.39), player_pos('76'))
    screen.blit(pygame.transform.rotozoom(snake_surf, 232, 1.09), player_pos('98'))  # 87
    screen.blit(pygame.transform.rotozoom(snake_surf, 330, 0.6), player_pos('95'))
    screen.blit(pygame.transform.rotozoom(snake_surf, 270, 0.38), player_pos('97'))

    screen.blit(pygame.transform.rotozoom(ladder_surf, 135, 0.45), player_pos('21'))  # 3
    screen.blit(pygame.transform.rotozoom(ladder_surf, 252, 0.5), player_pos('31'))  # 8

    screen.blit(pygame.transform.rotate(long_ladder, 304), player_pos('84'))  # 28
    screen.blit(pygame.transform.rotozoom(ladder_surf, 62, 0.44), player_pos('78'))  # 58

    screen.blit(pygame.transform.rotate(short_ladder, 90), player_pos('85'))  # 74
    screen.blit(pygame.transform.rotozoom(short_ladder, 45, 1), player_pos('99'))  # 80
    screen.blit(pygame.transform.rotozoom(short_ladder, 135, 1), player_pos('91'))  # 89

    screen.blit(pygame.transform.rotozoom(snake_surf, -6, 0.56), player_pos('17'))


def player_pos(p_pos):
    if len(p_pos) == 1:
        a, b = '0', p_pos

    else:
        a, b = p_pos[0], p_pos[1]
    a, b = int(a), int(b)
    py = 410 - (a * 41)
    if a % 2 == 0:
        px = 40 + b * 41
    else:
        px = 410 - (b * 41)
    return px, py


def s_and_l_check(p_pos):
    global ladsnek_pos
    p_int = int(p_pos)
    if p_int in ladsnek_pos:
        p_int = ladsnek_pos.get(p_int)
        p_int = str(p_int)
        if len(p_int) == 1:
            p_int = '0' + p_int
        return str(p_int)
    else:
        return str(p_pos)


def roll():
    global turn, menu, winner, rol, p_all_pos
    rol = True
    numb = randint(1, 6)
    p_all_pos[turn] = str(int(p_all_pos[turn]) + numb)
    p_all_pos[turn] = s_and_l_check(int(p_all_pos[turn]))
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 3
    elif turn == 3:
        turn = 4
    elif turn == 4:
        turn = 1

    for i in p_all_pos:
        if int(p_all_pos[i]) > 99:
            winner = i
            menu = 3
    return numb


def win_screen(w):
    if winner == 1:
        screen.fill('red')
        w = 'Red'
    elif winner == 2:
        screen.fill('blue')
        w = 'Blue'
    elif winner == 3:
        screen.fill('green')
        w = 'Green'
    elif winner == 4:
        screen.fill('yellow')
        w = 'Yellow'
    return w


ladsnek_pos = {3: 21, 8: 30, 28: 84, 58: 77, 74: 85, 80: 98, 89: 91, 17: 7, 52: 29, 56: 40, 76: 43, 87: 18, 95: 69,
               97: 62}
winner = 0
rol = False
sc_wid = 600
sc_hei = 600
menu = 0

pygame.init()
screen = pygame.display.set_mode((sc_wid, sc_hei))
pygame.display.set_caption(title='Test')
fps = pygame.time.Clock()
defont = pygame.font.SysFont('', 40, True)

start_surf = defont.render('Press SPACE to Start', False, (255, 255, 255))
start_rect = start_surf.get_rect(center=(sc_wid // 2, sc_hei // 2))

help_text1 = defont.render('HOW TO PLAY :', False,'white')
help_text2 = defont.render("Press ROLL button or 'R' Key to Roll", False,'white')

esc_text = defont.render('Press Esc to Pause', False,'white')
front_text = defont.render('Order of Players: Red -> Blue -> Green -> Yellow', False, 'white')

b_roll_surf = pygame.image.load('button.png').convert()
b_roll_rect = b_roll_surf.get_rect(midright=(560, 300))

ladder_surf = pygame.image.load('ladder.png').convert_alpha()
long_ladder = pygame.transform.scale(ladder_surf, (300, 35))
short_ladder = pygame.transform.scale(ladder_surf, (70, 35))
snake_surf = pygame.image.load('snake.png').convert_alpha()

box_surf = pygame.image.load('box.png').convert()
box_rect = box_surf.get_rect()
box_x = 40
box_y = 40

# PLAYERS
turn = 1
p_all_pos = {1: '00', 2: '00', 3: '00', 4: '00'}
# red 1
p_red_surf = pygame.image.load('red_p.png').convert_alpha()
p_red_rect = p_red_surf.get_rect()
# blue 2
p_blue_surf = pygame.image.load('blue_p.png').convert_alpha()
p_blue_rect = p_blue_surf.get_rect()
# green 3
p_green_surf = pygame.image.load('green_p.png').convert_alpha()
p_green_rect = p_green_surf.get_rect()
# yellow 4
p_yellow_surf = pygame.image.load('yellow_p.png').convert_alpha()
p_yellow_rect = p_yellow_surf.get_rect()
num = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if menu == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = 1
        elif menu == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = 2
                if event.key == pygame.K_r:
                    num = roll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_roll_rect.collidepoint(pygame.mouse.get_pos()):
                    num = roll()
        elif menu == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = 1
    if menu == 0:
        screen.fill((51, 41, 105))
        screen.blit(start_surf, start_rect)
    elif menu == 1:
        screen.fill((0, 40, 40))
        board()
        snake_lad_board()
        screen.blit(b_roll_surf, b_roll_rect)
        screen.blit(pygame.transform.scale_by(front_text,0.8),(40,480))
        screen.blit(pygame.transform.scale_by(esc_text,0.8),(40,5))

        if rol:
            screen.blit(pygame.transform.scale_by(defont.render(f"YOU ROLLED A {num}", True, 'white'), 0.6), (456, 150))

        p_red_rect.topleft = player_pos(p_all_pos[1])
        p_red_rect.x -= 6
        screen.blit(p_red_surf, p_red_rect)

        p_blue_rect.topleft = player_pos(p_all_pos[2])
        p_blue_rect.x -= 2
        screen.blit(p_blue_surf, p_blue_rect)

        p_green_rect.topleft = player_pos(p_all_pos[3])
        p_green_rect.x += 6
        screen.blit(p_green_surf, p_green_rect)

        p_yellow_rect.topleft = player_pos(p_all_pos[4])
        p_yellow_rect.x += 2
        screen.blit(p_yellow_surf, p_yellow_rect)


    elif menu == 2:
        screen.fill((100, 42, 125))
        screen.blit(help_text1, (50,80))
        screen.blit(help_text2,(50,120))


    elif menu == 3:
        win_text = defont.render(f"PLAYER {win_screen(winner)} WON", False, 'white')
        win_rect = win_text.get_rect(center=(sc_wid // 2, sc_hei // 2))
        screen.blit(win_text, win_rect)

    fps.tick(30)
    pygame.display.update()