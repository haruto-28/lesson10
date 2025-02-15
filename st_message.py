import streamlit as st
import random
import string

# ランダムなパスワードを生成する関数
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# セッション状態にパスワードを保存
if 'password' not in st.session_state:
    st.session_state.password = generate_random_password()

# パスワード入力
st.title("パスワード保護アプリ")
input_password = st.text_input("パスワードを入力してください", type="password")

# パスワードが正しいか確認
if st.button("ログイン"):
    if input_password == st.session_state.password:
        st.success("ログイン成功！🎉")
        st.write("ここにアプリの内容を表示します。")
    else:
        st.error("パスワードが間違っています。再試行してください。")

# 新しいパスワードを生成するボタン
if st.button("新しいパスワードを生成"):
    st.session_state.password = generate_random_password()
    st.success(f"新しいパスワードが生成されました: {st.session_state.password}")