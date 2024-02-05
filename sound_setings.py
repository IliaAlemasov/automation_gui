import pyttsx3

'''Is library settings for sound engine pyttsx3 '''

def settings1_sound():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 165)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

def settings2_sound():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)

if __name__ == '__main__':
    print("it library")

