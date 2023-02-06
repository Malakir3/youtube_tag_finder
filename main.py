#!/usr/bin/python

# デフォルト
from apiclient.discovery import build
from apiclient.errors import HttpError
# from oauth2client.tools import argparser

# 追記
from dotenv import load_dotenv
import os
# 別ファイルをインポート
import detail_search

# 環境変数の読み込み
load_dotenv()

DEVELOPER_KEY = os.environ.get('DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = os.environ.get('YOUTUBE_API_SERVICE_NAME')
YOUTUBE_API_VERSION = os.environ.get('YOUTUBE_API_VERSION')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
SEARCH_WORD = os.environ.get('SEARCH_WORD')

def youtube_search(search_response):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q = SEARCH_WORD,
    type = "video",
    part="id,snippet",
    maxResults="10",
    # channelId = CHANNEL_ID,
    videoDuration = "medium",
    order = "viewCount"
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
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

  # 配列の中身を改行コードで連結して出力
  print ("Videos:\n", "\n".join(videos), "\n")
  # print ("Channels:\n", "\n".join(channels), "\n")
  # print ("Playlists:\n", "\n".join(playlists), "\n")

  return search_response

if __name__ == "__main__":
  # 検索条件の一部を外部から受け取る場合
  # argparser.add_argument("--q", help="Search term", default="yoyo")
  # argparser.add_argument("--max-results", help="Max results", default=5)
  # args = argparser.parse_args()

  search_ary = []
  try:
    youtube_search(search_ary)

    print(search_ary)

    # detail_search.videos(search_ary)
  except:
    print ("An HTTP error occurred")
  # except (HttpError, e):
    # print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))