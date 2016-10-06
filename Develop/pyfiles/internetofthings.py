#contains all the stuff for interfacing with the web.
#Wget
#Item Downloader(Deprecated)
#internetcheck
'''
if you are paranoid... there is a config option under General.cfg to disable this whole module.
'''
from . import upsettings as settings
import urllib.request, urllib.error, urllib.parse
import wget
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
def internet_on():
    if settings.GetGlobsett('disableinterwebzcheck') == 0:
        try:
            response=urllib.request.urlopen('8.8.8.8',timeout=1)
            return True
        except urllib.error.URLError as err:
            return False
    else:
        logging.info('internet check is disabled.(This is Normal Most of the time if you manually disable it.)')
def DownloadItem(url,name,Size):
    if settings.GetGlobsett('disableinterwebzcheck') == '0':
        print(('The size of this file is:' + Size))
        if Size > 100:
            print('This file is quite large and may take a long time on a bad internet.')
        urllib.request.urlretrieve (url, name)
        print('Done!')
    else:
        logging.info('Connection to internet is currently turned off. please enable it for downloading.')
#wget
def wgetr(item,out=None):
    if item.find('http') == '-1':
        logging.warn('was thrown a invalid link! not processing it.')
    else:
        print(('Wgetting item: ' + item))
        if out ==None:
            wget.download(item)
        else:
            wget.download(item,out)
#youtube
# Comment: i cannot prevent people from using the api key soo yeah
DEVELOPER_KEY = 'AIzaSyD_SNXOc8SfLdGWvPcHNLXvJqyF3u_Pqcc'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()
  videos = []
  channels = []
  playlists = []
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  return "Videos:\n", "\n".join(videos), "\n"
  return "Channels:\n", "\n".join(channels), "\n"
  return "Playlists:\n", "\n".join(playlists), "\n"