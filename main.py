from curses import KEY_SPREVIOUS
import keyboard

# Key events stored here
event_counter = []

# For counting how many keys pressed before writing it into the txt document
keysPressed = 0

# After {writeEventsAfter} keys pressed, it'll write everything into a file
writeEventsAfter = 100

# Saves all events into "input_counter.txt"
def saveKeysPressed():
    print("dump")

    dataFile = open("input_counter.txt", "w")
    dataFile.write("\n" + str(keysPressed / 2))
    dataFile.close()

    event_counter.clear()

# Gets called whenever the user clicks any key."
def on_press(event):
    global keysPressed
    keysPressed += 1

    if keysPressed >= writeEventsAfter:
        saveKeysPressed()
        keysPressed = 0


keyboard.hook(on_press)
keyboard.wait()
