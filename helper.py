import urllib.parse

def get_nested_value(d, keys):
  """
  Retrieve the value from a nested dictionary using a sequence of keys.

  Args:
  - d: The nested dictionary
  - keys: A sequence of keys to traverse through the nested dictionary

  Returns:
  - The value associated with the keys, or None if the keys don't exist
  """
  if not isinstance(keys, (list, tuple)):
    keys = [keys]

  value = d
  for key in keys:
    if isinstance(value, dict):
      value = value.get(key)
    elif not isinstance(value, list):
      return None
  return value

def extract_nested_keys(data, parent_keys=[], keys=[]):
  """
  Recursively extracts keys from a nested dictionary.

  Args:
      data (dict): The nested dictionary from which keys are to be extracted.
      parent_keys (list, optional): List of parent keys. Defaults to an empty
      list.
      keys (list, optional): List to store the extracted keys. Defaults to an
      empty list.

  Returns:
      list: A list containing all extracted keys.
  """
  for key, value in data.items():
    current_keys = parent_keys + [key]
    if isinstance(value, dict):
      extract_nested_keys(value, current_keys, keys)
    elif isinstance(value, list):
      for item in value:
        if isinstance(item, dict):
          extract_nested_keys(item, current_keys, keys)
    else:
      keys.append(current_keys)
  return keys


required_song_info = {
    'primary_genre': ['track', 'genres', 'primary'],
    'trackTitle': ['track', 'urlparams', '{tracktitle}'],
    'trackArtist': ['track', 'urlparams', '{trackartist}'],
    'sections': ['track', 'sections']
}

def get_required_song_info(shazamData, song_metadata=required_song_info):
  """
  Extracts required song information from Shazam data based on provided metadata mappings.

  Args:
      song_metadata (dict): A dictionary containing metadata mappings for the song.
                            Keys represent the desired information (e.g.,'title','artist'),
                            and values represent the corresponding paths in the Shazam data.
      shazamData (dict): The Shazam data containing information about the
      song.

  Returns:
      dict: A dictionary containing the extracted song information based on
      the provided mappings.
  """
  song_info = {}
  for key, value in song_metadata.items():
    info = get_nested_value(shazamData, value)

    if info is not None:
      if isinstance(info, str):
        info = urllib.parse.unquote_plus(info)
        song_info[key] = info

      elif key == 'sections':
        # Accessing information from the first section (SONG)
        first_section = info[0]

        # Accessing metadata from the first section
        metadata = first_section['metadata']
        for item in metadata:
          title = item['title']
          text = item['text']
          song_info[title] = text

  return song_info

if __name__=='__main__':
  x = {
      'matches': [{
          'id': '439660395',
          'offset': 77.920421875,
          'timeskew': 0.0001231432,
          'frequencyskew': 0.0
      }],
      'location': {
          'accuracy': 0.01
      },
      'timestamp':
      1707128597475,
      'timezone':
      'Europe/Moscow',
      'track': {
          'layout':
          '5',
          'type':
          'MUSIC',
          'key':
          '432365947',
          'title':
          'Side Effects (feat. Emily Warren)',
          'subtitle':
          'The Chainsmokers',
          'images': {
              'background':
              'https://is1-ssl.mzstatic.com/image/thumb/AMCArtistImages116/v4/a1/df/f6/a1dff612-65e9-36ce-1167-c2ec7bee2899/7c048695-1009-4525-8f5a-c1319b768fc9_ami-identity-27852ea90adda198875408ceb0169bd5-2023-07-24T19-18-54.847Z_cropped.png/800x800cc.jpg',
              'coverart':
              'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/63/24/e1/6324e131-0034-4753-9cc6-ade1da39a4a8/886447471074.jpg/400x400cc.jpg',
              'coverarthq':
              'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/63/24/e1/6324e131-0034-4753-9cc6-ade1da39a4a8/886447471074.jpg/400x400cc.jpg',
              'joecolor': 'b:010101p:e9dac5s:caa7a7t:baaf9eq:a28686'
          },
          'share': {
              'subject': 'Side Effects (feat. Emily Warren) - The Chainsmokers',
              'text': 'Side Effects (feat. Emily Warren) by The Chainsmokers',
              'href':
              'https://www.shazam.com/track/432365947/side-effects-feat-emily-warren',
              'image':
              'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/63/24/e1/6324e131-0034-4753-9cc6-ade1da39a4a8/886447471074.jpg/400x400cc.jpg',
              'twitter':
              'I used @Shazam to discover Side Effects (feat. Emily Warren) by The Chainsmokers.',
              'html':
              'https://www.shazam.com/snippets/email-share/432365947?lang=en-US&country=GB',
              'avatar':
              'https://is1-ssl.mzstatic.com/image/thumb/AMCArtistImages116/v4/a1/df/f6/a1dff612-65e9-36ce-1167-c2ec7bee2899/7c048695-1009-4525-8f5a-c1319b768fc9_ami-identity-27852ea90adda198875408ceb0169bd5-2023-07-24T19-18-54.847Z_cropped.png/800x800cc.jpg',
              'snapchat': 'https://www.shazam.com/partner/sc/track/432365947'
          },
          'hub': {
              'type':
              'APPLEMUSIC',
              'image':
              'https://images.shazam.com/static/icons/hub/ios/v5/applemusic_{scalefactor}.png',
              'actions': [{
                  'name': 'apple',
                  'type': 'applemusicplay',
                  'id': '1445725445'
              }, {
                  'name':
                  'apple',
                  'type':
                  'uri',
                  'uri':
                  'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/1f/b6/18/1fb618b7-222d-0dd0-c6c9-26bacd727e1e/mzaf_2983518916803196311.plus.aac.ep.m4a'
              }],
              'options': [{
                  'caption':
                  'OPEN IN',
                  'actions': [{
                      'name':
                      'hub:applemusic:deeplink',
                      'type':
                      'applemusicopen',
                      'uri':
                      'https://music.apple.com/gb/album/side-effects-feat-emily-warren/1445725433?i=1445725445&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios'
                  }, {
                      'name':
                      'hub:applemusic:deeplink',
                      'type':
                      'uri',
                      'uri':
                      'https://music.apple.com/gb/album/side-effects-feat-emily-warren/1445725433?i=1445725445&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios'
                  }],
                  'beacondata': {
                      'type': 'open',
                      'providername': 'applemusic'
                  },
                  'image':
                  'https://images.shazam.com/static/icons/hub/ios/v5/overflow-open-option_{scalefactor}.png',
                  'type':
                  'open',
                  'listcaption':
                  'Open in Apple Music',
                  'overflowimage':
                  'https://images.shazam.com/static/icons/hub/ios/v5/applemusic-overflow_{scalefactor}.png',
                  'colouroverflowimage':
                  False,
                  'providername':
                  'applemusic'
              }, {
                  'caption':
                  'BUY',
                  'actions': [{
                      'type':
                      'uri',
                      'uri':
                      'https://itunes.apple.com/gb/album/side-effects-feat-emily-warren/1445725433?i=1445725445&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=itunes&itsct=Shazam_ios'
                  }],
                  'beacondata': {
                      'type': 'buy',
                      'providername': 'itunes'
                  },
                  'image':
                  'https://images.shazam.com/static/icons/hub/ios/v5/itunes-overflow-buy_{scalefactor}.png',
                  'type':
                  'buy',
                  'listcaption':
                  'Buy on iTunes',
                  'overflowimage':
                  'https://images.shazam.com/static/icons/hub/ios/v5/itunes-overflow-buy_{scalefactor}.png',
                  'colouroverflowimage':
                  False,
                  'providername':
                  'itunes'
              }],
              'providers': [{
                  'caption':
                  'Open in Spotify',
                  'images': {
                      'overflow':
                      'https://images.shazam.com/static/icons/hub/ios/v5/spotify-overflow_{scalefactor}.png',
                      'default':
                      'https://images.shazam.com/static/icons/hub/ios/v5/spotify_{scalefactor}.png'
                  },
                  'actions': [{
                      'name':
                      'hub:spotify:searchdeeplink',
                      'type':
                      'uri',
                      'uri':
                      'spotify:search:Side%20Effects%20%28feat.%20Emily%20Warren%29%20The%20Chainsmokers'
                  }],
                  'type':
                  'SPOTIFY'
              }, {
                  'caption':
                  'Open in Deezer',
                  'images': {
                      'overflow':
                      'https://images.shazam.com/static/icons/hub/ios/v5/deezer-overflow_{scalefactor}.png',
                      'default':
                      'https://images.shazam.com/static/icons/hub/ios/v5/deezer_{scalefactor}.png'
                  },
                  'actions': [{
                      'name':
                      'hub:deezer:searchdeeplink',
                      'type':
                      'uri',
                      'uri':
                      'deezer-query://www.deezer.com/play?query=%7Btrack%3A%27Side+Effects+%28feat.+Emily+Warren%29%27%20artist%3A%27The+Chainsmokers%27%7D'
                  }],
                  'type':
                  'DEEZER'
              }],
              'explicit':
              False,
              'displayname':
              'APPLE MUSIC'
          },
          'sections': [{
              'type':
              'SONG',
              'metapages': [{
                  'image':
                  'https://is1-ssl.mzstatic.com/image/thumb/AMCArtistImages116/v4/a1/df/f6/a1dff612-65e9-36ce-1167-c2ec7bee2899/7c048695-1009-4525-8f5a-c1319b768fc9_ami-identity-27852ea90adda198875408ceb0169bd5-2023-07-24T19-18-54.847Z_cropped.png/800x800cc.jpg',
                  'caption': 'The Chainsmokers'
              }, {
                  'image':
                  'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/63/24/e1/6324e131-0034-4753-9cc6-ade1da39a4a8/886447471074.jpg/400x400cc.jpg',
                  'caption': 'Side Effects (feat. Emily Warren)'
              }],
              'tabname':
              'Song',
              'metadata': [{
                  'title': 'Album',
                  'text': 'Sick Boy'
              }, {
                  'title': 'Label',
                  'text': 'Disruptor Records/Columbia'
              }, {
                  'title': 'Released',
                  'text': '2018'
              }]
          }, {
              'type':
              'LYRICS',
              'text': [
                  "It's 4 A.M., I don't know where to go",
                  'Everywhere is closed, I should just go home, yeah',
                  'My feet are taking me to your front door',
                  "I know I shouldn't though, heaven only knows", '',
                  'That ooh, the side effect to my loneliness is you', '',
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight',
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight', '',
                  'This happens every time I try to mix',
                  'Decision making with one too many drinks',
                  'But ooh, if late night friends have consequences, cool, yeah',
                  '', "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight',
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight', '',
                  'Oh, I think about it all the time',
                  "Make it happen in my mind, I'm telling you, yeah",
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight', '',
                  "Time should've taught me the lesson",
                  'Went looking for a sign but instead I got a message',
                  'I take off my pride every time we undressing',
                  "Draw the line, I'm outta line (yeah)",
                  "Time should've taught me the lesson",
                  'Went looking for a sign but instead I got a message',
                  'I take off my pride every time we undressing',
                  "Draw the line, I'm outta line", '',
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight, yeah',
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight, yeah', '',
                  'I, I think about it all the time',
                  "Make it happen in my mind, I'm telling you, yeah",
                  "Oh, you're all that I want", 'No good at giving you up',
                  'Come on and give me some love tonight', '',
                  "Time should've taught me the lesson",
                  'Went looking for a sign but instead I got a message',
                  'I take off my pride every time we undressing',
                  "Draw the line, I'm outta line, yeah",
                  "Time should've taught me the lesson",
                  'Went looking for a sign but instead I got a message',
                  'I take off my pride every time we undressing',
                  "Draw the line, I'm outta line, yeah"
              ],
              'url':
              'https://cdn.shazam.com/lyrics/v1/en-US/GB/iphone/musixmatch/subtitles/85790075/173/1?token=9b51c760138cf3859d9cec172a0412e5',
              'footer':
              'Writer(s): Andrew Taggart, Alexander J Pall, Sylvester Willy Sivertsen, Corey James Sanders, Emily Warren\nLyrics powered by www.musixmatch.com',
              'tabname':
              'Lyrics',
              'beacondata': {
                  'lyricsid': '30374290',
                  'providername': 'musixmatch',
                  'commontrackid': '85790075'
              }
          }, {
              'type':
              'VIDEO',
              'tabname':
              'Video',
              'youtubeurl':
              'https://cdn.shazam.com/video/v3/-/GB/iphone/432365947/youtube/video?q=The+Chainsmokers+%22Side+Effects+(feat.+Emily+Warren)%22'
          }, {
              'type': 'RELATED',
              'url':
              'https://cdn.shazam.com/shazam/v3/en-US/GB/iphone/-/tracks/track-similarities-id-432365947?startFrom=0&pageSize=20&connected=',
              'tabname': 'Related'
          }],
          'url':
          'https://www.shazam.com/track/432365947/side-effects-feat-emily-warren',
          'artists': [{
              'id': '42',
              'adamid': '580391756'
          }],
          'isrc':
          'USQX91801629',
          'genres': {
              'primary': 'Dance'
          },
          'urlparams': {
              '{tracktitle}': 'Side+Effects+%28feat.+Emily+Warren%29',
              '{trackartist}': 'The+Chainsmokers'
          },
          'myshazam': {
              'apple': {
                  'actions': [{
                      'name':
                      'myshazam:apple',
                      'type':
                      'uri',
                      'uri':
                      'https://music.apple.com/gb/album/side-effects-feat-emily-warren/1445725433?i=1445725445&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios'
                  }]
              }
          },
          'highlightsurls': {
              'artisthighlightsurl':
              'https://cdn.shazam.com/video/v3/en-US/GB/iphone/580391756/highlights?affiliate=mttnagencyid%3Ds2n%26mttnsiteid%3D125115%26mttn3pid%3DApple-Shazam%26mttnsub1%3DShazam_ios%26mttnsub2%3D5348615A-616D-3235-3830-44754D6D5973%26itscg%3D30201%26app%3Dmusic%26itsct%3DShazam_ios&videoIdToFilter=1432017572',
              'trackhighlighturl':
              'https://cdn.shazam.com/video/v3/en-US/GB/iphone/highlights/1432017572?affiliate=mttnagencyid%3Ds2n%26mttnsiteid%3D125115%26mttn3pid%3DApple-Shazam%26mttnsub1%3DShazam_ios%26mttnsub2%3D5348615A-616D-3235-3830-44754D6D5973%26itscg%3D30201%26app%3Dmusic%26itsct%3DShazam_ios'
          },
          'relatedtracksurl':
          'https://cdn.shazam.com/shazam/v3/en-US/GB/iphone/-/tracks/track-similarities-id-432365947?startFrom=0&pageSize=20&connected=',
          'albumadamid':
          '1445725433'
      },
      'tagid':
      '4B7FA2E2-ABFC-4868-BCC6-709191E025C6'
  }
  print(get_required_song_info(x))
  #print(extract_nested_keys(x))
