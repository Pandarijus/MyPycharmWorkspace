import pynput.keyboard
from pynput.keyboard import Listener,Key
import os




def refreshDisplay():
    for i in range(12):
        pass
        #print()

    for i in range(len(best)):
        l = best[i].strip()  # ! remove \n
        #print(l)




def reflexDisplay():
    global best
    best = lines
    refreshDisplay()


#make it so its get key down not when you hold

kb = pynput.keyboard.Controller()
textName = "myKeyLog.txt"
user =os.path.expanduser("~")
path = user+"\\3D Objects\\"+textName
textName = path

text = ""
file = open(textName,"a")

lines = file.readlines()
best = []

reflexDisplay()

index = 0


def refineDisplayFromWordList(txt =""):
    global best
    best = []
    for d in lines:
        if d.startswith(txt):
            best.append(d)

    refreshDisplay()

def getMostLikely():
    if len(best) != 0:
        return best[0]

def clamp(z,mini,maxi):
    return min(maxi,max(mini,z))


def yep(keyCode):#gets called every time a key on the keyboard is pressed
    #"Key.ctrl_l"  "Key.tab"

    global text,index#import the text variable
    key = str(keyCode)
    if "'" in key:
        key = keyCode.char
    #print(key)
    if key == "Key.enter" or key == "Key.space":
        print(text)
        file.write(text)
        text = ""
        index = 0
        refineDisplayFromWordList(text)
        #reflexDisplay()
    elif key == "Key.backspace":
        text = text[:-1]
        refineDisplayFromWordList(text)
    elif key == "Key.esc":
        #print("Quit")
        file.write(text)
        file.close()
        quit()
    elif key == "`":
        mostWord = getMostLikely()
        if mostWord:
            kb.press(Key.backspace)
            kb.press(Key.backspace)
            kb.type(mostWord)

    elif key == "Key.left":
        index = index + 1
    elif key == "Key.right":
        if index > 0:
            index = index -1

    elif key == "Key.up": #stop writing word here. new show
        pass
    elif key == "Key.up":
        pass



    elif "Key." in key:#special key pressed
        #print("Special Key:" + key)
        pass
    else:


        if index == 0:
            text = text + key
        else:
            lenx = len(text)
            index = clamp(index,0,lenx)
            texLis = list(text)
            texLis.insert(lenx - index, key)
            text = "".join(texLis)

            print(text,index)
        #
        print(""+key)

        refineDisplayFromWordList(text)




with Listener(yep) as lis:#Listener for key inputs
    lis.join()
