"""
きびダぬかょじイすいうゅヤみとのつモにうよかンまバるんドいッ、のをるド

きょうのよる、
びじゅつかんの
ダイヤモンドを
ぬすみにまいる
かいとうバッド

"""

import streamlit as st

def main():
    st.title("暗号解読・作成アプリ")
    st.caption("暗号を作成・解読するアプリ")

    mode = st.radio("モードを選択してください", ["解読モード", "作成モード"])

    if mode == "解読モード":
        page_read()
    else:
        page_make()

def page_read():
    st.header("解読モード", divider="rainbow")
    
    text = st.text_input("暗号を入力してください", placeholder= "パタトカクシーー")
    
    if text == "":
        st.stop()
    
    num_chars = st.number_input(
        "何文字ごとに読みますか",
        min_value=1,
        max_value=len(text)
    )
    
    result = read_ango(text,num_chars)
    # result = read_ango("パタトクカシーー", 2)
    st.write("解読された文章")
    st.code(result)         #コピーボタン追加のため

def read_ango(text, num_chars):
    col = len(text) // num_chars
    result = ""
    for j in range(num_chars):
        for i in range(col):
            result += text[num_chars * i + j]
        result += "\n"


    return result
    


def page_make():
    st.header("作成モード", divider="rainbow")

    text = st.text_area("1行当たりの文字数が同じ文章を暗号化します", placeholder="パトカー\nタクシー")

    if st.button("暗号化する"): 
        if check_text(text):
            st.success("暗号化に成功しました")
            ango = make_ango(text)
            st.code(ango)
        else:
            st.error("暗号化に失敗しました。すべての行をそろえてください")

def check_text(text):
    
    lines = text.split("\n")

    for i in range(len(lines)):
        if not len(lines[0]) == len(lines[i]):      # !=
            return False

    return True

def make_ango(text):

    lines = text.split("\n")

    ango = ""

    for i in range(len(lines[0])):
        for line in lines:
            ango += line[i]

    return ango







if __name__ == "__main__": #　アンダーバー２つ
    main()