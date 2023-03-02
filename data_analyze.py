import pandas
import matplotlib as plt

# データフレームに格納して集計処理
def count_tags(list):
  # データフレーム用の配列を作成
  title_list = []
  view_count_list = []
  tags_list = []
  tag_priority_list = []
  for video in list:
    priority = 1
    for tag in video["tags"]:
      title_list.append(video["title"])
      view_count_list.append(video["view_count"])
      tags_list.append(tag)
      tag_priority_list.append(priority)
      priority += 1
  # データフレームを作成
  data_frame = pandas.DataFrame(
    data={
      'title': title_list,
      'view_count': view_count_list,
      'tag': tags_list,
      'tag_priority' : tag_priority_list
    }
  )

  # print(data_frame)

  # タグのグループを作成
  group_tag = data_frame.groupby('tag', as_index=False)
  # タグの出現回数を算出後に、多い順に並び変え、インデックスを振り直し、先頭の指定行を抽出
  sorted_group_tag = group_tag.size().sort_values('size',ascending=False).reset_index(drop=True)[0:10]

  print(sorted_group_tag)

  # # print(group_tag.groups) # 格納対象
  # print(group_tag.size()) # 出現回数
  # # print(group_tag.mean()) # 平均(tag_priority)
  
  # plt.bar()

  # tick_labelを使用したい
  ax = sorted_group_tag.plot(kind='barh', title='RESULT', tick_label=['a','b','c','d','e','a','b','c','d','e']) # MatplotlibのAxesSubplotオブジェクト


  fig = ax.get_figure()
  fig.savefig('./graph/result.jpg')
  
  