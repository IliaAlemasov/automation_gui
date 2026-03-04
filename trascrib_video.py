import sys
import subprocess
import os
import re
from pathlib import Path
from typing import Optional, List
import time
import numpy as np


def clean_input_string(input_str: str) -> str:
    """
    Очищает строку от невидимых символов, которые добавляет Windows при копировании.
    Удаляет U+202A (LEFT-TO-RIGHT EMBEDDING) и другие управляющие символы.
    """
    # Удаляем все непечатаемые символы кроме пробелов, табуляции и перевода строки
    cleaned = re.sub(r'[\u2000-\u200F\u202A-\u202E\u200B-\u200D\uFEFF]', '', input_str)

    # Также удаляем другие возможные невидимые символы
    cleaned = ''.join(char for char in cleaned if char.isprintable() or char in ' \t\n')

    # Убираем кавычки и лишние пробелы
    cleaned = cleaned.strip().strip('"').strip("'")

    return cleaned


def find_ffmpeg() -> Optional[Path]:
    """Ищем ffmpeg в стандартных местах Windows"""
    common_paths = [
        Path("C:/Program Files/ffmpeg/bin/ffmpeg.exe"),
        Path("C:/Program Files (x86)/ffmpeg/bin/ffmpeg.exe"),
        Path("C:/ffmpeg/bin/ffmpeg.exe"),
        "ffmpeg",
        Path(os.getenv("USERPROFILE", "")) / "ffmpeg/bin/ffmpeg.exe",
        Path("ffmpeg.exe"),
    ]

    for path in common_paths:
        try:
            if isinstance(path, str):
                result = subprocess.run(
                    ["where", path] if os.name == "nt" else ["which", path],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    return Path(result.stdout.strip().split('\n')[0])
            elif path.exists():
                return path
        except:
            continue

    return None


def get_video_formats() -> List[str]:
    """Поддерживаемые видеоформаты (требуют конвертации в MP3)"""
    return ['.mp4', '.webm', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.m4v']


def get_audio_formats() -> List[str]:
    """Поддерживаемые аудиоформаты (можно транскрибировать напрямую)"""
    return ['.mp3', '.ogg', '.wav', '.m4a', '.flac']  # добавил ещё для удобства


def is_video_file(file_path: Path) -> bool:
    """Проверяет, является ли файл видео (требует конвертации)"""
    return file_path.suffix.lower() in get_video_formats()


def is_audio_file(file_path: Path) -> bool:
    """Проверяет, является ли файл аудио (можно сразу транскрибировать)"""
    return file_path.suffix.lower() in get_audio_formats()


def convert_video_to_mp3(video_path: Path) -> Optional[Path]:
    """Конвертирует видеофайл в MP3 через ffmpeg"""
    ffmpeg_path = find_ffmpeg()

    if not ffmpeg_path:
        print("\n❌ FFmpeg не найден!")
        print("\n📥 Установите FFmpeg в C:\\ffmpeg\\")
        print("   Или добавьте в переменную PATH")
        return None

    try:
        # Создаем путь для MP3 файла (заменяем расширение на .mp3)
        audio_path = video_path.with_suffix('.mp3')

        print(f"\n🎬 Конвертация видео в MP3:")
        print(f"   Исходный файл: {video_path.name} ({video_path.suffix})")
        print(f"   Целевой файл: {audio_path.name}")
        print(f"   Размер исходного: {video_path.stat().st_size / (1024 * 1024):.1f} MB")

        audio_path_abs = audio_path.absolute()
        video_path_abs = video_path.absolute()

        # Удаляем старый MP3 файл если существует
        if audio_path_abs.exists():
            print(f"   ⚠️  Удаляем старый MP3 файл...")
            try:
                audio_path_abs.unlink()
            except Exception as e:
                print(f"   ⚠️  Не удалось удалить старый файл: {e}")

        # Команда ffmpeg для конвертации видео в MP3
        cmd = [
            str(ffmpeg_path),
            '-i', str(video_path_abs),
            '-q:a', '2',
            '-map', 'a',  # Берем только аудиодорожку
            '-y',  # Перезаписываем без подтверждения
            '-loglevel', 'error',
            str(audio_path_abs)
        ]

        print(f"   ⚙️  Запуск FFmpeg...")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )

        if result.returncode == 0:
            time.sleep(0.5)  # Даем время на запись файла

            if audio_path_abs.exists():
                size_mb = audio_path_abs.stat().st_size / (1024 * 1024)
                print(f"\n✅ Аудиофайл успешно создан!")
                print(f"   Размер: {size_mb:.1f} MB")
                print(f"   Путь: {audio_path_abs}")
                return audio_path_abs
            else:
                print(f"\n❌ Аудиофайл не был создан!")
                print(f"   Проверьте права доступа к папке: {audio_path_abs.parent}")
                return None
        else:
            print(f"\n❌ Ошибка FFmpeg при конвертации:")
            print(f"   {result.stderr[:500]}")

            # Пробуем альтернативную команду для сложных случаев
            print(f"   🔄 Пробуем альтернативный метод конвертации...")
            return convert_video_to_mp3_fallback(video_path, ffmpeg_path)

    except Exception as e:
        print(f"\n❌ Ошибка конвертации: {e}")
        import traceback
        traceback.print_exc()
        return None


def convert_video_to_mp3_fallback(video_path: Path, ffmpeg_path: Path) -> Optional[Path]:
    """Альтернативный метод конвертации видео в MP3"""
    try:
        audio_path = video_path.with_suffix('.mp3')
        audio_path_abs = audio_path.absolute()

        # Альтернативная команда - более универсальная
        cmd = [
            str(ffmpeg_path),
            '-i', str(video_path.absolute()),
            '-vn',  # Без видео
            '-acodec', 'libmp3lame',
            '-ab', '192k',  # Битрейт 192 kbps
            '-ar', '44100',  # Частота дискретизации
            '-ac', '2',  # Стерео
            '-y',
            '-loglevel', 'error',
            str(audio_path_abs)
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )

        if result.returncode == 0 and audio_path_abs.exists():
            size_mb = audio_path_abs.stat().st_size / (1024 * 1024)
            print(f"   ✅ Альтернативный метод сработал!")
            print(f"   Размер: {size_mb:.1f} MB")
            return audio_path_abs
        else:
            print(f"   ❌ Альтернативный метод тоже не сработал")
            return None

    except Exception as e:
        print(f"   ❌ Ошибка в альтернативном методе: {e}")
        return None


def clean_path(path_str: str) -> Path:
    """Очистка пути от кавычек и нормализация слешей"""
    # Сначала очищаем от невидимых символов
    path_str = clean_input_string(path_str)

    # Заменяем обратные слеши на прямые
    path_str = path_str.replace('\\', '/')

    # Создаем Path объект
    path_obj = Path(path_str)

    # Если это не абсолютный путь, делаем его абсолютным
    if not path_obj.is_absolute():
        path_obj = path_obj.absolute()

    return path_obj


def print_progress(step: int, total: int, message: str):
    """Простой текстовый прогресс-бар"""
    progress = "█" * step + "░" * (total - step)
    print(f"\r[{progress}] {message}", end="", flush=True)
    if step == total:
        print()


def transcribe_audio(audio_path: Path, ffmpeg_path: Path) -> Optional[str]:
    """Транскрибирует аудио через Whisper"""
    try:
        print_progress(2, 4, "Загрузка модели Whisper...")

        if not audio_path.exists():
            print(f"\n❌ Аудиофайл не найден: {audio_path}")
            return None

        print(f"\n   Аудиофайл: {audio_path.name}")
        print(f"   Размер: {audio_path.stat().st_size / (1024 * 1024):.1f} MB")

        # Импортируем whisper
        try:
            import whisper
        except ImportError:
            print("\n   Устанавливаем whisper...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "openai-whisper==20231117"])
            import whisper

        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"\n   Устройство: {device.upper()}")

        model = whisper.load_model("base", device=device)

        print_progress(3, 4, f"Транскрибация {audio_path.name}...")

        # Ключевое исправление: передаем путь к ffmpeg в whisper
        # Устанавливаем переменную окружения для whisper
        ffmpeg_dir = str(ffmpeg_path.parent)
        os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")

        print(f"\n   FFmpeg для whisper: {ffmpeg_path}")
        print(f"   PATH обновлен")

        # Анимация
        start_time = time.time()

        # Транскрибируем
        result = model.transcribe(
            str(audio_path.absolute()),
            language="ru",
            task="transcribe",
            fp16=False
        )

        elapsed = time.time() - start_time
        print(f"\r   [✓] Транскрибация завершена за {elapsed:.1f} сек!")
        return result["text"]

    except Exception as e:
        print(f"\n❌ Ошибка транскрибации: {e}")
        import traceback
        traceback.print_exc()

        # Попробуем альтернативный метод с librosa
        print("\n🔄 Пробуем альтернативный метод загрузки...")
        try:
            return transcribe_audio_fallback(audio_path, ffmpeg_path)
        except Exception as e2:
            print(f"❌ Альтернативный метод тоже не удался: {e2}")
            return None


def transcribe_audio_fallback(audio_path: Path, ffmpeg_path: Path) -> Optional[str]:
    """Альтернативный метод транскрибации через librosa"""
    try:
        print("   Используем librosa для загрузки аудио...")

        import whisper
        import torch
        import librosa

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = whisper.load_model("base", device=device)

        # Загружаем аудио через librosa
        audio, sr = librosa.load(str(audio_path.absolute()), sr=16000, mono=True)

        print(f"   Аудио загружено: {len(audio) / sr:.1f} сек")

        # Транскрибируем
        result = model.transcribe(
            audio,
            language="ru",
            task="transcribe",
            fp16=False
        )

        return result["text"]
    except ImportError:
        print("   Устанавливаем librosa...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "librosa"])
        return transcribe_audio_fallback(audio_path, ffmpeg_path)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e


def save_text(text: str, audio_path: Path):
    """Сохраняет текст в файл"""
    try:
        txt_path = audio_path.with_suffix('.txt')
        txt_path_abs = txt_path.absolute()
        txt_path_abs.write_text(text, encoding='utf-8')
        print_progress(4, 4, f"Сохранение текста в {txt_path.name}...")
        return True
    except Exception as e:
        print(f"\n❌ Ошибка сохранения: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=" * 60)
    print("🎬 Видео/Аудио → Текст конвертер")
    print("=" * 60)

    video_formats = get_video_formats()
    audio_formats = get_audio_formats()
    print(f"📹 Видеоформаты (конвертация в MP3): {', '.join(video_formats)}")
    print(f"🎵 Аудиоформаты (прямая транскрибация): {', '.join(audio_formats)}")

    # Находим ffmpeg сразу
    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        print("\n❌ FFmpeg не найден!")
        print("\n📥 Установите FFmpeg:")
        print("   1. Скачайте с https://github.com/BtbN/FFmpeg-Builds/releases")
        print("   2. Распакуйте в C:\\ffmpeg")
        print("   3. Добавьте C:\\ffmpeg\\bin в PATH")
        print("   4. Перезапустите PyCharm")
        return

    print(f"✅ FFmpeg найден: {ffmpeg_path}")

    # Получаем входную строку
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])  # Объединяем все аргументы
    else:
        print("\n📋 Вставьте путь к видео или аудиофайлу:")
        print("   Можно перетащить файл прямо в это окно")
        print("\nПуть: ", end="")
        input_str = input().strip()

    # Диагностика ввода
    print(f"\n🔍 Диагностика ввода:")
    print(f"   Исходная строка (сырая): {repr(input_str)}")
    print(f"   Длина: {len(input_str)} символов")

    try:
        file_path = clean_path(input_str)
        print(f"✅ Обработанный путь: {file_path}")
    except Exception as e:
        print(f"\n❌ Ошибка обработки пути: {e}")
        import traceback
        traceback.print_exc()
        return

    # Проверка существования файла
    if not file_path.exists():
        print(f"\n❌ Файл не найден: {file_path}")
        print(f"   Проверьте существование файла")
        print(f"   Рабочая директория: {Path.cwd()}")
        return

    ext = file_path.suffix.lower()

    # Определяем, что делать с файлом
    if is_video_file(file_path):
        print(f"\n🎬 Обнаружен видеофайл: {file_path.name}")
        # Шаг 1: конвертация видео в MP3
        print_progress(1, 4, "Конвертация видео в MP3...")
        audio_path = convert_video_to_mp3(file_path)
        if not audio_path:
            print("\n❌ КОНВЕРТАЦИЯ НЕ УДАЛАСЬ")
            return

    elif is_audio_file(file_path):
        print(f"\n🎵 Обнаружен аудиофайл: {file_path.name}")
        print("   Конвертация не требуется, используем исходный файл.")
        audio_path = file_path
        # Прогресс: шаг 1 пропускаем, но показываем сообщение
        # Просто выведем обычный print, чтобы не ломать прогресс-бар
        print("[█░░░] Аудиофайл готов (конвертация не требуется)")

    else:
        print(f"\n❌ Неподдерживаемый формат файла: {ext}")
        print(f"   Поддерживаемые форматы:")
        print(f"   Видео: {', '.join(video_formats)}")
        print(f"   Аудио: {', '.join(audio_formats)}")
        return

    print(f"\n📂 Файл: {file_path.name}")
    print(f"📁 Папка: {file_path.parent}")
    print(f"📊 Размер: {file_path.stat().st_size / (1024 * 1024):.1f} MB")
    print("-" * 60)

    try:
        # 2. Транскрибация
        text = transcribe_audio(audio_path, ffmpeg_path)
        if not text:
            print("\n❌ ТРАНСКРИБАЦИЯ НЕ УДАЛАСЬ")

            # Устанавливаем librosa для fallback
            print("\n📦 Устанавливаем librosa для альтернативной загрузки...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "librosa"])
            text = transcribe_audio_fallback(audio_path, ffmpeg_path)

            if not text:
                return

        # 3. Сохранение
        if save_text(text, audio_path):
            print("\n" + "=" * 60)
            print("✅ ВСЁ ГОТОВО!")
            print("=" * 60)

            # Показываем первые 500 символов текста
            preview = text[:500] + ("..." if len(text) > 500 else "")
            print(f"\n📄 Предпросмотр текста:\n{preview}")
            print(f"\n📊 Статистика:")
            print(f"   Символов: {len(text):,}")
            print(f"   Слов: {len(text.split()):,}")
            print(f"\n💾 Файлы:")
            print(f"   Исходный: {file_path}")
            print(f"   Аудио для транскрибации: {audio_path}")
            print(f"   Текст: {audio_path.with_suffix('.txt')}")
        else:
            print("\n❌ Ошибка сохранения")

    except KeyboardInterrupt:
        print("\n\n⏹️  Прервано пользователем")
    except Exception as e:
        print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()