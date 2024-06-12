import pygame
import time

pygame.init()

wn = pygame.display.set_mode((800 ,600))

mode = "normal" # "normal" or "hard"
drop_before_arrive = 0.8
pixel_per_second = 565 / drop_before_arrive

# Object & Images
mayo = pygame.image.load("images\mayo.webp").convert_alpha()
start_menu = pygame.image.load("images\patrick_mayo.jpg").convert_alpha()
start_button = pygame.image.load("images\start_button.png").convert_alpha()
start_menu = pygame.transform.scale(start_menu, (800, 600))
start_button = pygame.transform.scale(start_button, (200, 100))
mayo = pygame.transform.rotate(mayo, 90)
mayo = pygame.transform.scale(mayo, (100, 100))
slot = (125, 30)
white_back = pygame.Rect(0, 0, 800, 600)
border_left_line = pygame.Rect(140, 0, 10, 600)
border_right_line = pygame.Rect(650, 0, 10, 600)
display_pressed1 = pygame.Rect(150, 500, slot[0], slot[1])
display_pressed2 = pygame.Rect(275, 500, slot[0], slot[1])
display_pressed3 = pygame.Rect(400, 500, slot[0], slot[1])
display_pressed4 = pygame.Rect(525, 500, slot[0], slot[1])
music_location = "images\\ver.hard.mp3"
track = pygame.mixer.music.load(music_location)
font = pygame.font.Font("freesansbold.ttf", 32)

# Screen
pygame.display.set_caption("Is Mayonnaise an Instrument?")
pygame.display.set_icon(mayo)


# files
times_arrive = []
times_drop = []
notes = []
note_dict = {64:0, 192:1, 320:2, 448:3}
with open(f"note_and_time\\times_{mode}.txt", "r") as time_f:
    for i in time_f:
        i = int(i)
        i /= 1000
        i = round(i, 4)
        times_arrive.append(i)

with open(f"note_and_time\\notes_{mode}.txt", "r") as note_f:
    for i in note_f:
        i = int(i)
        i = note_dict[i]
        notes.append(i)

for i in times_arrive:
    i -= drop_before_arrive # dropping rate
    i = round(i, 4)
    times_drop.append(i)

# Classes
class Note():
    def __init__(self, drop_time, arrive_time, xcor, ycor, block):
        self.drop_time = drop_time
        self.arrive_time = arrive_time
        self.xcor = xcor
        self.ycor = ycor
        self.block = block
        self.hit = False
        self.show = True
    
    def ycor_update(self, time_pass):
        p = time_pass - self.drop_time # 開始墜落後經過的時間。
        # 上面的時間 * 像素每秒 - (目前位置 + 60) = 要增加的座標 (60 是測試出來的緩衝座標)
        self.ycor += pixel_per_second * p - (self.ycor + 60) 

    def check_remove(self, time_pass):
        block_check = keys[self.block]
        time_check = abs(time_pass - self.arrive_time) <= 0.1
        return block_check and time_check



# Functions
def background_display(mouse_pos):
    global started
    global start_time
    if started:
        draw_back()
    else:
        wn.blit(start_menu, (0, 0))
        wn.blit(start_button, (370, 70))
        if mouse == "down":
            if mouse_pos[0] > 300 and mouse_pos[0] < 500 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
                started = True
                start_time = time.time()


def draw_back():
    pygame.draw.rect(wn, (107, 186, 241), white_back)
    pygame.draw.rect(wn, (255, 255, 0), border_left_line)
    pygame.draw.rect(wn, (255, 255, 0), border_right_line)
    
    pygame.draw.line(wn, (255, 255, 255), (275, 0),(275, 600))
    pygame.draw.line(wn, (255, 255, 255), (400, 0),(400, 600))
    pygame.draw.line(wn, (255, 255, 255), (525, 0),(525, 600))
    
    pygame.draw.line(wn, (100, 100, 100), (150, 500),(650, 500))
    pygame.draw.line(wn, (100, 100, 100), (150, 530),(650, 530))


def draw_press():
    if keys[pygame.K_d]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed1)
    if keys[pygame.K_f]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed2)
    if keys[pygame.K_j]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed3)
    if keys[pygame.K_k]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed4)


def pre_time_handle():
    global loop_start_time
    global start_time
    global time_pass
    loop_start_time = time.time()
    if not started:
        start_time = loop_start_time
    time_pass = float(loop_start_time - start_time)
    time_pass = round(time_pass, 4)


def post_time_handle(loop_start_time):
    now_end_time = time.time()
    now_end_time = round(now_end_time, 4)
    loop_time = now_end_time - loop_start_time
    if loop_time < 0.001:
        time.sleep(0.001 - loop_time)


def note_remove(time_pass):
    for one_note in showing_array:
        if one_note.check_remove(time_pass):
            one_note.hit = True
            one_note.show = False


def showingArray_appending(time_pass):
    global showing_array
    global pointer
    coresponding_location = [160, 285, 410, 535]
    coresponding_key = {0: pygame.K_d, 1: pygame.K_f, 2: pygame.K_j, 3: pygame.K_k}
    while pointer < len(times_drop) and abs(time_pass - times_drop[pointer]) <= 0.1:
        one_note = Note(times_drop[pointer], times_arrive[pointer], coresponding_location[notes[pointer]], -100, coresponding_key[notes[pointer]])
        showing_array.append(one_note)
        pointer += 1
    

def note_displaying(time_pass):
    global showing_array
    for one_note in showing_array:
        if one_note.show:
            one_note.ycor_update(time_pass)
            wn.blit(mayo, (one_note.xcor, one_note.ycor))
        if one_note.ycor >= 900:
            one_note.show = False


def combo_showing():
    # count combo
    combo = 0
    note_died_count = 0
    for one_note in showing_array:
        if one_note.arrive_time < time_pass:
            note_died_count += 1
    for i in range(note_died_count):
        if showing_array[i].hit:
            combo += 1
        else:
            combo = 0
    # show combo
    combo_show = font.render(f"COMBO: {combo}", True, (255, 255, 255))
    wn.blit(combo_show, (10, 10))


def pygame_events():
    global running
    global mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
            print(mouse)
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""


# Global Variables
running = True
mouse = ""
pointer = 0
start_time = 0
started = False
showing_array = []
time_pass = 0
combo = 0
showing_pointer = 0


# Main process
while running:
    # basic info
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    pygame_events() # handle pygame events
    pre_time_handle() # timing process when in the begin of the loop 
    background_display(mouse_pos) # display_backgroud
    draw_press() # draw the key that pressed
    note_remove(time_pass) # remove old notes
    showingArray_appending(time_pass) # add new notes
    note_displaying(time_pass) # display notes  
    combo_showing()
    pygame.display.update()
    post_time_handle(loop_start_time)

    
pygame.quit()