
import pygame
import time
import exp_random
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
class Buttonplay:
    def __init__(self, x, y, width, height,text1, image_before, image_after_par = None,sound_par=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text1
        self.image = pygame.image.load(image_before)
        self.image = pygame.transform.scale(self.image,(width,height))
        if image_after_par:
            self.image_after = pygame.image.load(image_after_par)
            self.image_after = pygame.transform.scale(self.image_after,(width,height))
        self.rect = self.image.get_rect(topleft=(x,y))
        if sound_par:
            self.sound = pygame.mixer.Sound(sound_par)
        self.is_mouse = False

    def draw(self,screen1):
        current_image = self.image_after if self.is_mouse else self.image
        screen1.blit(current_image,self.rect.topleft)
        font = pygame.font.SysFont('',70)
        text_surface = font.render(self.text,True, (184, 159, 209))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen1.blit(text_surface,text_rect)


    def check_image_after(self,mouse_pos):
        self.is_mouse = self.rect.collidepoint(mouse_pos)
    def future_event(self,event1):
        global Gameplay
        if event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1 and self.is_mouse:
            Gameplay = True
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT,button = self))

class Buttonquit:
    def __init__(self, x, y, width, height, text1, image_before, image_after_par = None,sound_par=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text1
        self.image = pygame.image.load(image_before)
        self.image = pygame.transform.scale(self.image,(width,height))
        if image_after_par:
            self.image_after = pygame.image.load(image_after_par)
            self.image_after = pygame.transform.scale(self.image_after,(width,height))
        self.rect = self.image.get_rect(topleft=(x,y))
        if sound_par:
            self.sound = pygame.mixer.Sound(sound_par)
        self.is_mouse = False
    def draw2(self,screen1):
        current_image = self.image_after if self.is_mouse else self.image
        screen1.blit(current_image,self.rect.topleft)
        font = pygame.font.SysFont('',70)
        text_surface = font.render(self.text,True, (184, 159, 209))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen1.blit(text_surface,text_rect)
    def check_image_after2(self,mouse_pos):
        self.is_mouse = self.rect.collidepoint(mouse_pos)
    def future_event2(self,event1):
        global running
        if event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1 and self.is_mouse:
            running = False
            pygame.quit()
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT,button = self))

class Buttonquitingame:
    def __init__(self,x,y,width,height,text1,image_before,image_after_par = None,sound_par=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text1
        self.image = pygame.image.load(image_before)
        self.image = pygame.transform.scale(self.image,(width,height))
        if image_after_par:
            self.image_after = pygame.image.load(image_after_par)
            self.image_after = pygame.transform.scale(self.image_after,(width,height))
        self.rect = self.image.get_rect(topleft=(x,y))
        if sound_par:
            self.sound = pygame.mixer.Sound(sound_par)
        self.is_mouse = False
    def draw3(self,screen1):
        global Gameplay
        if Gameplay:
            current_image = self.image_after if self.is_mouse else self.image
            screen1.blit(current_image,self.rect.topleft)
            font = pygame.font.SysFont('',30)
            text_surface = font.render(self.text,True, (67, 191, 75))
            text_rect = text_surface.get_rect(center = self.rect.center)
            screen1.blit(text_surface,text_rect)
    def check_image_after3(self,mouse_pos):
        self.is_mouse = self.rect.collidepoint(mouse_pos)
    def future_event3(self,event1):
        global Gameplay
        if event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1 and self.is_mouse:
            Gameplay = False
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT,button = self))


watching = False
class Promptinglist:
    def __init__(self,x,y,width,height,text1,image_before,image_after_par = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text1
        self.image = pygame.image.load(image_before)
        self.image = pygame.transform.scale(self.image,(width,height))
        if image_after_par:
            self.image_after = pygame.image.load(image_after_par)
            self.image_after = pygame.transform.scale(self.image_after,(width,height))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.is_mouse = False
    def draw4(self,screen1):
        global Gameplay
        if Gameplay:
            current_image = self.image_after if self.is_mouse else self.image
            screen1.blit(current_image,self.rect.topleft)
            font = pygame.font.SysFont('',30)
            text_surface = font.render(self.text,True, (67, 191, 75))
            text_rect = text_surface.get_rect(center = self.rect.center)
            screen1.blit(text_surface,text_rect)
    def check_image_after4(self,mouse_pos):
        self.is_mouse = self.rect.collidepoint(mouse_pos)
    def future_event4(self):
        if self.is_mouse:
            screen.blit(prompting_list, (900, 150))
            screen.blit(prompting_box,(960,200))
            screen.blit(stone,(1030,200))
            screen.blit(gun_right,(1100,190))
            screen.blit(plus,(990,200))
            screen.blit(same, (1063,200))
            screen.blit(two,(1015,200))
            screen.blit(six,(935,192))
            pygame.event.post(pygame.event.Event(pygame.USEREVENT,button = self))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1366,768))
image_path1 = 'images/background_for_game_FULLSCREEN.png'
background = pygame.image.load(image_path1).convert_alpha()
background_x = 0
font_berry = pygame.font.SysFont('',60)
font_block = pygame.font.SysFont('',60)
font_stones = pygame.font.SysFont('',60)
font_bullets = pygame.font.SysFont('',60)
font_killors = pygame.font.SysFont('',60)
image_path2 = 'images/menu_for_game.png'
main_menu = pygame.image.load(image_path2).convert_alpha()
text = pygame.font.SysFont('',120)
main_text = text.render('Project game',True,(184, 159, 209))
help_text = pygame.font.SysFont('',60)
main_text_help = help_text.render('Press D',True,(45, 179, 186))
none_text = pygame.font.SysFont('',60)
none_text_help = none_text.render('Not enough',True,(45, 179, 186))
end_b = pygame.font.SysFont('',60)
end_of_berryes = end_b.render("It's over",True,(45, 179, 186))
stone_text = pygame.font.SysFont('',20)
stone_text_total = stone_text.render('Press D',True,(45, 179, 186))
stone_text_end = pygame.font.SysFont('',20)
stone_text_total_end = stone_text_end.render("It's over",True,(45, 179, 186))
#########################################
image_path3 = 'images/prompting_list.png'
prompting_list = pygame.image.load(image_path3).convert_alpha()
image_path4 = 'images/prompting_block.png'
prompting_box = pygame.image.load(image_path4).convert_alpha()
image_path5 = 'images/plus.png'
plus = pygame.image.load(image_path5).convert_alpha()
image_path6 = 'images/same.png'
same = pygame.image.load(image_path6).convert_alpha()
image_path7 = 'images/two.png'
two = pygame.image.load(image_path7).convert_alpha()
image_path8 = 'images/six.png'
six = pygame.image.load(image_path8).convert_alpha()
##########################################
dead_text_help = pygame.font.SysFont('',170)
dead_text = dead_text_help.render('YOU DEAD',True,(194, 10, 10))
image_path9 = 'images/cool_icon.png'
icon = pygame.image.load(image_path9).convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption('Game 1.0')
image_path10 = 'images/mine_background_music.mp3'
pygame.mixer.music.load(image_path10)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
image_path10 = 'images/mine_background_music.mp3'
image_path110 = 'images/have_food.mp3'
food_sound = pygame.mixer.Sound(image_path110)
food_sound.set_volume(0.4)
image_path11 = 'images/touch_axe.mp3'
axe_sound = pygame.mixer.Sound(image_path11)
image_path12 = 'images/dead_sound.mp3'
dead_sound = pygame.mixer.Sound(image_path12)
image_path13 = 'images/berry_sound.mp3'
berry_sound = pygame.mixer.Sound(image_path13)
image_path14 = 'images/pain.mp3'
pain_sound = pygame.mixer.Sound(image_path14)
image_path15 = 'images/shot_sound.mp3'
shot_sound = pygame.mixer.Sound(image_path15)
image_path16 = 'images/box_broken.mp3'
box_broken = pygame.mixer.Sound(image_path16)
image_path17 = 'images/monument_is_broken.mp3'
monument_is_broken = pygame.mixer.Sound(image_path17)

image_path18 = 'images/primary_character_left1.png'
view_left_quietness = pygame.image.load(image_path18).convert_alpha()
image_path19 = 'images/primary_character_right1.png'
view_right_quietness = pygame.image.load(image_path19).convert_alpha()
image_path20 = 'images/primary_character_left1.png'
one_left = pygame.image.load(image_path20).convert_alpha()
image_path21 = 'images/primary_character_right1.png'
two_right = pygame.image.load(image_path21).convert_alpha()
image_path22 = 'images/death_right.png'
dead_right = pygame.image.load(image_path22).convert_alpha()
image_path23 = 'images/death_left.png'
dead_left = pygame.image.load(image_path23).convert_alpha()
image_path24 = 'images/death_monument.png'
dead_movement = pygame.image.load(image_path24).convert_alpha()
image_path25 = 'images/stripe_up.png'
strelka = pygame.image.load(image_path25).convert_alpha()
image_path26 = 'images/strelka_little.png'
strelka_little = pygame.image.load(image_path26).convert_alpha()
image_path27 = 'images/strelka_stone_below.png'
strelka_stone_below = pygame.image.load(image_path27).convert_alpha()
image_path28 = 'images/axe_left.png'
axe_left = pygame.image.load(image_path28).convert_alpha()
image_path29 = 'images/axe_right.png'
axe_right = pygame.image.load(image_path29).convert_alpha()
image_path30 = 'images/pistolet_left.png'
gun_left = pygame.image.load(image_path30).convert_alpha()
image_path31 = 'images/pistolet_right.png'
gun_right = pygame.image.load(image_path31).convert_alpha()
image_path32 = 'images/little_bullet.png'
bullet_right = pygame.image.load(image_path32).convert_alpha()
image_path33 = 'images/little_bullet_left.png'
bullet_left = pygame.image.load(image_path33).convert_alpha()
image_path34 = 'images/bullet_for_game.png'
icon_bullet_right = pygame.image.load(image_path34).convert_alpha()
image_path35 = 'images/bullet_for_game_left.png'
icon_bullet_left = pygame.image.load(image_path35).convert_alpha()
image_path36 = 'images/award1.png'
award1 = pygame.image.load(image_path36).convert_alpha()
image_path37 = 'images/award2.png'
award2 = pygame.image.load(image_path37).convert_alpha()
image_path38 = 'images/award3.png'
award3 = pygame.image.load(image_path38).convert_alpha()
image_path39 = 'images/berry_for_game.png'
fruits = pygame.image.load(image_path39).convert_alpha()
image_path40 = 'images/pine_block.png'
pine_block = pygame.image.load(image_path40).convert_alpha()
image_path41 = 'images/berry_for_game_value.png'
berry = pygame.image.load(image_path41).convert_alpha()
image_path42 = 'images/blocks_for_game.png'
block = pygame.image.load(image_path42).convert_alpha()
image_path43 = 'images/blocks_for_game.png'
block_house = pygame.image.load(image_path43).convert_alpha()
image_path44 = 'images/yellow_star.png'
help_star = pygame.image.load(image_path44).convert_alpha()
image_path45 = 'images/stone.png'
stone = pygame.image.load(image_path45).convert_alpha()
image_path46 = 'images/Icon_stone.png'
icon_stone = pygame.image.load(image_path46).convert_alpha()
image_path47 = 'images/desk_for_game.png'
desk = pygame.image.load(image_path47).convert_alpha()
image_path48 = 'images/present_box.png'
present_box = pygame.image.load(image_path48).convert_alpha()
image_path49 = 'images/head.png'
headgg = pygame.image.load(image_path49).convert_alpha()

image_path51 = 'images/primary_character_left1.png'
image_path52 = 'images/primary_character_left2.png'
image_path53 = 'images/primary_character_left1.png'
image_path54 = 'images/primary_character_left3.png'
character_view_left = [
    pygame.image.load(image_path51).convert_alpha(),
    pygame.image.load(image_path52).convert_alpha(),
    pygame.image.load(image_path53).convert_alpha(),
    pygame.image.load(image_path54).convert_alpha()
]
image_path55 = 'images/primary_character_right1.png'
image_path56 = 'images/primary_character_right2.png'
image_path57 = 'images/primary_character_right1.png'
image_path58 = 'images/primary_character_right3.png'
character_view_right = [
    pygame.image.load(image_path55).convert_alpha(),
    pygame.image.load(image_path56).convert_alpha(),
    pygame.image.load(image_path57).convert_alpha(),
    pygame.image.load(image_path58).convert_alpha()
]
image_path59 = 'images/health1.png'
image_path60 = 'images/health2.png'
image_path61 = 'images/health3.png'
image_path62 = 'images/health4.png'
image_path63 = 'images/health5.png'
image_path64 = 'images/health6.png'
heart_list = [
    pygame.image.load(image_path59).convert_alpha(),
    pygame.image.load(image_path60).convert_alpha(),
    pygame.image.load(image_path61).convert_alpha(),
    pygame.image.load(image_path62).convert_alpha(),
    pygame.image.load(image_path63).convert_alpha(),
    pygame.image.load(image_path64).convert_alpha()
]
image_path65 = 'images/ghost_for_game.png'
ghost = pygame.image.load(image_path65).convert_alpha()
ghost_list1 = []
ghost_list2 = []
bullets1 = []
bullets2 = []
#Игрок
player_x = 633
player_y = 530
dop = 600
anim_character = 0
heart_count = 0
anim_strelka = 0
player_speed = 3
#Методы для игрока
movement = 'right'
is_jump = False
jump_height = 10
image_path68 = 'images/Keyup_game.png'
image_path69 = 'images/Keydown_game.png'
image_path70 = 'images/click_sound.mp3'
image_path71 = 'images/Keyup_game.png'
image_path72 = 'images/keydown_lost_game.png'
image_path73 = 'images/keyup_ingame.png'
image_path74 = 'images/keydown_ingame.png'
image_path75 = 'images/book_keyup.png'
image_path76 = 'images/book_keydown.png'
right_button = Buttonplay(200,350,450,150,'Play',image_path68,image_path69,image_path70)
false_button = Buttonquit(200,550,450,150,'Quit',image_path71,image_path72,image_path70)
false_button_ingame = Buttonquitingame(1250,20,80,80,'Menu',image_path73,image_path74,image_path70)
prompt_button = Promptinglist(1150,15,80,80,'',image_path75,image_path76)
####################################предметы#####################################
image_path66 = 'images/simple_tree.png'
simple_tree = pygame.image.load(image_path66).convert_alpha()
coordinates_tr = [[-1200,335],[-700,335],[950,335]]
coordinates_fr = [[-250,330],[200,330],[1600,330]]
coordinates_stones = [[150,615],[800,615]]
image_path67 = 'images/fruits_tree.png'
fruit_tree = pygame.image.load(image_path67).convert_alpha()
number_value1 = 0
number_value2 = 0
number_value3 = 0
total_number = 0
block_value1 = 0
block_value2 = 0
block_value3 = 0
total_block = 0
stone_number1 = 0
stone_number2 = 0
total_stones = 0
timer1 = pygame.USEREVENT + 1
timer2 = pygame.USEREVENT + 2
timer3 = pygame.USEREVENT + 3
timer4 = pygame.USEREVENT + 4
timer5 = pygame.USEREVENT + 5
timer6 = pygame.USEREVENT + 6
timer7 = pygame.USEREVENT + 7
timer8 = pygame.USEREVENT + 8
health_timer = pygame.USEREVENT + 9
timer_dead = pygame.USEREVENT + 10
ghost_timer1 = pygame.USEREVENT + 12
ghost_timer2 = pygame.USEREVENT + 13
present_timer = pygame.USEREVENT + 14
pygame.time.set_timer(timer1, 65000)
pygame.time.set_timer(timer2, 65000)
pygame.time.set_timer(timer3, 65000)
pygame.time.set_timer(timer4, 65000)
pygame.time.set_timer(timer5, 65000)
pygame.time.set_timer(timer6, 65000)
pygame.time.set_timer(timer7, 65000)
pygame.time.set_timer(timer8, 65000)
pygame.time.set_timer(ghost_timer1, 10000)
pygame.time.set_timer(ghost_timer2, 15000)
pygame.time.set_timer(health_timer,40000)
pygame.time.set_timer(timer_dead,100)
pygame.time.set_timer(present_timer,15000)
cord_m = 0
desk_x = 500
value_bullets = 0
count_box = 0
random_location1 = 0
killors = 0
award_x = 480
#################################################
Gameplay = False
running = True
check_life = True
monument = False
present = False
Gun = False
Craft = True
box1 = False
while running:
    if Gameplay:
        keys = pygame.key.get_pressed()
        screen.blit(background, (background_x, 0))
        screen.blit(background,(background_x + 1366,0))
        screen.blit(background,(background_x - 1366,0))
        screen.blit(desk,(desk_x,545))
        rect_desk = desk.get_rect(center=(desk_x+40,545))
        if not box1:
            random_location1 = random.randint(-1000,1000)


        for coord1 in coordinates_fr:
            screen.blit(fruit_tree,coord1)
            if keys[pygame.K_LEFT] and player_x > 45 and check_life == True:
                coord1[0] += 7
            elif keys[pygame.K_RIGHT] and player_x < 1226 and check_life == True:
                coord1[0] -= 7
        for coord2 in coordinates_tr:
            screen.blit(simple_tree,coord2)
            if keys[pygame.K_LEFT] and player_x > 45 and check_life == True:
                coord2[0] += 7
            elif keys[pygame.K_RIGHT] and player_x < 1226 and check_life == True:
                coord2[0] -= 7
        for coord3 in coordinates_stones:
            screen.blit(stone,coord3)
            if keys[pygame.K_LEFT] and player_x > 45 and check_life == True:
                coord3[0] += 7
            elif keys[pygame.K_RIGHT] and player_x < 1226 and check_life == True:
                coord3[0] -= 7

        if pygame.KEYUP and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and check_life == True:
            if movement == 'left' and check_life == True:
                screen.blit(view_left_quietness, (player_x, player_y))
            elif movement == 'right' and check_life == True:
                screen.blit(view_right_quietness, (player_x, player_y))
        if keys[pygame.K_LEFT] and pygame.KEYDOWN and check_life == True:
            screen.blit(character_view_left[anim_character], (player_x, player_y))
            movement = 'left'
        elif keys[pygame.K_RIGHT] and pygame.KEYDOWN and check_life == True:
            screen.blit(character_view_right[anim_character], (player_x, player_y))
            movement = 'right'
        player_rect = view_left_quietness.get_rect(topleft=(player_x, player_y))
        rect_monument = dead_movement.get_rect(center=(cord_m,dop))
        if ghost_list1:
            for (i, element) in enumerate(ghost_list1):
                screen.blit(ghost, element)
                element.x -= 18
                if player_rect.colliderect(element) and heart_count != 5:
                    heart_count += 1
                    pain_sound.play()
                    ghost_list1.pop(0)
                if element.x < -1250:
                    ghost_list1.pop(i)
        if ghost_list2:
            for (i, element) in enumerate(ghost_list2):
                screen.blit(ghost, element)
                element.x += 18
                if player_rect.colliderect(element) and heart_count != 5:
                    heart_count += 1
                    pain_sound.play()
                    ghost_list2.pop(0)
                if element.x > 1250:
                    ghost_list2.pop(i)




        if bullets1:
            for (i, element) in enumerate(bullets1):
                screen.blit(bullet_right, (element.x, element.y))
                element.x += 15
                if element.x > 1250:
                    bullets1.pop(i)
                if ghost_list1:
                    for (index, ghost_el) in enumerate(ghost_list1):
                        if element.colliderect(ghost_el):
                            ghost_list1.pop(index)
                            bullets1.pop(i)
                            killors += 1





        if bullets2:
            for (i, element) in enumerate(bullets2):
                screen.blit(bullet_left, (element.x, element.y))
                element.x -= 15
                if element.x < -1250:
                    bullets2.pop(i)
                if ghost_list2:
                    for (index, ghost_el) in enumerate(ghost_list2):
                        if element.colliderect(ghost_el):
                            ghost_list2.pop(index)
                            bullets2.pop(i)
                            killors += 1




        if 10 <= killors <= 20:
            screen.blit(award1,(award_x,605))
        elif 20 < killors <= 30:
            screen.blit(award2,(award_x,605))
        elif killors > 30:
            screen.blit(award3,(award_x,605))

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] and pygame.KEYDOWN or pygame.KEYUP:
            screen.blit(berry, (10, 10))
            screen.blit(block,(10,70))
            screen.blit(icon_stone,(10,130))
            screen.blit(icon_bullet_right,(10,210))
            screen.blit(headgg,(1250,680))
            if monument and check_life == True:
                 screen.blit(dead_movement,(cord_m,dop))
            if keys[pygame.K_b] and player_rect.colliderect(rect_monument) and check_life == True and monument == True:
                screen.blit(help_star, (cord_m+8,dop-20))

            if box1:
                screen.blit(present_box, (random_location1, 600))
            box_rect = present_box.get_rect(center=(random_location1, 600))
            if player_rect.colliderect(box_rect) and check_life == True and box1 == True and keys[pygame.K_b]:
                screen.blit(help_star,(random_location1+6,580))
                if keys[pygame.K_d]:
                    box_broken.play()
                    value_bullets += 6
                    box1 = False



        if keys[pygame.K_c] and pygame.KEYDOWN and not keys[pygame.K_b] and not keys[pygame.K_v] and total_block > 0 and check_life == True:
            if keys[pygame.K_LEFT] and pygame.KEYDOWN:
                if anim_character == 0 or anim_character == 2:
                    screen.blit(pine_block, (player_x, player_y +65))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(pine_block, (player_x, player_y + 66))
            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN:
                if anim_character == 0 or anim_character == 2:
                    screen.blit(pine_block, (player_x + 35, player_y + 65))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(pine_block, (player_x + 38, player_y + 66))
            elif pygame.KEYUP and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                if movement == 'left':
                    screen.blit(pine_block, (player_x, player_y + 65))
                elif movement == 'right':
                    screen.blit(pine_block, (player_x + 35, player_y + 66))

        if keys[pygame.K_v] and pygame.KEYDOWN and not keys[pygame.K_b] and not keys[pygame.K_c] and total_number > 0 and check_life == True:
            if keys[pygame.K_LEFT] and pygame.KEYDOWN and check_life == True:
                if anim_character == 0 or anim_character == 2:
                    screen.blit(fruits, (player_x, player_y + 65))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(fruits, (player_x - 2, player_y + 66))
            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN and check_life == True:
                if anim_character == 0 or anim_character == 2:
                    screen.blit(fruits, (player_x + 35, player_y + 65))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(fruits, (player_x + 38, player_y + 66))
            elif pygame.KEYUP and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                if movement == 'left':
                    screen.blit(fruits, (player_x , player_y + 65))
                elif movement == 'right':
                    screen.blit(fruits, (player_x + 35, player_y + 65))

        if keys[pygame.K_v] and keys[pygame.K_d] and pygame.KEYDOWN and 5 > heart_count > 0 and total_number > 0 and check_life == True:
            food_sound.play()
            time.sleep(0.02)
            heart_count -= 1
            total_number -= 1

        if keys[pygame.K_b] and pygame.KEYDOWN and not keys[pygame.K_v] and not keys[pygame.K_c] and not keys[pygame.K_x] and check_life == True:
            if keys[pygame.K_LEFT] and pygame.KEYDOWN:
                if anim_character == 0 or anim_character == 2:
                    screen.blit(axe_left, (player_x - 8, player_y + 60))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(axe_left, (player_x - 11, player_y + 59))
            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN:
                screen.blit(character_view_right[anim_character], (player_x, player_y))
                if anim_character == 0 or anim_character == 2:
                    screen.blit(axe_right, (player_x + 30, player_y + 60))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(axe_right, (player_x + 33, player_y + 59))
            elif pygame.KEYUP and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                if movement == 'left':
                     screen.blit(axe_left, (player_x - 8, player_y + 60))
                elif movement == 'right':
                     screen.blit(axe_right, (player_x + 30, player_y + 60))

        if keys[pygame.K_b] and player_rect.colliderect(rect_desk) and Gun == False:
            if total_block < 6 or total_stones <= 1:
                screen.blit(none_text_help,(540,320))
            elif total_block >= 6 and total_stones >= 2:
                screen.blit(main_text_help,(530,320))
            if anim_character == 0 or anim_character == 1 and block_value2 < 4:
                screen.blit(strelka,(570,400))
            elif anim_character == 2 or anim_character == 3 and block_value2 < 4:
                screen.blit(strelka, (570,370))
            if keys[pygame.K_d] and total_block >= 6 and total_stones >= 2:
                axe_sound.play()
                Gun = True
                total_stones -= 2
                total_block -= 6

        if keys[pygame.K_x] and pygame.KEYDOWN and not keys[pygame.K_v] and not keys[pygame.K_c] and not keys[pygame.K_b] and check_life == True and Gun == True:
            if keys[pygame.K_LEFT] and pygame.KEYDOWN:
                if anim_character == 0 or anim_character == 2:
                    screen.blit(gun_left, (player_x - 8, player_y + 60))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(gun_left, (player_x - 11, player_y + 59))
            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN:
                screen.blit(character_view_right[anim_character], (player_x, player_y))
                if anim_character == 0 or anim_character == 2:
                    screen.blit(gun_right, (player_x + 35, player_y + 60))
                elif anim_character == 1 or anim_character == 3:
                    screen.blit(gun_right, (player_x + 38, player_y + 59))
            elif pygame.KEYUP and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                if movement == 'left':
                     screen.blit(gun_left, (player_x - 8, player_y + 60))
                elif movement == 'right':
                     screen.blit(gun_right, (player_x + 35, player_y + 60))

        if keys[pygame.K_b] and 100<player_x<150 and check_life == True:
            if block_value1 < 3:
                screen.blit(main_text_help, (80,150))
            else:
                screen.blit(end_of_berryes,(80,150))
            if anim_character == 0 or anim_character == 1 and block_value1 < 4:
                screen.blit(strelka,(100,230))
            elif anim_character == 2 or anim_character == 3 and block_value1 < 4:
                screen.blit(strelka, (100,200))
                if keys[pygame.K_d] and block_value1 < 3:
                    berry_sound.play()
                    block_value1 += 1
                    total_block += 1
        if keys[pygame.K_b] and 240<player_x<290 and check_life == True:
            if block_value2 < 3:
                screen.blit(main_text_help, (220,150))
            else:
                screen.blit(end_of_berryes,(220,150))
            if anim_character == 0 or anim_character == 1 and block_value2 < 4:
                screen.blit(strelka,(240,230))
            elif anim_character == 2 or anim_character == 3 and block_value2 < 4:
                screen.blit(strelka, (240,200))
                if keys[pygame.K_d] and block_value2 < 3:
                    berry_sound.play()
                    block_value2 += 1
                    total_block += 1
        if keys[pygame.K_b] and 735<player_x<785 and check_life == True:
            if block_value3 < 3:
                screen.blit(main_text_help, (715,150))
            else:
                screen.blit(end_of_berryes,(715,150))
            if anim_character == 0 or anim_character == 1 and block_value3 < 4:
                screen.blit(strelka,(735,230))
            elif anim_character == 2 or anim_character == 3 and block_value3 < 4:
                screen.blit(strelka, (735,200))
                if keys[pygame.K_d] and block_value3 < 3:
                    berry_sound.play()
                    block_value3 += 1
                    total_block += 1

        if keys[pygame.K_b] and 470<player_x<490 and check_life == True:
            if stone_number1 < 1:
                screen.blit(stone_text_total, (500,560))
            else:
                screen.blit(stone_text_total_end, (500, 560))
            if anim_character == 0 or anim_character == 1 and stone_number1 < 4:
                screen.blit(strelka_stone_below,(520,580))
            elif anim_character == 2 or anim_character == 3 and stone_number1 < 4:
                screen.blit(strelka_stone_below, (520,600))
                if keys[pygame.K_d] and stone_number1 < 1:
                    monument_is_broken.play()
                    stone_number1 += 1
                    total_stones += 1
        if keys[pygame.K_b] and 670<player_x<690 and check_life == True:
            if stone_number2 < 1:
                screen.blit(stone_text_total, (680,560))
            else:
                screen.blit(stone_text_total_end, (680, 560))
            if anim_character == 0 or anim_character == 1 and stone_number2 < 4:
                screen.blit(strelka_stone_below,(700,580))
            elif anim_character == 2 or anim_character == 3 and stone_number2 < 4:
                screen.blit(strelka_stone_below, (700,600))
                if keys[pygame.K_d] and stone_number2 < 1:
                    monument_is_broken.play()
                    stone_number2 += 1
                    total_stones += 1

        if keys[pygame.K_b] and 375<player_x<425 and check_life == True:
            if number_value1 < 3:
                screen.blit(main_text_help, (355,150))
            else:
                screen.blit(end_of_berryes,(355,150))
            if anim_character == 0 or anim_character == 1 and number_value1 < 4:
                screen.blit(strelka,(375,230))
            elif anim_character == 2 or anim_character == 3 and number_value1 < 4:
                screen.blit(strelka, (375,200))
                if keys[pygame.K_d] and number_value1 < 3:
                    berry_sound.play()
                    number_value1 += 1
                    total_number += 1
        elif keys[pygame.K_b] and 510<player_x<560 and check_life == True:
            if number_value2 < 3:
                screen.blit(main_text_help, (500, 150))
            else:
                screen.blit(end_of_berryes,(500,150))
            if anim_character == 0 or anim_character == 1 and number_value2 < 4:
                screen.blit(strelka,(520,230))
            elif anim_character == 2 or anim_character == 3 and number_value2 < 4:
                screen.blit(strelka, (520,200))
                if keys[pygame.K_d] and number_value2 < 3:
                    berry_sound.play()
                    number_value2 += 1
                    total_number += 1
        elif keys[pygame.K_b] and 940<player_x<990 and check_life == True:
            if number_value3 < 3:
                screen.blit(main_text_help, (930, 150))
            else:
                screen.blit(end_of_berryes, (930, 150))
            if anim_character == 0 or anim_character == 1 and number_value3 < 4:
                screen.blit(strelka, (950, 230))
            elif anim_character == 2 or anim_character == 3 and number_value3 < 4:
                screen.blit(strelka, (950, 200))
                if keys[pygame.K_d] and number_value3 < 3:
                    berry_sound.play()
                    number_value3 += 1
                    total_number += 1

        if keys[pygame.K_LEFT] and player_x > 45 and check_life == True:
            player_x -= player_speed
            background_x += 7
            cord_m += 7
            desk_x += 7
            award_x += 7
            random_location1 += 7
        elif keys[pygame.K_RIGHT] and player_x < 1226 and check_life == True:
            player_x += player_speed
            background_x -= 7
            cord_m -= 7
            desk_x -= 7
            award_x -= 7
            random_location1 -= 7



        if not is_jump:
            if keys[pygame.K_SPACE] and check_life == True:
                is_jump = True
        else:
            if jump_height >= -10:
                if jump_height > 0:
                    player_y -= (jump_height ** 2) / 2
                else:
                    player_y += (jump_height ** 2) / 2
                jump_height -= 1
            elif jump_height < -10:
                is_jump = False
                jump_height = 10





        for event in pygame.event.get():
            false_button_ingame.future_event3(event)
            prompt_button.future_event4()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == timer1:
                number_value1 = 0
            if event.type == timer2:
                number_value2 = 0
            if event.type == timer3:
                number_value3 = 0
            if event.type == health_timer:
                heart_count += 1
            if event.type == timer4:
                block_value1 = 0
            if event.type == timer5:
                block_value2 = 0
            if event.type == timer6:
                block_value3 = 0
            if event.type == timer7:
                stone_number1 = 0
            if event.type == timer8:
                stone_number2 = 0
            if event.type == present_timer and box1 == False:
                box1 = True

            if event.type == ghost_timer1:
                ghost_list1.append(ghost.get_rect(topleft=(1250, 545)))
            if event.type == ghost_timer2:
                ghost_list2.append(ghost.get_rect(topleft=(-1250, 545)))
            if Gameplay and event.type == pygame.KEYUP and movement == 'right' and event.key == pygame.K_x  and value_bullets > 0 and Gun == True and check_life == True:
                bullets1.append(bullet_right.get_rect(topleft=(player_x + 30, player_y + 64)))
                shot_sound.play()
                value_bullets -= 1
            elif Gameplay and event.type == pygame.KEYUP and movement == 'left' and event.key == pygame.K_x and value_bullets > 0 and Gun == True and check_life == True:
                bullets2.append(bullet_left.get_rect(topleft=(player_x - 10, player_y + 64)))
                shot_sound.play()
                value_bullets -= 1

            if heart_count == 5 and event.type == timer_dead and pygame.KEYDOWN or heart_count == 5 and event.type == timer_dead and pygame.KEYUP:
                check_life = False
                dead_sound.play()
                total_number = 0
                total_block = 0
                total_stones = 0
                heart_count = 0
                monument = True
                Gun = False
                ghost_list1.clear()
                ghost_list2.clear()
                bullets1.clear()
                bullets2.clear()
                value_bullets = 0
                killors = 0
            else:
                check_life = True
        if not check_life:
            if movement == 'right':
                screen.blit(dead_right, (player_x,dop))
            elif movement == 'left':
                screen.blit(dead_left,(player_x,dop))
            screen.blit(dead_text, (400, 200))
            if -1400<=player_x<=-1000:
                cord_m = -1200
            elif -1000<player_x<=-600:
                cord_m = -800
            elif -600<player_x<=-200:
                cord_m = -400
            elif -200<player_x<=400:
                cord_m = 0
            elif 400<player_x<=800:
                cord_m = 600
            elif 800<player_x<=1400:
                cord_m = 1000

        if keys[pygame.K_b] and keys[pygame.K_d] and player_rect.colliderect(rect_monument) and check_life == True and monument == True:
            monument_is_broken.play()
            total_number += 1
            total_block += 1
            value_bullets += 1
            monument = False

        if anim_character == 3 and check_life == True:
            anim_character = 0
        elif anim_character != 3 and check_life == True:
            anim_character = anim_character + 1
        if anim_strelka == 1 and check_life == True:
            anim_strelka = 0
        elif anim_strelka != 1 and check_life == True:
            anim_strelka += 1

        false_button_ingame.check_image_after3(pygame.mouse.get_pos())
        false_button_ingame.draw3(screen)
        prompt_button.check_image_after4(pygame.mouse.get_pos())
        prompt_button.draw4(screen)
        for image in heart_list:
            screen.blit(heart_list[heart_count], (10, 650))
        berry_text = font_berry.render(str(total_number), True, (230, 164, 50))
        screen.blit(berry_text, (70, 15))
        block_text = font_block.render(str(total_block),True,(166, 98, 15))
        screen.blit(block_text, (70, 80))
        stones_text = font_stones.render(str(total_stones),True,(163, 67, 7))
        screen.blit(stones_text, (70, 140))
        bullet_text = font_bullets.render(str(value_bullets),True,(201, 209, 50))
        screen.blit(bullet_text, (70, 200))
        killors_text = font_killors.render(str(killors), True, (204, 151, 143))
        screen.blit(killors_text, (1300, 680))
    else:
        screen.blit(main_menu,(0,0))
        screen.blit(main_text,(270,150))
        right_button.check_image_after(pygame.mouse.get_pos())
        false_button.check_image_after2(pygame.mouse.get_pos())
        right_button.draw(screen)
        false_button.draw2(screen)
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            right_button.future_event(event)
            false_button.future_event2(event)
    pygame.display.update()
    clock.tick(15)









