import json
from scrapbox_notation_to_md import scrapbox_to_md
import get_scrapbox
import re


# scrapboxページタイトルからテキストを呼び出す
def call_text_array(url, title, is_project_private=False, cookies=None):
    # 各ページの中身を順に取得
    scrapbox_page_res = get_scrapbox.page(url, title, is_project_private, cookies)
    scrapbox_page_items = json.loads(scrapbox_page_res.text)
    line_array = []
    for i in scrapbox_page_items["lines"]:
        line_array.append(i["text"])
    return line_array

# ファイル名に使用できない空白文字を削除する。
def avoid_special_char(char):
    file_name = re.sub(r'[\s/]', '', char)
    return file_name


def main():
    # scrapbox プロジェクトのURL
    url = "https://scrapbox.io/$Projectname"
    # プライベートプロジェクトのcookie
    cookies = {"connect.sid": "$Cookies"}
    # 呼び出す記事の数
    limit = 300
    # プロジェクトはプライベートか？
    is_project_private = True
    # ページ一覧を取得
    scrapbox_page_list = get_scrapbox.pagelist(url, limit, is_project_private, cookies)
    scrapbox_page_list_items = json.loads(scrapbox_page_list.text)

    # 各ページのデータが入った配列要素はdict
    pages_array = scrapbox_page_list_items["pages"]

    for page in pages_array:
        title = page['title']
        scrapbox_title = avoid_special_char(title)
        texts = call_text_array(url, title, is_project_private, cookies)
        md_array = scrapbox_to_md(texts)
        with open('output_md/' + scrapbox_title + '.md', 'a', encoding='utf-8') as f:
            for i in md_array:
                f.write(i+'\n')


if __name__ == '__main__':
    main()
