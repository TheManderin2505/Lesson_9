import pgzrun
import random

WIDTH = 800
HEIGHT = 600


START_SPEED = 10
ITEMS = ["bag",'battery',"bottle","chips"]

FINAL_LEVEL = 6
current_level = 1

game_over = False

game_complete = False

items = []
animations = []


def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground",(0,0))
    if game_over:
        deisplay_msg("GAME OVER ", "TRY AGAIN")
    elif game_complete:
        deisplay_msg("GAME COMPLETE ", "WELL DONE")
    else:
        for item in items:
            item.draw()

    



def deisplay_msg(heading,sub_heading):
    screen.draw.text(heading,fontsize = 60, center = (400,300),color = "black")
    screen.draw.text(sub_heading,fontsize = 30, center = (400,330),color = "black")


def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down

def make_items(number_of_extra_items):

    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create


def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        items = Actor(option + "img")
        new_items.append(items)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)

    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        animation = animate(item,duration = duration,on_finished = handle_game_over,y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        items = []
        animations = []

def stop_animations(animation_to_stop):
    for animation in animation_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()
