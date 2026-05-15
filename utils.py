from ursina import color, invoke, Vec3
from config import KOORDS_ECKEN, KOORDS_KANTEN

def get_id_info(pos):
    """Prüft die Koordinate gegen die Datenbanken in config.py."""
    for id_val, coords in KOORDS_ECKEN.items():
        if pos == coords:
            return str(id_val), color.dark_gray

    for id_val, coords in KOORDS_KANTEN.items():
        if pos == coords:
            return str(id_val), color.light_gray

    return None, None

def release_cubies(cubies, gesamtwuerfel, dreh_achse, state_manager):
    """Fixiert Cubies in der Welt, nachdem die Animation beendet ist."""
    for c in cubies:
        w_pos = c.world_position
        w_rot = c.world_rotation
        c.parent = gesamtwuerfel
        c.position = w_pos
        c.rotation = w_rot

    dreh_achse.rotation = (0, 0, 0)
    state_manager.is_animating = False

def rotate_whole_cube(achse, winkel, gesamtwuerfel, state_manager):
    if state_manager.is_animating:
        return
    state_manager.is_animating = True

    aktuelle_rot = gesamtwuerfel.rotation
    if achse == 'y':
        ziel_rot = aktuelle_rot + Vec3(0, winkel, 0)
    elif achse == 'x':
        ziel_rot = aktuelle_rot + Vec3(winkel, 0, 0)

    gesamtwuerfel.animate_rotation(ziel_rot, duration=0.3)

    def finish():
        state_manager.is_animating = False

    invoke(finish, delay=0.35)




def super_home(cam, gesamtwuerfel, state_manager):
    if state_manager.is_animating:
        return
    state_manager.is_animating = True

    cam.rotation_x = 30
    cam.rotation_y = 45
    cam.distance = 15

    gesamtwuerfel.animate_rotation((0, 0, 0), duration=0.5)

    def finish_reset():
        state_manager.is_animating = False

    invoke(finish_reset, delay=0.55)