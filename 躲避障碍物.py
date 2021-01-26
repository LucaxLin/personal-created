import pygame
import random
import sys


def set_level(score):
    speed = 10
    speed += score/5
    return speed


def drop_enemy(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])


def draw_enemy(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def enemy_falling(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos,enemy_pos):
            return True
    return False


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False


pygame.init()
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
background_color = (0, 0, 0)
width = 800
height = 600
player_size = 50
enemy_size = 50
enemy_pos = [random.randint(0, width-enemy_size), 0]
player_pos = [width/2, height-player_size*2]
enemy_list = [enemy_pos]
score = 0
my_font = pygame.font.SysFont('monospace', 35)
screen = pygame.display.set_mode((width, height))
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT and x - player_size > 0:
                x -= player_size/2
            elif event.key == pygame.K_RIGHT and x + player_size < width:
                x += player_size/2
            player_pos = [x, y]
    screen.fill(background_color)
    speed = set_level(score)
    if collision_check(enemy_list, player_pos):
        game_over = True
        print('Your final score is:', score)
        if score < 10:
            print('Come on, you can do better than that')
        elif score < 20:
            print('Really? Try one more time')
        elif score <= 50:
            print('Well Done!')
        else:
            print("YOU NAILED IT!!")
    drop_enemy(enemy_list)
    draw_enemy(enemy_list)
    score = enemy_falling(enemy_list, score)
    text = 'Score: ' + str(score)
    label = my_font.render(text, 1, yellow)
    screen.blit(label, (width - 200, height - 40))
    pygame.draw.rect(screen, red, (player_pos[0], player_pos[1], player_size, player_size))
    clock.tick(30)
    pygame.display.update()
