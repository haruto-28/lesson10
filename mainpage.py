import streamlit as st

# タイトルと説明
st.title("宿題管理ページ")
st.write("現在の宿題の状況")

# ユーザー入力
height = st.number_input("身長 (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
weight = st.number_input("体重 (kg)", min_value=10.0, max_value=200.0, value=70.0, step=0.1)

# BMI計算
if height > 0 and weight > 0:
    height_m = height / 100  # cmをmに変換
    bmi = weight / (height_m ** 2)
    st.write(f"あなたのBMIは: {bmi:.2f}")

    # BMIのカテゴリ表示
    if bmi < 18.5:
        st.write("BMIカテゴリ: 低体重")
    elif 18.5 <= bmi < 25:
        st.write("BMIカテゴリ: 普通体重")
    elif 25 <= bmi < 30:
        st.write("BMIカテゴリ: 肥満 (1度)")
    elif 30 <= bmi < 35:
        st.write("BMIカテゴリ: 肥満 (2度)")
    else:
        st.write("BMIカテゴリ: 肥満 (3度)")