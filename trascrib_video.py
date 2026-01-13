import sys
import subprocess
import os
from pathlib import Path
from typing import Optional
import time
import numpy as np


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


def load_audio_with_ffmpeg(audio_path: Path, ffmpeg_path: Path) -> np.ndarray:
    """Загружаем аудио через ffmpeg напрямую"""
    import tempfile
    import soundfile as sf

    # Создаем временный WAV файл (whisper лучше работает с WAV)
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Конвертируем MP3 в WAV через ffmpeg
        cmd = [
            str(ffmpeg_path),
            '-i', str(audio_path.absolute()),
            '-ar', '16000',  # 16kHz частота дискретизации
            '-ac', '1',  # моно
            '-acodec', 'pcm_s16le',
            '-y',
            '-loglevel', 'error',
            tmp_path
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"FFmpeg error: {result.stderr}")

        # Загружаем WAV файл
        import librosa
        audio, sr = librosa.load(tmp_path, sr=16000, mono=True)
        return audio

    finally:
        # Удаляем временный файл
        try:
            os.unlink(tmp_path)
        except:
            pass


def clean_path(path_str: str) -> Path:
    """Очистка пути от кавычек и нормализация слешей"""
    path_str = path_str.strip().strip('"').strip("'")
    path_str = path_str.replace('\\', '/')
    return Path(path_str)


def print_progress(step: int, total: int, message: str):
    """Простой текстовый прогресс-бар"""
    progress = "█" * step + "░" * (total - step)
    print(f"\r[{progress}] {message}", end="", flush=True)
    if step == total:
        print()


def convert_mp4_to_mp3(video_path: Path) -> Optional[Path]:
    """Конвертирует MP4 в MP3 через ffmpeg"""
    ffmpeg_path = find_ffmpeg()

    if not ffmpeg_path:
        print("\n❌ FFmpeg не найден!")
        print("\n📥 Установите FFmpeg в C:\\ffmpeg\\")
        print("   Или добавьте в переменную PATH")
        return None

    try:
        audio_path = video_path.with_suffix('.mp3')
        print_progress(1, 4, f"Конвертация {video_path.name} в MP3...")

        audio_path_abs = audio_path.absolute()
        video_path_abs = video_path.absolute()

        print(f"   Исходный: {video_path_abs}")
        print(f"   Целевой: {audio_path_abs}")

        # Удаляем старый MP3 файл если существует
        if audio_path_abs.exists():
            print(f"   Удаляем старый файл...")
            audio_path_abs.unlink()

        cmd = [
            str(ffmpeg_path),
            '-i', str(video_path_abs),
            '-q:a', '2',
            '-map', 'a',
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

        if result.returncode == 0:
            time.sleep(1)  # Даем время на запись
            if audio_path_abs.exists():
                size_mb = audio_path_abs.stat().st_size / (1024 * 1024)
                print(f"\n✅ Аудиофайл создан: {audio_path_abs}")
                print(f"   Размер: {size_mb:.1f} MB")
                return audio_path_abs
            else:
                print(f"\n❌ Аудиофайл не создан!")
                return None
        else:
            print(f"\n❌ Ошибка FFmpeg: {result.stderr[:500]}")
            return None

    except Exception as e:
        print(f"\n❌ Ошибка конвертации: {e}")
        return None


def transcribe_audio(audio_path: Path, ffmpeg_path: Path) -> Optional[str]:
    """Транскрибирует аудио через Whisper"""
    try:
        print_progress(2, 4, "Загрузка модели Whisper...")

        if not audio_path.exists():
            print(f"\n❌ Аудиофайл не найден: {audio_path}")
            return None

        print(f"\n   Аудиофайл: {audio_path}")
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
        return False


def main():
    print("=" * 60)
    print("🎬 MP4 → MP3 → Текст конвертер")
    print("=" * 60)

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

    if len(sys.argv) > 1:
        input_str = sys.argv[1]
    else:
        print("\n📋 Вставьте путь к MP4 файлу:")
        print("   Можно перетащить файл прямо в это окно")
        print("\nПуть: ", end="")
        input_str = input().strip()

    try:
        video_path = clean_path(input_str).absolute()
    except Exception as e:
        print(f"\n❌ Ошибка обработки пути: {e}")
        return

    if not video_path.exists():
        print(f"\n❌ Файл не найден: {video_path}")
        return

    if video_path.suffix.lower() != '.mp4':
        print(f"\n❌ Это не MP4 файл: {video_path.suffix}")
        return

    print(f"\n📂 Файл: {video_path.name}")
    print(f"📁 Папка: {video_path.parent}")
    print(f"📊 Размер: {video_path.stat().st_size / (1024 * 1024):.1f} MB")
    print("-" * 60)

    try:
        # 1. Конвертация
        audio_path = convert_mp4_to_mp3(video_path)
        if not audio_path:
            print("\n❌ КОНВЕРТАЦИЯ НЕ УДАЛАСЬ")
            return

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
            print(f"   Видео: {video_path}")
            print(f"   Аудио: {audio_path}")
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