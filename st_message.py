# app.py
import streamlit as st

# ページのタイトル
st.title("メッセージ送信アプリ")

# メッセージを入力するページ
if st.sidebar.button("メッセージを送る"):
    # メッセージの入力
    message = st.text_input("送信するメッセージを入力してね")

    # メッセージをセッション状態に保存
    if message:
        st.session_state.message = message
        st.success("メッセージを送信しました！🎉")
    else:
        st.warning("メッセージを入力してください！")

# 別のページに移動するボタン
if st.sidebar.button("メッセージを表示する"):
    st.session_state.show_message = True

# メッセージを表示するページ
if st.session_state.get("show_message"):
    st.title("受信したメッセージ")
    if "message" in st.session_state:
        st.write(f"受信したメッセージ: {st.session_state.message}")
    else:
        st.write("メッセージはありません。")