import os
from thing import *


def clamp(val, low, high):
    return max(low, min(high, val))


def load_from_path(path, load):
    assets = []
    for dir_name, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            if file_name.endswith(".txt"):
                continue
            o = load(os.path.join(dir_name, file_name))
            if o is not None:
                assets.append(o)
    return assets


def load_sounds_from_folder(folder):
    def load_sound(path):
        return pygame.mixer.Sound(path)
    return load_from_path("sounds/" + folder, load_sound)


def load_things_from_folder(folder):
    def load_thing(path):
        name = path[path.rfind("/") + 1:]
        try:
            assets.images[name] = pygame.image.load(path)
        except pygame.error:
            return None
        return name
    return load_from_path("images/" + folder, load_thing)