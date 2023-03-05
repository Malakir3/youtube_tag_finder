#!/usr/bin/python

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
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
    order = "viewCount"
    # 以下は任意で設定
    # channelId = CHANNEL_ID,
    # videoDuration = "medium",
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
    # タグが設定されていない動画は例外として扱う
    if 'tags' in video_detail["items"][0]["snippet"]:
      tmp_dict["tags"] = video_detail["items"][0]["snippet"]["tags"]
    else:
      tmp_dict["tags"] = ["タグ無し"]

    # 結果配列に辞書を格納
    finder_result.append(tmp_dict)

  ##########################################################
  # 任意の後続処理
  # 例：結果を表示
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
  # 動画詳細の一覧を取得
  finder_result = youtube_search()

  # 一覧をデータフレームに格納
  data_frame = data_analyze.create_data_frame(finder_result)

  # データフレームからグラフを出力
  data_analyze.create_result_graph(data_frame, SEARCH_WORD, MAX_RESULTS)

