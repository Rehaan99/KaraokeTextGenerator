import os
import time
import json
import pyfiglet
import argparse
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
LYRICS_DIR = BASE_DIR / "lyricFiles"
SONG_LIST_JSON_FILE = BASE_DIR / "song_list.json"
songs = json.load(open(SONG_LIST_JSON_FILE, "r", encoding="utf-8"))

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def cmd_play_song(args):
    clear_console()
    song_name = songs[args.song_id - 1]["song_name"] if args else input("Enter song number: ")
    lyric_file = LYRICS_DIR / f"{song_name}.json"
    if not lyric_file.exists():
        print(f"Lyric file for {song_name} does not exist.")
        print(lyric_file)
        return

    song_name_words = song_name.split("_", 1)[1]
    song_title = " ".join(word.capitalize() for word in song_name_words.split("_"))
    ascii_banner = pyfiglet.figlet_format(song_title, font="small")
    # solid_banner = "".join("█" if c != " " and c != "\n" else c for c in ascii_banner)
    print(ascii_banner)

    with open(lyric_file, "r", encoding="utf-8") as f:
        words = json.load(f)

    start_time = time.perf_counter()
    capitalize_next = True
    for word_info in words:
        is_end_of_line = False
        word = word_info["word"]
        if word.endswith(","):
            word = word[:-1]
            is_end_of_line = True
        elif word.endswith(".") or word.endswith("?") or word.endswith("!"):
            is_end_of_line = True

        while time.perf_counter() - start_time < word_info["start"]:
            time.sleep(0.005)
        duration = word_info["end"] - word_info["start"]
        n_chars = len(word)
        delay = duration / n_chars if n_chars > 0 else duration

        for i, char in enumerate(word):
            if capitalize_next and i == 1:
                char = char.upper()
                capitalize_next = False
            print(char, end="", flush=True)
            time.sleep(delay)

        if is_end_of_line:
            print()
            capitalize_next = True
        else:
            print(end="", flush=True)


def cmd_list_songs(_args):
    clear_console()
    ascii_banner = pyfiglet.figlet_format("Available Songs", font="small")
    print(ascii_banner)

    for song in songs:
        song_words = song['song_name'].split("_", 1)
        song_artist = song_words[0]
        song_title = " ".join(word.capitalize() for word in song_words[1].split("_"))
        print(f"{song['Id'] + 1} : \033[1m{song_artist}\033[0m - {song_title}")


def main():
    parser = argparse.ArgumentParser(prog="console-text-writer", description="Song tools")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List all songs")
    p_list.set_defaults(func=cmd_list_songs)

    p_play = sub.add_parser("play", help="Play a song by Id")
    p_play.add_argument("--song-id", "-i", type=int, required=True, help="Id of the song to play")
    p_play.set_defaults(func=cmd_play_song)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
