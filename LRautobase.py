import time
import pyautogui
import pyttsx3


def loadpause_def():
    time.sleep(loadpause)


engine = pyttsx3.init()


print('сколько фото обрабоать?')
xfoto = int(input())

print('пауза для прогрузки в сек?')

loadpause = float(input())

print('выполние начнется через 10 сек')

time.sleep(10)  # пауза перед стартом

pyautogui.FAILSAFE = True  # аварийное выключение

for i in range(xfoto):
    pyautogui.hotkey('ctrl', 'u')

    loadpause_def()

    pyautogui.press('right')

    loadpause_def()

engine.say("Шеф все готово, не забудь подкинуть в топку новых фото")
print('шеф все готово!')
engine.runAndWait()
