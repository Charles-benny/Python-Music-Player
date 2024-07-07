# Music Player

## Overview
This is a simple yet powerful Music Player application built using Python's Tkinter library for the graphical user interface, Pygame for audio playback, and Pillow for image handling. The app supports basic functionalities such as playing, pausing, stopping, resuming, navigating between songs, and managing playlists. 

## Features
- **Open Folder**: Browse and select a folder containing your favorite music files (.mp3).
- **Play/Pause/Stop**: Control music playback with ease.
- **Next/Previous Song**: Navigate through your playlist effortlessly.
- **Remove Song**: Remove a song from the playlist.
- **Volume Control**: Adjust the volume using a convenient slider.
- **Track Duration**: Display the duration of the currently playing track.
- **Song Title Display**: Show the name of the currently playing song.
- **User Interface**: Intuitive and visually appealing interface with custom icons and images.

## Screenshots
![Music Player](https://github.com/Charles-benny/Python-Music-Player/assets/121818645/1fa662e3-f7c4-44da-8919-8ce88b2e0a95)


## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/music-player.git
    ```
2. Navigate to the project directory:
    ```sh
    cd music-player
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the application:
    ```sh
    python music_player.py
    ```

## Requirements
- Python 3.x
- Tkinter
- Pygame
- Pillow
- Mutagen

## Usage
1. Click on the "Open Folder" button to select a folder containing .mp3 files.
2. Use the Play, Pause, Stop, Next, and Previous buttons to control the music playback.
3. Adjust the volume using the slider.
4. The currently playing song and its duration will be displayed at the bottom of the app.

## Project Structure
```plaintext
music-player/
│
├── assets/
│   ├── DISPLAY.jpg
│   ├── LOGO.jpg
│   ├── NEXT.png
│   ├── PAUSE.png
│   ├── PLAY.png
│   ├── PREVIOUS.png
│   ├── REMOVE.png
│   ├── RESUME.png
│   ├── STOP.png
│   └── TOP.png
│
├── screenshots/
│   └── music_player_interface.png
│
├── music_player.py
├── requirements.txt
└── README.md
