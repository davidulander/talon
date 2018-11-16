from talon.voice import Context, Key, Str, press
from talon import clip, tap
from talon import cron
import time

context = Context('test')
delay = '1000ms'

def correct_text():

    # inputText=" this is a test paragraph.It has various errors,in its capitalisation and spacing  . this script will attempt  to fix these errors.  the aim is to use it with Dragon in applications where it can't auto space or auto capitalise."

    cron.after(delay,press('cmd-c'))
    time.sleep(0.1)
    inputText=clip.get()
    print(inputText)

    correctText=''
    uppern=True # whether to capitalise the next character
    spacen=False # whether to allow the next character to be a space
    spacenf=False #Whether to force a space before the next character if one doesn't exist
    charp=''
    for index,char in enumerate(inputText):
        charNew=''
        upper=uppern
        space=spacen
        if (char != ' ') and spacenf and (charp=='.'):
            charNew+=' '
        spacenf=False

        if char== '.' or char==',':
            while correctText[-1]==' ':
                correctText=correctText[:-1]
            spacen=True
            uppern=True
            spacenf=True
            charNew+=char
        elif char==' ':
            if spacen:
                charNew+=char
                spacen=False
            else:
                charNew=''
        elif upper:
            charNew+=char.upper()
            uppern=False
            spacen=True
        else:
            charNew+=char
            spacen=True

        correctText+=charNew
        charp=charNew

    clip.set(correctText)
    time.sleep(0.1)
    cron.after(delay,press('cmd-v'))

def correct_text2(index):

    correct_text()

keymap = {
    'correct text': correct_text2,
}

context.keymap(keymap)
