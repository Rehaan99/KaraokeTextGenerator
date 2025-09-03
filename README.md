# 🎶 Console Text Writer

A tool to generate and display song lyrics in sync with audio directly in your terminal, with Docker support.

---

## ✨ Available Functions

### 📝 Song Management

- **`add_songs`**  
  Scans `.wav` files in the `audioLyrics/` folder and adds them to the `ungenerated_songs` list.  
  ➡️ Next, call `generate_lyrics` to process these songs.

- **`generate_lyrics`**  
  Generates lyric timing JSON files stored in the `lyricFiles/` directory.  
  ⚠️ Currently supports **English songs only**. Accuracy may vary — manual review is recommended.

---

### 🎵 Docker Commands

The docker image can be found at **`itzray/console-text-writer`**

```bash
docker run --rm -it itzray/console-text-writer list
```

- **`cmd_list_songs`**  
  Lists all available songs with their IDs for playback.

  ```bash
  docker run --rm -it console-text-writer list
  ```

  - **`cmd_play_song`**  
    Displays the lyrics in sync with audio for a selected song.

  ```bash
  docker run --rm -it console-text-writer play --song-id 1
  ```

### Find this code in action on tiktok and youtube

<a href="https://www.tiktok.com/@mhffn_">
  <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/69/TikTok_logo.svg/1200px-TikTok_logo.svg.png" width="32"/>
</a>
<a href="https://www.youtube.com/@1ts_Ray/shorts">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" width="32"/>
</a>

### Current Considerations and Future Expansion

- Add Lite and Complete edition docker images, lite will be the current version, complete will include the ai generation (currently omitted due to file size)
  - Turn the other functions into docker callable functions.
  - Allow a long running container that can accept .wav files and create local lyric files.
- Also play the audio file at the same time. Makes things easier to sync up.
-
