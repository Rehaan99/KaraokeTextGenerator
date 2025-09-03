import json
import os
from pathlib import Path
    
BASE_DIR = Path(__file__).resolve().parent
SONG_LIST_JSON_FILE = BASE_DIR / "song_list.json"
AUDIO_DIRECTORY = BASE_DIR / "audioFiles"
UNGENERATED_SONGS_FILE = BASE_DIR / "ungenerated_songs.json"
songs = json.load(open(SONG_LIST_JSON_FILE, "r", encoding="utf-8"))

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def add_songs():
    clear_console()
    audio_files = [f for f in os.listdir(AUDIO_DIRECTORY) if os.path.isfile(os.path.join(AUDIO_DIRECTORY, f))]
    audio_file_names = [f.replace(".wav", "") for f in audio_files]
    for song in songs:
        if song["song_name"] in audio_file_names:
            audio_file_names.remove(song["song_name"])

    if audio_file_names:
        for audio_file in audio_file_names:
            print(f"Found audio file for new song: {audio_file}")
            new_song_name = audio_file
            new_song = {"Id": len(songs) + 1, "song_name": new_song_name}
            songs.append(new_song)
            with open(UNGENERATED_SONGS_FILE, "w", encoding="utf-8") as f:
                json.dump(songs, f, indent=4)
            print(f"Added song: {new_song_name} to ungenerated songs file. Run generate_lyrics to create lyrics.")
    else:
        print("No new audio files found.")