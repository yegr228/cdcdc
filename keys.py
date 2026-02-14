from pygame import Rect
from effects import draw_key_effect

def draw_keys(screen,key_rects,pressed_keys):
    for i , rect in enumerate(key_rects):
        is_pressed = i in pressed_keys