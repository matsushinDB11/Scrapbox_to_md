Scrapbox to Markdown
=====
## OverView
Scrapboxのページ内容をMarkdown形式に変換して出力する
## Discription
Scrapbox_to_Notion.pyの下記変数それぞれに値を設定して実行すると、Scrapboxのページの中身をそれぞれMarkdown形式に変換してoutput_mdディレクトリに出力する。


Scrapbox_to_Notion.py 変数の説明
- url: 文字列型 ScrapboxプロジェクトのURLを設定する
- cookies: 文字列型 Scrapboxプロジェクトがプライベートプロジェクトの場合、ログイン時のCookieを設定する。CookieはScrapboxプロジェクトにログインした状態でブラウザのDeveloper tool から確認できる。
- limit = 整数型 Scrapboxプロジェクトから呼び出すページの数
- is_project_private: bool型 Scrapboxプロジェクトがプライベートプロジェクトの場合True, パブリックの場合Falseを設定する。
## Requirement
Python 3.8  
request module
