import streamlit as st
import json
import os
import time

# ファイル名を指定
STATE_FILE = "state.json"
PASSWORD = "your_password"  # ここでパスワードを設定

# セッション状態を読み込む関数
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"button_clicked": False, "another_button_clicked": False, "authenticated": False, "start_time": 0.0, "elapsed_time": 0.0}

# セッション状態を保存する関数
def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

# セッション状態を読み込む
if "state" not in st.session_state:
    st.session_state.state = load_state()

state = st.session_state.state

# パスワード入力
if not state.get("authenticated", False):
    password = st.text_input("パスワードを入力してください:", type="password")
    if password == PASSWORD:
        state["authenticated"] = True
        save_state(state)
        st.experimental_rerun()  # 認証後にページをリロード
    else:
        st.write("パスワードが間違っています。")
else:
    # 認証されている場合にボタンを表示
    if st.button("Click Me"):
        state["button_clicked"] = True
        state["another_button_clicked"] = False
        state["start_time"] = time.time()
        save_state(state)
        st.experimental_rerun()

    if st.button("Click Another Button"):
        state["another_button_clicked"] = True
        state["button_clicked"] = False
        state["elapsed_time"] = time.time() - state["start_time"]
        save_state(state)
        st.experimental_rerun()

    # セッション状態に基づいて表示を更新
    if state["button_clicked"]:
        st.write("宿題を始めました")
    elif state["another_button_clicked"]:
        st.write(f"宿題を終了しました。経過時間: {state['elapsed_time']:.2f}秒")
    else:
        st.write("ボタンはまだ押されていません。")