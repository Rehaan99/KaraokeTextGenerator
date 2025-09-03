@echo off

SET IMAGE_NAME=itzray/console-text-writer
SET COMMAND=%1
SET SONG_ID=%2

REM Check if command is 'list'
IF /I "%COMMAND%"=="list" (
    docker run --rm -it %IMAGE_NAME% list
    GOTO :EOF
)

REM Check if command is 'play'
IF /I "%COMMAND%"=="play" (
    IF "%SONG_ID%"=="" GOTO :MISSING_ID
    docker run --rm -it %IMAGE_NAME% play --song-id %SONG_ID%
    GOTO :EOF
)

REM If none of the above, show usage
ECHO Invalid command.
ECHO Usage: run_songs.bat {list|play <song_id>}

:MISSING_ID
    ECHO Missing song ID.
    ECHO Usage: run_songs.bat play <song_id>
    GOTO :EOF