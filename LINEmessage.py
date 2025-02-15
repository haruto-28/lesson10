import streamlit as st
import requests

# LINEのチャネルアクセストークン
LINE_CHANNEL_ACCESS_TOKEN = 'gg1QDQOYgK74md2lPMCIZI+OKx3/00r6Rs7NecUO5vmM+McOyrt1TEeseRAsySlRNWbIeGT1M8oj49Mo7DbQOcmSwE1xcnWtj5wP/h6buAf7ZqSZ3szhOirUEBXMwr7grdm4xq+kKKBM6UCr/uVTHAdB04t89/1O/w1cDnyilFU='

def send_line_message(message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }
    payload = {
        'to': 'mine88xyzword',  # メッセージを送る相手のユーザーID
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