#!/usr/bin/env python3
"""
🐓 Петушок — антизасыпалка мыши
Автор: Продвинутый энтузиаст
Дата: 2026-02-13
"""

import sys
import time
import math
import random
import threading
from typing import Tuple, Optional

import pyautogui
import pyttsx3
from pynput import keyboard

# ============================================================================
# КОНФИГУРАЦИЯ (настраивай под себя)
# ============================================================================

# Диапазон скорости (пиксели в секунду)
SPEED_RANGE = (200, 800)

# Дистанция перемещения за один цикл (пиксели)
DISTANCE_RANGE = (5, 50)

# Пауза между циклами (секунды)
PAUSE_RANGE = (3, 29)

# Возврат в центр, если мышь ближе чем EDGE_MARGIN пикселей к краю экрана
EDGE_MARGIN = 20

# Центр экрана будет вычислен автоматически при запуске

# ============================================================================
# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ СОСТОЯНИЯ
# ============================================================================

# Флаг работы петушка
running = False

# Для блокировки повторного запуска
lock = threading.Lock()

# Экран (будет инициализирован)
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# ============================================================================
# ГОЛОСОВОЙ ДВИЖОК (pyttsx3 в отдельном потоке)
# ============================================================================

def speak(text: str):
    """Произносит текст в отдельном потоке, не блокируя основную программу."""
    def _speak():
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"❌ Ошибка голоса: {e}")

    thread = threading.Thread(target=_speak, daemon=True)
    thread.start()

# ============================================================================
# ФУНКЦИИ ДВИЖЕНИЯ
# ============================================================================

def random_speed() -> float:
    """Случайная скорость в пикселях/сек."""
    return random.uniform(*SPEED_RANGE)

def random_distance() -> int:
    """Случайная дистанция в пикселях."""
    return random.randint(*DISTANCE_RANGE)

def random_angle() -> float:
    """Случайное направление в градусах (0-360)."""
    return random.uniform(0, 360)

def move_mouse(dx: int, dy: int, speed_px_per_sec: float):
    """
    Перемещает мышь на (dx, dy) с заданной скоростью.
    Скорость пересчитывается в duration для pyautogui.moveRel.
    """
    distance = math.hypot(dx, dy)
    if distance == 0:
        return
    # Время = расстояние / скорость
    duration = distance / speed_px_per_sec
    # Ограничиваем минимальную длительность, чтобы движение было видимым
    duration = max(duration, 0.01)
    pyautogui.moveRel(dx, dy, duration=duration, _pause=False)

def is_near_edge(x: int, y: int) -> bool:
    """Проверяет, находится ли мышь близко к краю экрана."""
    return (x <= EDGE_MARGIN or x >= SCREEN_WIDTH - EDGE_MARGIN or
            y <= EDGE_MARGIN or y >= SCREEN_HEIGHT - EDGE_MARGIN)

def return_to_center():
    """Плавно возвращает мышь в центр экрана."""
    cx, cy = pyautogui.position()
    dx = CENTER_X - cx
    dy = CENTER_Y - cy
    if dx != 0 or dy != 0:
        # Используем среднюю скорость для возврата
        move_mouse(dx, dy, sum(SPEED_RANGE) / 2)
        print(f"🎯 Возврат в центр экрана")

# ============================================================================
# ЦИКЛ ДВИЖЕНИЯ (ВЫПОЛНЯЕТСЯ В ОТДЕЛЬНОМ ПОТОКЕ)
# ============================================================================

def movement_loop():
    """Основной цикл: движение с рандомными параметрами."""
    global running

    print("🐓 Петушок начал работу!")
    speak("петушок работает")

    while running:
        try:
            # 1. Рандомные параметры
            dist = random_distance()
            angle = random_angle()
            speed = random_speed()
            pause = random.uniform(*PAUSE_RANGE)

            # 2. Вычисляем смещение
            rad = math.radians(angle)
            dx = int(dist * math.cos(rad))
            dy = int(dist * math.sin(rad))

            # 3. Плавно двигаем мышь
            move_mouse(dx, dy, speed)
            print(f"➡️  Движение: dx={dx}, dy={dy}, speed={speed:.0f} px/сек, пауза={pause:.1f}с")

            # 4. Проверка границ
            x, y = pyautogui.position()
            if is_near_edge(x, y):
                print("⚠️  Мышь у края экрана")
                return_to_center()

            # 5. Пауза между циклами
            time.sleep(pause)

        except KeyboardInterrupt:
            # Этот блок не сработает в потоке, но оставим для аккуратности
            break
        except Exception as e:
            print(f"❌ Ошибка в цикле движения: {e}")
            time.sleep(1)

    print("🐓 Петушок остановлен")
    speak("петушок отдыхает")

# ============================================================================
# УПРАВЛЕНИЕ ПОТОКОМ ДВИЖЕНИЯ
# ============================================================================

def start_chicken():
    """Запускает петушка в отдельном потоке."""
    global running
    with lock:
        if running:
            print("⚠️  Петушок уже работает")
            return
        running = True
        thread = threading.Thread(target=movement_loop, daemon=True)
        thread.start()

def stop_chicken():
    """Останавливает петушка."""
    global running
    with lock:
        running = False
    # Сообщение об остановке выведет сам поток

# ============================================================================
# ГЛОБАЛЬНЫЕ ХОТКЕИ (PYNPUT)
# ============================================================================

def on_press(key):
    """Обработчик нажатий клавиш."""
    try:
        # Правый Ctrl + 9 → старт
        if key == keyboard.Key.ctrl_r:
            # Запоминаем, что правый Ctrl зажат
            return
        if hasattr(key, 'char') and key.char == '9':
            # Проверяем, зажат ли правый Ctrl
            if keyboard.Controller().ctrl_r:
                start_chicken()
                return False  # Не блокируем событие

        # Правый Ctrl + 0 → стоп
        if hasattr(key, 'char') and key.char == '0':
            if keyboard.Controller().ctrl_r:
                stop_chicken()
                return False

        # Левый Ctrl + C — аварийный выход (глобально)
        if key == keyboard.Key.ctrl_l or (hasattr(key, 'char') and key.char in ('c', 'C')):
            # Здесь сложно, проще вынести в отдельный listener на Ctrl+C
            pass

    except AttributeError:
        pass

def on_release(key):
    """Обработчик отпускания клавиш."""
    pass

def global_ctrl_c_listener():
    """Слушатель для глобального Ctrl+C (даже при свёрнутом окне)."""
    with keyboard.Listener(on_press=lambda k: sys.exit(0) if k == keyboard.Key.ctrl_l or
                          (hasattr(k, 'char') and k.char == '\x03') else None) as listener:
        listener.join()

# ============================================================================
# ТОЧКА ВХОДА
# ============================================================================

def main():
    print("=" * 60)
    print("🐓 ПЕТУШОК — антизасыпалка мыши")
    print("=" * 60)
    print(f"🖥️  Экран: {SCREEN_WIDTH}x{SCREEN_HEIGHT}, центр: {CENTER_X},{CENTER_Y}")
    print("\n🎮 Глобальные хоткеи:")
    print("   ▶️  Правый Ctrl + 9 — запустить петушка")
    print("   ⏹️  Правый Ctrl + 0 — остановить петушка")
    print("   💀 Левый Ctrl + C  — аварийный выход (глобально)")
    print("\n🔄 Скрипт работает в фоне. Сворачивай окно — хоткеи всё равно сработают.")
    print("=" * 60)

    # Запускаем слушатель глобальных хоткеев
    # Для правого Ctrl+9/0 нужен свой listener с проверкой модификатора
    def on_press_global(key):
        try:
            # Проверка: правый Ctrl зажат?
            # pynput не даёт простого способа узнать состояние модификатора в колбэке.
            # Поэтому будем использовать костыль: отслеживать нажатие/отпускание Ctrl_r.
            # Для этого заведём глобальную переменную.
            global right_ctrl_pressed
            if key == keyboard.Key.ctrl_r:
                right_ctrl_pressed = True
            elif key == keyboard.Key.ctrl_r and hasattr(key, '_phys'):  # отпускание
                right_ctrl_pressed = False

            if hasattr(key, 'char') and key.char == '9' and right_ctrl_pressed:
                start_chicken()
            elif hasattr(key, 'char') and key.char == '0' and right_ctrl_pressed:
                stop_chicken()
            elif key == keyboard.Key.ctrl_l or (hasattr(key, 'char') and key.char == '\x03'):
                print("\n💀 Аварийное завершение по Ctrl+C")
                speak("петушок умер")
                sys.exit(0)

        except Exception as e:
            print(f"Ошибка в обработчике клавиш: {e}")

    right_ctrl_pressed = False

    # Запускаем глобальный слушатель в фоновом потоке
    listener = keyboard.Listener(on_press=on_press_global, on_release=on_release_global)
    listener.daemon = True
    listener.start()

    # Держим главный поток живым, чтобы скрипт не завершился
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Выход по Ctrl+C в консоли")
        speak("петушок отдыхает")
        sys.exit(0)

def on_release_global(key):
    global right_ctrl_pressed
    if key == keyboard.Key.ctrl_r:
        right_ctrl_pressed = False

if __name__ == "__main__":
    # Убираем паузы PyAutoGUI после неудач
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

    # Переопределяем функцию speak для отладки, если нет голоса
    try:
        # Проверяем, работает ли pyttsx3
        engine = pyttsx3.init()
        engine.stop()
    except Exception:
        # Если не работает — заглушка
        def speak(text):
            print(f"[Голос]: {text}")

    main()