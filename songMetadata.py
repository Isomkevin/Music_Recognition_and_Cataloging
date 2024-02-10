import os
import eyed3


def get_music_metadata(track):

  def get_genre():
    genre_object = eyed3.id3.Genre()
    genre_name = genre_object.name
    return genre_object

  audio = eyed3.load(track)
  audio_data = {
      "Title": audio.tag.title,
      "Artist": audio.tag.artist,
      "Album": audio.tag.album,
      "Publisher": audio.tag.publisher,
      "Genre": f"{get_genre()}",
      "Release_date": audio.tag.release_date
  }
  return audio_data


def renameSongTrack(filePath):
  """
  Rename a music file based on its metadata.

  Parameters:
  - filePath (str): The path to the music file.

  Returns:
  - None

  Description:
  This function takes a file path as input, extracts metadata (such as title and artist) from the audio file, and renames the file according to its metadata.

  Note:
  - The function assumes that the audio file is in MP3 format.
  """

  # Load metadata from the audio file
  audiofile = eyed3.load(filePath)
  new_filename = f"{audiofile.tag.title} - {audiofile.tag.artist}.mp3"
  os.rename(filePath, new_filename)


def editMusicTag(parameters, file_path):
  """
  Edit the tags of a music file specified by the file path using the provided
  parameters.

  Args:
      parameters (dict): A dictionary containing the tag parameters to edit.
                         Supported keys: 'TITLE', 'ARTIST', 'ALBUM',
                         'PUBLISHER', 'RELEASE_DATE'.
                         Each key should map to the corresponding tag value.
      file_path (str): The file path of the music file to be edited.

  Raises:
      ValueError: If the file path is invalid or if the specified tag
      parameters are not supported.

  Returns:
      None
  """
  audio_file = eyed3.load(file_path)
  if not audio_file.tag:
    audio_file.initTag()
  if parameters['trackTitle']:
    audio_file.tag.title = parameters['trackTitle']
  if parameters['trackArtist']:
    audio_file.tag.artist = parameters['trackArtist']
  if parameters['Album']:
    audio_file.tag.album = parameters['Album']
  if parameters['Label']:
    audio_file.tag.publisher = parameters['Label']
  if parameters['Released']:
    audio_file.tag.release_date = parameters['Released']

  audio_file.tag.save()


if __name__ == '__main__':
  musicTrack = 'The Chainsmokers - Side Effects (Official Video) ft. Emily Warren.mp3'
  print(get_music_metadata(musicTrack))
