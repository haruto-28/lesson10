import streamlit as st
import requests

# LINEのチャネルアクセストークン
LINE_CHANNEL_ACCESS_TOKEN = 'YOUR_CHANNEL_ACCESS_TOKEN'

def send_line_message(message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }
    payload = {
        'to': 'YOUR_USER_ID',  # メッセージを送る相手のユーザーID
        'messages': [{'type': 'text', 'text': message}]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

st.title("LINEメッセージ送信アプリ")

message = st.text_input("送信するメッセージを入力してね")

if st.button("メッセージを送る"):
    if message:
        status = send_line_message(message)
        if status == 200:
            st.success("メッセージを送信しました！🎉")
        else:
            st.error("メッセージの送信に失敗しました。😢")
    else:
        st.warning("メッセージを入力してください！")