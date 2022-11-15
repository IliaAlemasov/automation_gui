import time
import pyautogui
import pyttsx3

'''RU Этот скрипт поможет сделать атоматическую базовую пакетную цвето коррекцию в Lightroom.
Импортируйте фото для обработки в LR, откройте вкладку Develop, выделите первое фото, 
обязатетельно переключите раскладку клавиатуры на EN. Запустите скрипт, укажите сколько фото
нужно обработать, паузу для загрузки  - зависит от производительности вашего PC. Переключитесь
в окно LR и выделите первое фото'''

'''''EN This script will help you do automatic basic batch color correction in Lightroom.
Import a photo to process in LR, open the Develop tab, select the first photo,
be sure to switch the keyboard layout to EN. Run the script, specify how many photos
need to process, pause to loading - depends on the performance of your PC. switch
into the LR window and select the first photo'''

def loading_pause_def():
    time.sleep(load_pause)


if __name__ == '__main__':
    engine = pyttsx3.init()
    while True:
        try:
            print('сколько фото обрабоать?')
            x_foto = int(input())
            break
        except ValueError:
            print('Введите целое число цифрой без точки')

    while True:
        try:
            print('пауза для прогрузки в сек?')
            load_pause = float(input())
            break
        except ValueError:
            print('Введите число цифрой, можно с точкой.'
                  'например 2.5')
    # Если пауза для прогрузки слишком короткая Lightroom работает неправильно.
    # Сразу решаем эту проблему
    if load_pause >= 1.8:
        pass
    elif load_pause < 1.8:
        load_pause = 2

    print('выполние начнется через 10 сек')

    time.sleep(10)  # пауза перед стартом

    pyautogui.FAILSAFE = True  # аварийное выключение

    for i in range(x_foto):
        pyautogui.hotkey('ctrl', 'u')

        loading_pause_def()

        pyautogui.press('right')

        loading_pause_def()

    engine.say("Шеф все готово, не забудь подкинуть в топку новых фото")
    print('шеф все готово!')
    engine.runAndWait()
