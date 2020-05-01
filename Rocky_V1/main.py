import pygame
from pygame import mixer
from settings import*

pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Rocky v.1 ")
clock = pygame.time.Clock()


def draw_text(words, screen, pos, size, colour, font_name, centered=False):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(words, False, colour)
    text_size = text.get_size()
    if centered:
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1]-text_size[1]//2
    screen.blit(text, pos)


def health_bars(player1_health, player2_health):




    if player1_health > 75:
        player1_health_color = green
    elif player1_health > 50:
        player1_health_color = yellow
    else:
        player1_health_color = red

    if p2_health <= 0:
        draw_text("KO, Player 1 Wins ", win, [500, 50], 18, WHITE, START_FONT, centered=True)

    if player2_health > 75:
        player2_health_color = green
    elif player2_health > 50:
        player2_health_color = yellow
    else:
        player2_health_color = red

    pygame.draw.rect(win,player1_health_color, (20,75, player1_health,15))
    pygame.draw.rect(win, player2_health_color, (880, 75, player2_health, 15))






def collision():
    if player2_x - player1_x <= 210 and left_jab_p:
        print("left jab hit")
        return True

    elif player2_x - player1_x <= 130 and right_jab_p:
        print("right jab hit")
        return True

    elif player2_x - player1_x <= 150 and uppercut_p:
        print("uppercut hit")
        return True

    elif player2_x - player1_x <= 150 and hook_p:
        print("hook hit")
        return True
    else:
        return False


def drawWindow():
    global animCount
    global p1_health
    global p2_health
    global pl
    global player_stand2
    global collision_left_jab

    win.blit(bg, (0, 0))
    if player_stand2 == True:
        win.blit(playerStand2, (player2_x, player2_y))
    health_bars(p1_health,p2_health)

    if KO:
        player_stand2 = False
        collision_left_jab = False
        win.blit(knock_out[animCount//5], (player2_x, player2_y))
        win.blit(knocked_out, (player2_x, player2_y))
        animCount += 1

    if collision_left_jab:
        player_stand2 = False
        win.blit(player2_hit_array[animCount], (player2_x, player2_y))
        animCount += 1



    if left_jab_p:

        win.blit(left_jab[animCount // 5], (player1_x, player1_y))

        animCount += 1


    if right_jab_p:
        win.blit(right_jab[animCount // 5], (player1_x, player1_y))

        animCount += 1

    if uppercut_p:
        win.blit(uppercut[animCount // 5], (player1_x, player1_y))

        animCount += 1

    if hook_p:
        win.blit(hook[animCount // 5], (player1_x, player1_y))
        animCount += 1


    if left:

        win.blit(walkLeft[animCount // 6], (player1_x,player1_y))
        animCount += 1
    if right:

        win.blit(walkRight[animCount // 6], (player1_x, player1_y))
        animCount += 1




    elif player_stand1:
        win.blit(playerStand1, (player1_x, player1_y))

    pygame.display.update()


run = True
while run:
    FPS = 15
    clock.tick(30)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()
    pygame_events = pygame.event.get()


    if keys[pygame.K_LEFT] and player1_x > 10:

        player_stand1 = False
        player1_x -= speed


        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and player1_x < 700:
        player_stand1 = False
        player1_x += speed


        right = True
        left = False
        lastMove = "right"

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:


            left_jab_p = True
            collision()


            right_jab_p = False
            uppercut_p = False
            hook_p = False
            player_stand1 = False

            if collision() and p2_health >= 0:

                collision_left_jab = True
                p2_health -= 5
                pygame.display.update()
            elif collision() and p2_health <=0:
                collision_left_jab = False
                KO = True
            else:
                player_stand2 = True
                collision_left_jab = False
                pygame.display.update()


        elif event.key == pygame.K_d:
            if collision() and p2_health >=0:
                collision_left_jab = True
                p2_health -= 5
                pygame.display.update()
                player_stand2 = True
                pygame.display.update()

            right_jab_p = True
            collision()
            left_jab_p = False
            uppercut_p = False
            hook_p = False
            player_stand1 = False

        elif event.key == pygame.K_s:
            if collision() and p2_health >= 0:
                collision_left_jab = True
                p2_health -= 15
                pygame.display.update()
                player_stand2 = True
                pygame.display.update()

            uppercut_p = True
            collision()
            right_jab_p = False
            left_jab_p = False
            player_stand1 = False
            hook_p = False

        elif event.key == pygame.K_w:
            if collision() and p2_health >= 0:
                collision_left_jab = True
                pygame.display.update()
                p2_health -= 10
            else:
                player_stand2 = True
                pygame.display.update()

            hook_p = True
            collision()
            uppercut_p = False
            right_jab_p = False
            left_jab_p = False
            player_stand1 = False


        else:
            left_jab_p = False
            right_jab_p = False
            uppercut_p = False
            player_stand1 = True
            player_stand2 = True
            hook_p = False
            collision_left_jab = False
            pygame.display.update()



    elif keys[pygame.K_ESCAPE]:
        run = False


    else:
        left = False
        right = False
        animCount = 0


    drawWindow()



pygame.quit()







