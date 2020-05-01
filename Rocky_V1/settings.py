import pygame

player1_x = 50
player1_y = 500
player2_x = 600
player2_y = 500


green = (90, 245, 66)
red = (245, 66, 66)
yellow =(245, 239, 66)
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255, 255, 255)
START_FONT = 'arial black'
speed = 20


p1_health = 100
p2_health = 100
timer = 1

KO = False
left_jab_p = False
right_jab_p = False
uppercut_prep = False
uppercut_p = False
hook_p = False
collision_left_jab = False

left = False
right = False

animCount = 0
player_stand1 = True
player_stand2 = True
lastMove = "right"



####################################### images #############################

playerStand1 = pygame.image.load('pics/idle1.png')
playerStand2 = pygame.image.load('pics/p2_idle.png')
player2hit = pygame.image.load('pics/hit_pic.png')
bg = pygame.image.load("pics/ring.jpg")
knocked_out = pygame.image.load("pics/hit_pic3.png")



player2_hit_array = [ pygame.image.load('pics/hit_pic.png'),
                      pygame.image.load('pics/hit_pic.png'),
                      pygame.image.load('pics/hit_pic.png'),
                      pygame.image.load('pics/hit_pic.png'),
                      pygame.image.load('pics/hit_pic.png'),
                      pygame.image.load('pics/hit_pic.png'),
                 ]


knock_out = [pygame.image.load('pics/hit_pic.png'),
             pygame.image.load('pics/hit_pic2.png'),
             pygame.image.load('pics/hit_pic3.png'),
             pygame.image.load('pics/hit_pic.png'),
             pygame.image.load('pics/hit_pic2.png'),
             pygame.image.load('pics/hit_pic3.png')
             ]

walkRight = [pygame.image.load('pics/right_leg1.png'),
             pygame.image.load('pics/left_leg1.png'),
             pygame.image.load('pics/right_leg1.png'),
             pygame.image.load('pics/left_leg1.png'),
             pygame.image.load('pics/right_leg1.png'),
             pygame.image.load('pics/left_leg1.png')]

walkLeft = [pygame.image.load('pics/right_leg1.png'),
            pygame.image.load('pics/idle1.png'),
            pygame.image.load('pics/right_leg1.png'),
            pygame.image.load('pics/idle1.png'),
            pygame.image.load('pics/right_leg1.png'),
            pygame.image.load('pics/idle1.png'),
            ]

left_jab = [pygame.image.load('pics/left_jab.png'),
            pygame.image.load('pics/left_jab.png'),
            pygame.image.load('pics/left_jab.png'),
            pygame.image.load('pics/left_jab.png'),
            pygame.image.load('pics/left_jab.png'),
            pygame.image.load('pics/left_jab.png'),
            ]

right_jab = [pygame.image.load('pics/right_jab.png'),
             pygame.image.load('pics/right_jab.png'),
             pygame.image.load('pics/right_jab.png'),
             pygame.image.load('pics/right_jab.png'),
             pygame.image.load('pics/right_jab.png'),
             pygame.image.load('pics/right_jab.png'),
             ]

uppercut = [pygame.image.load('pics/uppercut_prep.png'),
            pygame.image.load('pics/uppercut.png'),
            pygame.image.load('pics/uppercut_prep.png'),
            pygame.image.load('pics/uppercut.png'),
            pygame.image.load('pics/uppercut_prep.png'),
            pygame.image.load('pics/uppercut.png'),
            pygame.image.load('pics/uppercut_prep.png'),
            pygame.image.load('pics/uppercut.png'),

             ]

hook = [pygame.image.load('pics/hook_prep.png'),
        pygame.image.load('pics/hook.png'),
        pygame.image.load('pics/hook_prep.png'),
        pygame.image.load('pics/hook.png'),
        pygame.image.load('pics/hook_prep.png'),
        pygame.image.load('pics/hook.png'),
        ]


