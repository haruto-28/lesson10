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
    return {"button_clicked": False}

# セッション状態を保存する関数
def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

# セッション状態を読み込む
state = load_state()

# ボタンの状態を確認して、セッション状態を更新
if st.button("Click Me"):
    state["button_clicked"] = True
    save_state(state)

# セッション状態に基づいて表示を更新
if state["button_clicked"]:
    st.write("Button was clicked!")
else:
    st.write("Button has not been clicked yet.")