#!/usr/bin/env python3
"""
YouTube Downloader (Console Edition)
Автор: Продвинутый энтузиаст
Дата: 2026-01-13
"""

import sys
import os
import subprocess
import socket
import shutil
from pathlib import Path
from typing import Optional, List
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from pytubefix.exceptions import PytubeFixError, VideoUnavailable, MembersOnly, LiveStreamError

# ============================================================================
# КОНФИГУРАЦИЯ
# ============================================================================

# 🛡️ Настройки прокси (при необходимости обхода ограничений)
PROXY_SETTINGS = None
# PROXY_SETTINGS = {
#     'http': 'http://user:pass@proxy_ip:port',
#     'https': 'http://user:pass@proxy_ip:port'
# }

# 📁 Путь по умолчанию (Q:\YT)
DEFAULT_PATH = Path("Q:/YT")


# ============================================================================
# УТИЛИТЫ
# ============================================================================

def clean_windows_path(path_str: str) -> Path:
    """Очищает путь Windows от кавычек и нормализует слеши."""
    path_str = path_str.strip().strip('"').strip("'")
    path_str = path_str.replace('\\', '/')
    return Path(path_str)


def normalize_urls(urls_input: str) -> List[str]:
    """
    Нормализует список URL, разделённых пробелами.
    Пример: "url1 url2 url3" -> ["url1", "url2", "url3"]
    """
    urls = []
    for url in urls_input.strip().split():
        url = url.strip().strip('"').strip("'")
        if url:
            urls.append(url)
    return urls


def print_header(title: str):
    """Красивый заголовок в консоли."""
    print("\n" + "=" * 60)
    print(f"🎬 {title}")
    print("=" * 60)


def test_connection(url: str = "https://www.youtube.com") -> bool:
    """Проверяет доступность интернета и YouTube."""
    try:
        socket.create_connection(("www.youtube.com", 80), timeout=5)
        print("✅ Сетевое подключение активно")
        return True
    except OSError as e:
        print(f"❌ Проблемы с сетью: {e}")
        print("💡 Проверьте подключение к интернету")
        return False


def setup_ffmpeg() -> bool:
    """Автоматически настраивает доступ к ffmpeg для Windows."""

    # 1️⃣ Проверяем, доступен ли ffmpeg в PATH
    if shutil.which("ffmpeg"):
        print("✅ ffmpeg найден в системном PATH")
        return True

    # 2️⃣ Проверяем возможные пути установки Windows
    common_paths = [
        Path("C:/ffmpeg/bin"),
        Path("C:/Program Files/ffmpeg/bin"),
        Path("C:/Program Files (x86)/ffmpeg/bin"),
        Path.cwd() / "ffmpeg/bin",
        Path.cwd() / "ffmpeg",
    ]

    for ffmpeg_path in common_paths:
        ffmpeg_exe = ffmpeg_path / "ffmpeg.exe" if ffmpeg_path.is_dir() else ffmpeg_path
        if ffmpeg_exe.exists():
            ffmpeg_dir = str(ffmpeg_exe.parent)
            os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
            print(f"✅ ffmpeg найден в: {ffmpeg_dir}")
            print("   (добавлено в PATH текущей сессии)")
            return True

    # 3️⃣ Предлагаем скачать портативную версию
    print("\n" + "=" * 60)
    print("❌ ffmpeg НЕ НАЙДЕН в системе")
    print("=" * 60)
    print("\n📦 РЕКОМЕНДУЕМЫЙ ВАРИАНТ:")
    print("   1. Скачайте портативный ffmpeg:")
    print("      🔗 https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
    print("\n   2. Распакуйте архив")
    print("   3. Поместите папку 'ffmpeg' в ту же директорию, где находится этот скрипт")
    print("\n   ИЛИ скопируйте только ffmpeg.exe в папку со скриптом")

    print("\n💡 FFmpeg нужен для:")
    print("   - Объединения видео 1080p+ (аудио + видео потоки)")
    print("   - Конвертации аудио в MP3")
    print("   - Изменения качества/разрешения")

    # 4️⃣ Предлагаем продолжить без ffmpeg
    print("\n" + "=" * 60)
    choice = input("Продолжить без ffmpeg? (y/n): ").strip().lower()

    if choice == 'y':
        print("⚠️  Высокое качество (1080p+) будет недоступно")
        print("   Конвертация в MP3 будет недоступна")
        print("   Доступно только до 720p (progressive streams)")
        return False
    else:
        print("\n❌ Программа остановлена")
        print("   Установите ffmpeg и перезапустите программу")
        input("\nНажмите Enter для выхода...")
        sys.exit(1)


# ============================================================================
# ОСНОВНЫЕ ФУНКЦИИ ЗАГРУЗКИ
# ============================================================================

def convert_to_mp3(input_path: Path, output_path: Path, title: str) -> Optional[Path]:
    """Конвертирует аудио файл в MP3 с метаданными."""
    try:
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        mp3_path = output_path / f"{safe_title}.mp3"

        print(f"🔄 Конвертирую в MP3...")

        # Команда ffmpeg для конвертации в MP3 с метаданными
        result = subprocess.run(
            ['ffmpeg', '-i', str(input_path),
             '-q:a', '0',  # Качество V0 (переменный битрейт)
             '-map', 'a',  # Только аудио
             '-id3v2_version', '3',  # ID3v2.3 теги
             '-metadata', f'title={title}',
             '-metadata', 'encoder=YouTube Downloader',
             '-loglevel', 'error', '-y', str(mp3_path)],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            # Удаляем временный MP4 файл
            input_path.unlink(missing_ok=True)
            print(f"✅ Аудио сконвертировано в MP3: {mp3_path.name}")
            return mp3_path
        else:
            print(f"⚠️  Ошибка конвертации: {result.stderr}")
            print("💡 Оставляю оригинальный MP4 файл")
            return input_path

    except subprocess.TimeoutExpired:
        print("❌ Таймаут при конвертации")
        return input_path
    except Exception as e:
        print(f"❌ Ошибка при конвертации: {e}")
        return input_path


def download_audio(yt: YouTube, output_path: Path, ffmpeg_available: bool) -> Optional[Path]:
    """Скачивает аудио и конвертирует в MP3 если доступен ffmpeg."""
    try:
        print("🔍 Ищу аудио поток...")
        audio_stream = yt.streams.get_audio_only()
        if not audio_stream:
            print("❌ Аудио поток не найден")
            return None

        # Безопасное имя файла
        safe_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        filename = f"AUDIO_{safe_title}.mp4"

        print(f"📥 Загружаю аудио ({audio_stream.abr})...")
        file_path = audio_stream.download(
            output_path=str(output_path),
            filename=filename,
            skip_existing=False
        )

        mp4_path = Path(file_path)

        # Конвертируем в MP3 если доступен ffmpeg
        if ffmpeg_available:
            mp3_path = convert_to_mp3(mp4_path, output_path, yt.title)
            return mp3_path if mp3_path else mp4_path
        else:
            print("💡 ffmpeg недоступен, сохраняю как MP4")
            return mp4_path

    except Exception as e:
        print(f"❌ Ошибка загрузки аудио: {e}")
        return None


def download_video(yt: YouTube, output_path: Path, quality_choice: str, ffmpeg_available: bool) -> Optional[Path]:
    """Скачивает видео в выбранном качестве."""
    try:
        # Шаг 1: Определяем целевое разрешение
        target_res = None
        if quality_choice == "1":
            target_res = "1080p"
        elif quality_choice == "2":
            target_res = "720p"
        elif quality_choice == "3":
            print("🔍 Ищу максимальное доступное качество...")
            video_streams = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by(
                'resolution').desc()
            best_video_stream = video_streams.first()
            if best_video_stream:
                target_res = best_video_stream.resolution
                print(f"   Найдено: {target_res}")
            else:
                print("❌ Не удалось найти адаптивные видео-потоки")
                return None

        # Шаг 2: Если выбрано конкретное разрешение (1080p или 720p)
        if target_res in ("1080p", "720p"):
            print(f"🔍 Ищу видео {target_res} (требует объединения с аудио)...")

            # 2A. Ищем видео-поток с нужным разрешением
            video_stream = yt.streams.filter(
                adaptive=True,
                file_extension='mp4',
                only_video=True,
                resolution=target_res
            ).first()

            # 2B. Ищем лучший аудио-поток
            audio_stream = yt.streams.filter(
                adaptive=True,
                only_audio=True,
                file_extension='mp4'
            ).order_by('abr').desc().first()

            if not video_stream or not audio_stream:
                print(f"❌ Для {target_res} не найден видео или аудио поток.")
                if target_res == "1080p":
                    print("💡 Пробую найти 720p...")
                    return download_video(yt, output_path, "2", ffmpeg_available)
                return None

            # 2C. Скачиваем оба потока
            safe_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            video_filename = f"VID_{safe_title}_{target_res}.mp4"
            audio_filename = f"AUD_{safe_title}.mp4"
            output_filename = f"{safe_title}_{target_res}.mp4"

            print(f"📥 Загружаю видео: {target_res}...")
            video_path = video_stream.download(output_path=str(output_path), filename=video_filename)
            print(f"📥 Загружаю аудио: {audio_stream.abr}...")
            audio_path = audio_stream.download(output_path=str(output_path), filename=audio_filename)

            # 2D. Объединяем с помощью ffmpeg
            if ffmpeg_available:
                print("🔄 Объединяю аудио и видео...")
                final_path = output_path / output_filename
                try:
                    result = subprocess.run(
                        ['ffmpeg', '-i', str(video_path), '-i', str(audio_path),
                         '-c', 'copy', '-loglevel', 'error', '-y', str(final_path)],
                        capture_output=True,
                        text=True,
                        timeout=300
                    )

                    if result.returncode == 0:
                        Path(video_path).unlink(missing_ok=True)
                        Path(audio_path).unlink(missing_ok=True)
                        print(f"✅ Видео собрано: {final_path.name}")
                        return final_path
                    else:
                        print(f"⚠️  Ошибка ffmpeg: {result.stderr}")
                        return Path(video_path)

                except subprocess.TimeoutExpired:
                    print("❌ Таймаут при объединении (слишком долго)")
                    return Path(video_path)
                except Exception as e:
                    print(f"❌ Ошибка при объединении: {e}")
                    return Path(video_path)
            else:
                print("❌ ffmpeg недоступен - пропускаю объединение")
                print("💡 Видео и аудио сохранены отдельно:")
                print(f"   Видео: {video_path}")
                print(f"   Аудио: {audio_path}")
                print("\n   Для объединения вручную используйте:")
                print(f'   ffmpeg -i "{video_path}" -i "{audio_path}" -c copy output.mp4')
                return Path(video_path)

        # Шаг 3: Если выбран режим "максимального" (качество не 1080p/720p)
        else:
            print(f"🔍 Ищу лучший прогрессивный поток...")
            stream = yt.streams.get_highest_resolution()
            if stream:
                print(f"📥 Загружаю: {stream.resolution}...")
                safe_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                filename = f"VIDEO_{safe_title}_{stream.resolution}.mp4"
                file_path = stream.download(output_path=str(output_path), filename=filename)
                return Path(file_path)

        return None

    except Exception as e:
        print(f"❌ Ошибка загрузки видео: {e}")
        import traceback
        traceback.print_exc()
        return None


def process_youtube_url(url: str, media_type: str, quality: str, save_path: Path, ffmpeg_available: bool) -> bool:
    """Основная функция обработки YouTube ссылки."""
    try:
        yt = YouTube(
            url,
            on_progress_callback=on_progress,
            proxies=PROXY_SETTINGS
        )

        print(f"\n📋 Информация о видео:")
        print(f"   Название: {yt.title}")
        print(f"   Автор: {yt.author}")
        print(f"   Длительность: {yt.length // 60}:{yt.length % 60:02d}")
        print(f"   Просмотров: {yt.views:,}")

        save_path.mkdir(parents=True, exist_ok=True)

        if media_type == "1":
            file_path = download_video(yt, save_path, quality, ffmpeg_available)
        else:
            file_path = download_audio(yt, save_path, ffmpeg_available)

        if file_path and file_path.exists():
            file_size = file_path.stat().st_size / (1024 * 1024)
            file_ext = file_path.suffix.upper()
            print(f"\n✅ Успешно сохранено: {file_path.name}")
            print(f"📁 Путь: {file_path}")
            print(f"📊 Размер: {file_size:.1f} MB")
            print(f"📄 Формат: {file_ext}")
            return True
        else:
            print("❌ Загрузка не удалась")
            return False

    except VideoUnavailable:
        print("❌ Видео недоступно (удалено или приватное)")
        return False
    except MembersOnly:
        print("❌ Только для участников канала")
        return False
    except LiveStreamError:
        print("❌ Это прямой эфир (нельзя скачать)")
        return False
    except PytubeFixError as e:
        print(f"❌ Ошибка pytubefix: {e}")
        print("💡 Попробуйте обновить pytubefix: pip install --upgrade pytubefix")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False


# ============================================================================
# ТОЧКА ВХОДА
# ============================================================================

def get_save_path() -> Path:
    """Получает путь для сохранения от пользователя."""
    print("\n📁 ВЫБЕРИТЕ ПУТЬ ДЛЯ СОХРАНЕНИЯ:")
    print("   1. Сохраняем по умолчанию Q:\\YT")
    print("   2. Указать свой путь")

    choice = input("> ").strip()

    if choice == "1":
        save_path = DEFAULT_PATH
        print(f"✅ Используем путь по умолчанию: {save_path}")
    elif choice == "2":
        print("\n📁 Введите свой путь для сохранения:")
        path_input = input("> ").strip()
        if path_input:
            save_path = clean_windows_path(path_input)
        else:
            save_path = Path.cwd() / "YouTube_Downloads"
            print(f"⚠️  Путь не указан, использую: {save_path}")
    else:
        print("⚠️  Неверный выбор, использую путь по умолчанию")
        save_path = DEFAULT_PATH

    return save_path


def main():
    """Главная функция программы."""
    print_header("YouTube Downloader")

    print("🔍 Проверяем системные зависимости...")
    ffmpeg_available = setup_ffmpeg()

    try:
        import pytubefix
        print(f"✅ pytubefix {pytubefix.__version__}")
    except ImportError:
        print("❌ pytubefix не установлен")
        print("📦 Установите: pip install pytubefix")
        if input("   Установить сейчас? (y/n): ").lower() == 'y':
            os.system("pip install pytubefix")
            print("🔄 Перезапустите программу")
        return

    if not test_connection():
        if input("💡 Продолжить без проверки сети? (y/n): ").lower() != 'y':
            return

    # 🔄 Режим пакетной обработки
    urls = []
    if len(sys.argv) > 1:
        print("\n🔗 Обнаружены ссылки в аргументах командной строки")
        all_args = " ".join(sys.argv[1:])
        urls = normalize_urls(all_args)
        print(f"📋 Найдено ссылок: {len(urls)}")
        for i, url in enumerate(urls, 1):
            print(f"   {i}. {url[:60]}{'...' if len(url) > 60 else ''}")
    else:
        print("\n📥 Введите ссылку YouTube (можно несколько через пробел):")
        url_input = input("> ").strip()
        urls = normalize_urls(url_input)

    if not urls:
        print("❌ Не указано ни одной ссылки")
        return

    # Выбор типа медиа
    print("\n🎵 Что скачиваем?")
    print("   1. Видео")
    print("   2. Только аудио (MP3 при наличии ffmpeg)")
    media_type = input("> ").strip()

    if media_type not in ("1", "2"):
        print("❌ Выберите 1 или 2")
        return

    quality = "3"
    if media_type == "1":
        print("\n📊 Выберите качество видео:")
        print("   1. 1080p (если доступно, требует ffmpeg)" + ("" if ffmpeg_available else " - НЕДОСТУПНО"))
        print("   2. 720p или меньше")
        print("   3. Максимально возможное")
        quality = input("> ").strip()

        if quality not in ("1", "2", "3"):
            print("⚠️  Использую максимальное качество")
            quality = "3"

        if quality == "1" and not ffmpeg_available:
            print("❌ 1080p недоступно без ffmpeg, использую максимальное")
            quality = "3"

    # Выбор пути сохранения
    save_path = get_save_path()
    print(f"💾 Сохраняем в: {save_path}")

    # Обработка всех ссылок
    success_count = 0
    total_count = 0

    try:
        for url_index, url in enumerate(urls, 1):
            print(f"\n{'=' * 60}")
            print(f"📦 Обработка ссылки {url_index}/{len(urls)}")
            print(f"{'=' * 60}")

            is_playlist = "playlist?list=" in url or "/playlist" in url

            if is_playlist:
                print("📚 Обнаружен плейлист, загружаю информацию...")
                playlist = Playlist(url)
                videos = list(playlist.videos)
                playlist_total = len(videos)

                print(f"🎯 Найдено видео в плейлисте: {playlist_total}")
                print(f"📛 Название плейлиста: {playlist.title}")

                for i, video in enumerate(videos, 1):
                    print(f"\n🎬 Видео {i}/{playlist_total}: {video.title}")
                    if process_youtube_url(video.watch_url, media_type, quality, save_path, ffmpeg_available):
                        success_count += 1
                    total_count += 1
            else:
                total_count += 1
                if process_youtube_url(url, media_type, quality, save_path, ffmpeg_available):
                    success_count += 1

    except KeyboardInterrupt:
        print("\n\n⏹️  Прервано пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка обработки: {e}")

    # Итоги
    print_header("ИТОГИ СКАЧИВАНИЯ")
    print(f"📊 Обработано ссылок: {len(urls)}")
    print(f"📊 Всего видео/аудио: {total_count}")
    print(f"✅ Успешно скачано: {success_count}")

    if success_count > 0:
        print(f"📁 Файлы сохранены в: {save_path}")
        if media_type == "2" and ffmpeg_available:
            print("🎵 Аудио сконвертировано в MP3")
        print("✅ Готово!")
    else:
        print("❌ Ничего не скачано")

    if total_count > 0 and success_count < total_count:
        print(f"⚠️  Часть загрузок не удалась: {total_count - success_count}")


# ============================================================================
# ЗАПУСК
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 Критическая ошибка: {e}")
        import traceback

        traceback.print_exc()
        input("Нажмите Enter для выхода...")
        sys.exit(1)