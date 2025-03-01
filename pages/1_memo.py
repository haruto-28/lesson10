import streamlit as st
import json
import os

# ファイル名を指定
NOTES_FILE = "notes.json"

# メモを読み込む関数
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

# メモを保存する関数
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

# Streamlitアプリの構築
st.title("メモ帳アプリ")

# メモの読み込み
notes = load_notes()

# 新しいメモの入力
new_note = st.text_area("新しいメモを入力してください:", height=100)

# 保存ボタン
if st.button("保存"):
    if new_note:
        notes.append(new_note)
        save_notes(notes)
        st.success("メモが保存されました。")
        # ページをリロードするためにクエリパラメータを設定
        st.experimental_set_query_params(reload="true")

# 現在のメモの表示
st.subheader("保存されたメモ")
if notes:
    for i, note in enumerate(notes):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"メモ {i + 1}: {note}")
        with col2:
            # 削除ボタン
            if st.button("削除", key=f"delete_{i}"):
                notes.pop(i)
                save_notes(notes)
                st.experimental_set_query_params(reload="true")
else:
    st.write("保存されたメモはありません。")