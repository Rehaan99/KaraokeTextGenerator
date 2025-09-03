COMMAND=$1
SONG_ID=$2

IMAGE_NAME=console-text-writer

if [ "$COMMAND" == "list" ]; then
    docker run --rm -it $IMAGE_NAME list
    exit 0
fi

if [ "$COMMAND" == "play" ]; then
    if [ -z "$SONG_ID" ]; then
        echo "Missing song ID."
        exit 1
    fi
    docker run --rm -it $IMAGE_NAME play --song-id $SONG_ID
    exit 0
fi

echo "Invalid command."
echo "Usage: run_songs.sh {list|play <song_id>}"