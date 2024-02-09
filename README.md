### Title: Music Recognition and Metadata Cataloging using eyed3 & Shazam

#### Description:
This Python script utilizes the Shazam API for music recognition and cataloging metadata of songs. It takes a music file as input, recognizes the song using Shazam, extracts required song information, edits the music file's metadata, and prints the metadata information. The script is designed to be asynchronous, leveraging asyncio for concurrent operations.

#### Key Features:
- Utilizes the Shazam API for song recognition.
- Asynchronous processing using asyncio for improved efficiency.
- Extracts required song information and edits music file metadata accordingly.
- Prints the metadata information of the recognized song.

#### Files:
1. `main.py`: Contains the main script for recognizing and cataloging music.
2. `helper.py`: Helper functions for extracting required song information.
3. `songMetadata.py`: Functions for editing music file metadata and retrieving metadata information.

#### Usage:
1. Ensure the required dependencies (`shazamio`) are installed.
2. Run `main.py` with the path to the music file as an argument.
3. The script will recognize the song using Shazam, edit the metadata, and print the metadata information.

#### Dependencies:
- `shazamio`: Python package for interfacing with the Shazam API.
- `asyncio`: For asynchronous operations.
