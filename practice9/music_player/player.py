import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 300))

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 200, 0)
DARK = (30, 30, 30)

MUSIC_FOLDER = "music"

playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith((".mp3", ".wav"))]

if not playlist:
    print("No music files found!")
    pygame.quit()

current_index = 0
is_playing = True
is_paused = False
current_length = 0  # ✅ FIX 1: Declared as a global variable with a safe default

clock = pygame.time.Clock()


def load_track(index):
    global current_index, current_length  # ✅ FIX 2: Declared as global so the assignment persists

    track_path = os.path.join(MUSIC_FOLDER, playlist[index])
    pygame.mixer.music.load(track_path)

    sound = pygame.mixer.Sound(track_path)
    current_length = sound.get_length()  # ✅ Now this actually updates the global


def play():
    global is_playing, is_paused

    if not is_playing:
        pygame.mixer.music.play()
        is_playing = True
        is_paused = False
    elif is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.pause()
        is_paused = True


def stop():
    global is_playing, is_paused
    pygame.mixer.music.stop()
    is_playing = False
    is_paused = False


def next_track():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    load_track(current_index)
    pygame.mixer.music.play()


def prev_track():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    load_track(current_index)
    pygame.mixer.music.play()


def draw_text(text, x, y, font_obj):
    label = font_obj.render(text, True, WHITE)
    screen.blit(label, (x, y))


def draw_progress_bar():
    if not is_playing:
        progress = 0
    else:
        current_time = pygame.mixer.music.get_pos() / 1000
        progress = current_time / current_length if current_length > 0 else 0

    bar_width = 400
    filled = int(bar_width * progress)

    pygame.draw.rect(screen, GRAY, (100, 200, bar_width, 20))
    pygame.draw.rect(screen, GREEN, (100, 200, filled, 20))


def draw_ui():
    screen.fill(DARK)

    draw_text("Now Playing:", 100, 50, font)
    draw_text(playlist[current_index], 100, 90, font)

    controls = "P:Play/Pause  S:Stop  N:Next  B:Back  Q:Quit"
    draw_text(controls, 30, 255, small_font)

    draw_progress_bar()


load_track(current_index)
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    draw_ui()
    pygame.display.flip()
    clock.tick(60)