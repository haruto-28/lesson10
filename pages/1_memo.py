import streamlit as st
import os

# ファイル名を指定
NOTES_FILE = "notes.txt"

# メモを読み込む関数
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return f.read()
    return ""

# メモを保存する関数
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        f.write(notes)

# Streamlitアプリの構築
st.title("メモ帳アプリ")

# メモの読み込み
notes = load_notes()

# テキストエリアを表示
notes_input = st.text_area("メモを入力してください:", value=notes, height=300)

# 保存ボタン
if st.button("保存"):
    save_notes(notes_input)
    st.success("メモが保存されました。")

# 現在のメモを表示
st.subheader("現在のメモ")
st.write(notes_input)