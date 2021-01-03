import re


# 1ページ分リストで渡す
# Scrapboxページの記法をMarakdown形式に変換し、1ページ分を配列で返す。
def scrapbox_to_md(text_array):
    # 箇条書き
    space = re.compile(r'^\s(.*)')
    wspace = re.compile(r'^\s{2,}(.*)')
    # 見出し or 太字
    headline_or_bold = re.compile(r'\[\*+(.+)\]')
    # 見出し
    h2 = re.compile(r'^\[\*{2,}(.+)\]')
    h3 = re.compile(r'^\[\*(.+)\]')
    # 消し線
    erase_line = re.compile(r'\[-\s(.+)\]')
    # ソースコード
    code = re.compile(r'code:(\w+)')
    # URLのみハイパーリンク
    hyperlink = re.compile(r'(^http(s)?://([\w-]+\.)+[\w-]+(/[\w ./?&=-]*)?)')
    # テキストのハイパーリンク
    text_hyperlink = re.compile(r'\[(.+)(http(s)?://([\w-]+\.)+[\w-]+(/[\w ./?&=-]*)?)\]')
    # Gyazo画像URL
    gyazo_link = re.compile(r'(http(s)?://(gyazo\.)+[\w-]+(/[\w ./?&=-]*)?)')

    md_array = []
    is_this_text_code = False
    is_this_text_title = True

    num_of_loops = 0
    for text in text_array:
        if is_this_text_title:
            md = '# ' + text
            is_this_text_title = False
        else:
            # テキストが箇条書きかを判定
            is_this_text_bullet = False
            # result_tab = tab.search(text)
            result_space = space.search(text)
            result_wspace = wspace.search(text)
            # ソースコードの終了点を判定
            if is_this_text_code:
                if not result_space:
                    md_array.append('```')
                    is_this_text_code = False
            # テキストがソースコードが判定
            if result_code := code.search(text):
                is_this_text_code = True
            if not is_this_text_code:
                # テキストが箇条書きか判定
                if result_space:
                    text = re.sub(r'^\s+\s*', '', text)
                    is_this_text_bullet = True
            # 見出し or 太字の場合
            if headline_or_bold.search(text):
                if result_h2 := h2.search(text):
                    md = '## ' + result_h2.group(1)
                elif result_h3 := h3.search(text):
                    md = '# ' + result_h3.group(1)
                else:
                    text = re.sub(r'\[\*+\s', '**', text)
                    md = re.sub(r'\]', '**', text)
            elif result := gyazo_link.search(text):
                md = '['+'(画像)'+']' + '(' + result.group(0) + ')'
            elif result := hyperlink.search(text):
                md = '[' + result.group(0) + ']' + '(' + result.group(0) + ')'
            elif result := text_hyperlink.search(text):
                md = '[' + result.group(1) + ']' + '(' + result.group(2) + ')'
            elif result_erase := erase_line.search(text):
                md = '~~' + result_erase.group(1) + '~~'
            elif result_code:
                md = '```' + result_code.group(1)
            else:
                md = text
            if is_this_text_bullet:
                if result_wspace:
                    md = '  - ' + md
                else:
                    md = '- ' + md
        md_array.append(md + '  ')
        num_of_loops += 1
    return md_array
