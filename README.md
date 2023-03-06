# プログラム名
YouTube Tag Finder

# 概要
YouTubeに投稿されている動画に付けられているタグを一括取得し、どんなタグの使用頻度が高いのかを調査します。

# 環境
python -v 3.10.4

# 使用ライブラリ
- google-api-python-client -v 2.78.0
- python-dotenv -v 0.21.1
- pandas -v 1.5.3
- matplotlib -v 3.7.0

# 制作背景
YouTubeDataAPIを使って何かできないかと考え、当初は漠然とYouTubeDataAPIの公式ドキュメントを見ていました。その際に、動画投稿者が各動画に対して任意で付与できるタグの存在を知りました。<br>
詳しく調べてみると、そのタグを視聴者が閲覧するには手間がかかることが分かりました。その反面、タグに設定された文字を知ることができれば、視聴者が新たな動画投稿者として同様の動画を投稿する際の助けになると考えました。<br>
本プログラムを使用すれば、動画投稿者が他の動画投稿者の動画に付けられたタグを、素早く調査することができます。

# 利用方法
1. 本プログラムでは前述のライブラリを使用していますので、それぞれ使用できるようPCにインストールしてください。<br>
`$ pip install LIBRARY_NAME`

2. ご自身のローカルPCで本プログラムを使用したいディレクトリに移動し、リポジトリをクローンしてください。<br>
```
例）デスクトップに作成済みのフォルダ"example"で実行する場合（OS:Windows, Shell:Bash）
$ cd ~/Desktop/example
$ git clone https://github.com/Malakir3/youtube_tag_finder.git
```
3. 以下のファイル・フォルダの名前を変更してください。
```
.env_dummy → .env
graph_dummy → graph
```
4. ファイル".env"に定義している各環境変数や検索ワードを設定してください。
5. main.pyを実行します。成功すれば、"graph"フォルダ内にjpg形式で画像ファイルが生成されます。<br>
`$ python main.py`

# 目指した課題解決


# 工夫したポイント


# 使用技術（開発環境）
## 言語
Python

## ソース管理
GitHub, SourceTree

## バージョン管理
Git for Windows

## エディタ
VSCode

## OS
Windows 10 Home

# 課題、実装予定の機能

# 開発秘話



