# アプリ名
YouTube tag finder

# 概要
YouTubeに投稿されている動画に付けられているタグを一括取得し、どんなタグの使用頻度が高いのかを調査します。

# 環境
python -v 3.10.4

# 使用ライブラリ
googleapiclient
dotenv
pandas
matplotlib

# 制作背景

# 利用方法
1. 本プログラムでは前述のライブラリを使用していますので、それぞれ使用できるようPCにインストールしてください。
`$ pip install LIBRARY_NAME

2. ご自身のローカルPCでデータをクローンしたいディレクトリに移動した後に、以下のコマンドを実行してください。  
`$ git clone https://github.com/Malakir3/youtube_tag_finder.git`
3. 以下のとおりファイル名を変更してください。
".env_dummy" → ".env"
"graph_dummy" → "graph"
4. ".env"に定義している各環境変数や検索ワードを設定してください。
5. main.pyを実行します。成功すれば、"graph"フォルダ内にjpg形式で画像ファイルが生成されます。
`$ python main.py`


# 目指した課題解決

# 工夫したポイント


# 使用技術（開発環境）
## 言語
Python

## ソース管理
GitHub, SourceTree

## エディタ
VSCode


# 課題、実装予定の機能

# 開発秘話



