#!/usr/bin/python

# テンプレート記載モジュール
from googleapiclient.discovery import build
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser

# 追記モジュール
from dotenv import load_dotenv
import os
import json
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
    maxResults="3",
    # channelId = CHANNEL_ID,
    videoDuration = "medium",
    order = "viewCount"
  ).execute()

  # 動画の詳細情報を検索
  finder_result = []
  for each_video in search_response.get("items", []):    
    video_detail = youtube.videos().list(
      id = each_video["id"]["videoId"],
      part = "snippet,statistics"
    ).execute()

    # 一時的な辞書を作成
    tmp_dict = {}
    tmp_dict["title"] = video_detail["items"][0]["snippet"]["title"]
    tmp_dict["view_count"] = video_detail["items"][0]["statistics"]["viewCount"]
    tmp_dict["tags"] = video_detail["items"][0]["snippet"]["tags"]

    # 結果配列に辞書を格納
    finder_result.append(tmp_dict)

  ##########################################################
  # 任意の後続処理
  json_result = json.dumps(finder_result,indent=4,ensure_ascii=False)
  print(json_result)
  ##########################################################

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