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

### Current Considerations and Future Expansion
