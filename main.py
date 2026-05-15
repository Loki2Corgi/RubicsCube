from ursina import *
from config import KOORDS_ECKEN, KOORDS_KANTEN, FARBEN, LABEL_STYLE, SEITEN_DATEN
from utils import get_id_info, rotate_whole_cube, super_home

# --- INITIALISIERUNG & DATENBANKEN ---
app = Ursina(title="Zauberwürfel Simulation")

# Status-Variablen für Animationen
class CubeState:
    is_animating = False

cube_state = CubeState()
gesamt_drehung_y = 0
gesamt_neigung_x = 0

# --- 2. KAMERA SETUP ---
cam = EditorCamera()
cam.rotation_x = 30
cam.rotation_y = 45
cam.distance = 0.5

# --- KOORDINATENKREUZ ---
achsensystem = Entity(position=(-4, -2, -4))
Entity(parent=achsensystem, model='cube', color=color.red, scale=(1.5, 0.05, 0.05), position=(0.75, 0, 0))
Text(parent=achsensystem, text='+X', position=(1.6, 0, 0), color=color.red, scale=8, billboard=True)
Entity(parent=achsensystem, model='cube', color=color.green, scale=(0.05, 1.5, 0.05), position=(0, 0.75, 0))
Text(parent=achsensystem, text='+Y', position=(0, 1.6, 0), color=color.green, scale=8, billboard=True)
Entity(parent=achsensystem, model='cube', color=color.blue, scale=(0.05, 0.05, 1.5), position=(0, 0, 0.75))
Text(parent=achsensystem, text='+Z', position=(0, 0, 1.6), color=color.blue, scale=8, billboard=True)

# --- WÜRFEL AUFBAU ---
gesamtwuerfel = Entity()
dreh_achse = Entity()
cubies = []

for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            pos = (x, y, z)
            label_text, label_color = get_id_info(pos)
            kern = Entity(parent=gesamtwuerfel, model='cube', color=color.black, position=pos, scale=0.98)
            cubies.append(kern)

            for s in SEITEN_DATEN:
                if pos[s['achse']] == s['wert']:
                    f_pos = [0, 0, 0]
                    f_pos[s['achse']] = s['wert'] * 0.5
                    Entity(parent=kern, model='cube', color=s['col'], position=f_pos,scale=s['scale'])

                    if label_text:
                        t_pos = [0, 0, 0]
                        t_pos[s['achse']] = s['wert'] * (0.5 + LABEL_STYLE['color_offset'])
                        Text(parent=kern, text=f"{LABEL_STYLE['bold_start']}{label_text}{LABEL_STYLE['bold_end']}", position=t_pos, rotation=s['rot'], scale=LABEL_STYLE['scale'], color=label_color, origin=(0, 0))

Button(text='L', color=color.orange, scale=(0.05, 0.05), position=(-0.75, 0.35), on_click=Func(rotate_whole_cube, 'y', -90, gesamtwuerfel, cube_state))
Button(text='R', color=color.orange, scale=(0.05, 0.05), position=(-0.85, 0.35), on_click=Func(rotate_whole_cube, 'y', 90, gesamtwuerfel, cube_state))
Button(text='U', color=color.orange, scale=(0.05, 0.05), position=(-0.8, 0.4), on_click=Func(rotate_whole_cube, 'x', -90, gesamtwuerfel, cube_state))
Button(text='D', color=color.orange, scale=(0.05, 0.05), position=(-0.8, 0.3), on_click=Func(rotate_whole_cube, 'x', 90, gesamtwuerfel, cube_state))
Button(text='H', color=color.red, scale=(0.05, 0.05), position=(-0.8, 0.35), on_click=Func(super_home, cam, gesamtwuerfel, cube_state))

app.run()