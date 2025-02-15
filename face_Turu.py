import streamlit as st
from PIL import Image
import face_recognition

# 基準の写真を読み込む
known_image = face_recognition.load_image_file("known_face.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# カメラで写真を撮る
uploaded_file = st.camera_input("写真を撮ってね！")

if uploaded_file is not None:
    # 撮った写真を表示
    image = Image.open(uploaded_file)
    st.image(image, caption='撮った写真', use_column_width=True)

    # 撮った写真を読み込む
    unknown_image = face_recognition.load_image_file(uploaded_file)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)

    # 一致を確認
    if unknown_face_encodings:
        results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0])
        if results[0]:
            st.write("一致！🎉")
        else:
            st.write("一致しませんでした。😢")