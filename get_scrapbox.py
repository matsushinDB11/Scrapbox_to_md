import requests
import re


# 通常URLをAPI用URLに変換
def replace_url_with_api(url):
    ptn_url = re.compile(r'https://scrapbox.io/(.*)')
    result = ptn_url.search(url)
    api = 'https://scrapbox.io/api/pages/' + result.group(1)
    return api


# scrapboxのタイトルに'/',' 'が含まれる場合の特殊URLを変換
def replace_spacial_url(title):
    line_array = list(title)
    ret_title = ''
    for i in line_array:
        if i == '/':
            i = '%2F'
        elif i == ' ':
            i = '_'
        ret_title += i
    return ret_title


# scrapbox のページ一覧を取得
def pagelist(url, limit=100, is_project_private=False, cookies=None):
    scapbox_api_url = replace_url_with_api(url)
    if is_project_private:
        res = requests.get(scapbox_api_url + '?limit=' + str(limit), cookies=cookies)
    else:
        res = requests.get(scapbox_api_url + '?limit=' + str(limit))
    return res


# scrapbox のページ内容を取得
def page(url, title, is_project_private=False, cookies=None):
    scrapbox_title = replace_spacial_url(title)
    scapbox_api_url = replace_url_with_api(url)
    page_api_url = scapbox_api_url + scrapbox_title
    if is_project_private:
        res = requests.get(page_api_url, cookies=cookies)
    else:
        res = requests.get(page_api_url)
    return res
