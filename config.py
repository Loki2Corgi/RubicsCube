from ursina import color

KOORDS_ECKEN = {
                0: (1, 1, 1),    1: (-1, 1, 1),    2: (-1, 1, -1),    3: (1, 1, -1),
                4: (1, -1, 1),   5: (-1, -1, 1),   6: (-1, -1, -1),   7: (1, -1, -1)
}

KOORDS_KANTEN = {
                  0: (0, 1, 1),    1: (-1, 1, 0),    2: (0, 1, -1),    3: (1, 1, 0),
                  4: (1, 0, -1),   5: (-1, 0, -1),   6: (-1, 0, 1),    7: (1, 0, 1),
                  8: (0, -1, 1),   9: (-1, -1, 0),   10: (0, -1, -1),  11: (1, -1, 0)
}


FARBEN = {
    'oben':    color.yellow, 'unten':   color.white,
    'rechts':  color.red,    'links':   color.orange,
    'vorne':   color.blue,   'hinten':  color.green
}

LABEL_STYLE = {
    'scale': 12,
    'bold_start': '<bold>',
    'bold_end': '</bold>',
    'font': 'tahoma.ttf', # Falls vorhanden
    'color_offset': 0.05,   # Abstand zur Fläche
    'outline_thickness': 1,  # Dicke der Umrandung
    'font': 'Arial.ttf'
}

SEITEN_DATEN = [
    {'achse': 0, 'wert':  1, 'col': FARBEN['rechts'], 'scale': (0.05, 0.8, 0.8), 'rot': (0, -90, 0)},
    {'achse': 0, 'wert': -1, 'col': FARBEN['links'],  'scale': (0.05, 0.8, 0.8), 'rot': (0, 90, 0)},
    {'achse': 1, 'wert':  1, 'col': FARBEN['oben'],   'scale': (0.8, 0.05, 0.8), 'rot': (90, 0, 0)},
    {'achse': 1, 'wert': -1, 'col': FARBEN['unten'],  'scale': (0.8, 0.05, 0.8), 'rot': (-90, 0, 0)},
    {'achse': 2, 'wert':  1, 'col': FARBEN['vorne'],  'scale': (0.8, 0.8, 0.05), 'rot': (0, 180, 0)},
    {'achse': 2, 'wert': -1, 'col': FARBEN['hinten'], 'scale': (0.8, 0.8, 0.05), 'rot': (0, 0, 0)},
]