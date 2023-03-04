#!/usr/bin/python

# テンプレート記載モジュール
from googleapiclient.discovery import build
# from oauth2client.tools import argparser

# 追記モジュール
from dotenv import load_dotenv
import os
import json
import data_analyze

################################################################################
def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # 動画一覧を取得
  search_response = youtube.search().list(
    q = SEARCH_WORD,
    type = "video",
    part="id,snippet",
    maxResults = MAX_RESULTS,
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

    if 'tags' in video_detail["items"][0]["snippet"]:
      tmp_dict["tags"] = video_detail["items"][0]["snippet"]["tags"]
    else:
      tmp_dict["tags"] = ["タグ無し"]

    # 結果配列に辞書を格納
    finder_result.append(tmp_dict)

  ##########################################################
  # 任意の後続処理
  # json_result = json.dumps(finder_result,indent=4,ensure_ascii=False)
  # print(json_result)
  ##########################################################

  return finder_result
################################################################################
# 環境変数の読み込み
load_dotenv()

DEVELOPER_KEY = os.environ.get('DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = os.environ.get('YOUTUBE_API_SERVICE_NAME')
YOUTUBE_API_VERSION = os.environ.get('YOUTUBE_API_VERSION')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
SEARCH_WORD = os.environ.get('SEARCH_WORD')
MAX_RESULTS = os.environ.get('MAX_RESULTS')

if __name__ == "__main__":
  # 検索条件の一部を外部から受け取る場合
  # argparser.add_argument("--q", help="Search term", default="yoyo")
  # argparser.add_argument("--max-results", help="Max results", default=5)
  # args = argparser.parse_args()

  # 動画詳細の一覧を取得
  finder_result = youtube_search()

  # 一覧をデータフレームに格納して集計処理
  data_frame = data_analyze.count_tags(finder_result, SEARCH_WORD, MAX_RESULTS)
