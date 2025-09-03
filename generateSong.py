import whisper
import json
import os
from availableSongs import song_name
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
LYRICS_DIR = BASE_DIR / "lyricFiles"
AUDIO_DIR = BASE_DIR / "audioFiles"
SONG_LIST_JSON_FILE = BASE_DIR / "song_list.json"
UNGENERATED_SONGS_FILE = BASE_DIR / "ungenerated_songs.json"
    
def _generate_lyrics():
    clear_console()
    with open(UNGENERATED_SONGS_FILE, "r", encoding="utf-8") as f:
        songs_json = json.load(f)

    for song_json in songs_json:
        song_name = song_json["song_name"]
        if os.path.exists(
            LYRICS_DIR / f"{song_name}.json"
        ):
            print(f"Lyric file for {song_name} already exists.")
            print(f"{song_name} will be deleted from ungenerated list.")
            return
        if not os.path.exists(
            AUDIO_DIR / f"{song_name}.wav"
        ):
            print(f"Audio file for {song_name} does not exist.")
            print(f"{song_name} will be deleted from ungenerated list.")
            return
        model = whisper.load_model("turbo")
        result = model.transcribe(
            f"{AUDIO_DIR}\\{song_name}.wav",
            language="en", #Make this a parameter
            temperature=0.0,
            word_timestamps=True,
        )
        words_json = []
        idx = 1
        for segment in result["segments"]:
            for word_info in segment["words"]:
                words_json.append(
                    {
                        "id": idx,
                        "start": round(word_info["start"], 2),
                        "end": round(word_info["end"], 2),
                        "word": word_info["word"],
                    }
                )
                idx += 1
        with open(
            f"{LYRICS_DIR}\\{song_name}.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(words_json, f, ensure_ascii=False, indent=2)

def generate_lyrics():
    _generate_lyrics()
    with open(
            UNGENERATED_SONGS_FILE,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump("", f, ensure_ascii=False, indent=2)
    print("Lyrics generation complete.")
    print("ungenerated songs list emptied.")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

