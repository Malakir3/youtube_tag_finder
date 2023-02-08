#!/usr/bin/python

# テンプレート記載モジュール
from apiclient.discovery import build
from apiclient.errors import HttpError
# from oauth2client.tools import argparser

# 追記モジュール
from dotenv import load_dotenv
import os
# import detail_search

################################################################################
def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # 動画一覧を取得
  search_response = youtube.search().list(
    q = SEARCH_WORD,
    type = "video",
    part="id,snippet",
    maxResults="10",
    # channelId = CHANNEL_ID,
    videoDuration = "medium",
    order = "viewCount"
  ).execute()

  # タグを検索
  for video in search_response.get("items", []):  
    snippet = youtube.videos().list(
      id = video["id"]["videoId"],
      type = "video",
      part="snippet",
    ).execute()

    print(snippet["tags"])

  # 結果の出力が不要であれば、以下は削除する
  videos = []
  channels = []
  playlists = []

  # "items"の値部分(配列)の各要素について繰り返し
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
################################################################################
# 環境変数の読み込み
load_dotenv()

DEVELOPER_KEY = os.environ.get('DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = os.environ.get('YOUTUBE_API_SERVICE_NAME')
YOUTUBE_API_VERSION = os.environ.get('YOUTUBE_API_VERSION')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
SEARCH_WORD = os.environ.get('SEARCH_WORD')

if __name__ == "__main__":
  # 検索条件の一部を外部から受け取る場合
  # argparser.add_argument("--q", help="Search term", default="yoyo")
  # argparser.add_argument("--max-results", help="Max results", default=5)
  # args = argparser.parse_args()

  # 動画一覧を取得
  search_result = youtube_search()

  # 動画一覧からタグを取得
  # detail_result = detail_search.get_tags(search_result)

  # try:
    # search_result = youtube_search()
    # detail_search.videos(search_response)
  # except:
  #   print ("An HTTP error occurred")
  # except (HttpError, e):
    # print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))