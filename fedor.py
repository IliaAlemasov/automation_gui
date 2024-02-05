from sound_setings import *
import pyttsx3 as pt

fedor = pt.init()
settings1_sound()
fedor.say('Привет мой друг! Как твои дела?')
print('Привет мой друг!Как твои дела?')
fedor.runAndWait()
x = input(str())
if x == 'плохо':
    fedor.say('Всё обязательно наладится!')
elif x == "хорошо":
    fedor.say('Очень рад слышать!')
else:
    fedor.say('Ничего и такое бывает')
fedor.runAndWait()



fedor.runAndWait()