import eyed3


def get_genre(genre=None):
  genre_name = eyed3.id3.Genre().name if genre is None else genre
  print(f"Genre is {genre_name}")
  return genre_name


def get_music_metadata(track):
  audio = eyed3.load(track)
  audio_data = {
      "Title": audio.tag.title,
      "Artist": audio.tag.artist,
      "Album": audio.tag.album,
      "Publisher": audio.tag.publisher,
      "Genre": f"{get_genre()}",
      "Release_date": int(audio.tag.release_date.year)
  }
  return audio_data


if __name__ == '__main__':
  musicTrack = u'test/music_folder/Bebe Rexha - Sacrifice [Official Music Video].mp3'
  print(get_music_metadata(musicTrack))
