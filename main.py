import asyncio
from shazamio import Shazam
from helper import get_required_song_info
from songMetadata import editMusicTag, get_music_metadata


async def main(musicFile):
  """
  Recognises the song and returns the metadata

  Args:
  - musicTrack: The path to the music file

  Returns:
  - A Dictionary with the metadata of the song created by Shazam 
  """

  shazam = Shazam()
  out = await shazam.recognize_song(musicFile)
  song_info = get_required_song_info(out)
  editMusicTag(song_info, musicFile)
  print(f"{musicFile} Catalouged!!\n\n")
  # print(get_music_metadata(musicFile))



if __name__ == '__main__':
  musicFolder = u'test/music_folder'
  musicTrack = f'{musicFolder}/Jack Harlow - Lovin On Me [Official Music Video] (320 kbps).mp3'
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main(musicTrack))
