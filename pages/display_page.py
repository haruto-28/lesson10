import streamlit as st
import json
import os

# ファイル名を指定
STATE_FILE = "state.json"

# セッション状態を読み込む関数
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"button_clicked": False, "another_button_clicked": False, "authenticated": False, "start_time": 0.0, "elapsed_time": 0.0}

# セッション状態を読み込む
if "state" not in st.session_state:
    st.session_state.state = load_state()

state = st.session_state.state

# 結果を表示
if state["another_button_clicked"]:
    st.write(f"宿題を終了しました。経過時間: {state['elapsed_time']:.2f}秒")
else:
    st.write("宿題はまだ終了していません。")

# 入力ページに戻るリンクを表示
st.write("入力ページに戻る -> [入力ページへ](mainpage.py)")