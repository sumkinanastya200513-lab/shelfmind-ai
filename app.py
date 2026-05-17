import streamlit as st
import tempfile
from pipeline import process_video

st.set_page_config(page_title="ShelfMind AI")

st.title("ShelfMind AI")
st.write("Загрузка видео с ценниками")

uploaded_file = st.file_uploader(
    "Загрузите видео",
    type=["mp4", "avi", "mov"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.read())
        video_path = tmp.name

    st.success("Видео загружено")

    if st.button("Начать обработку"):

        with st.spinner("Идет обработка..."):

            df = process_video(video_path)

            st.success("Готово")

            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Скачать CSV",
                data=csv,
                file_name="results.csv",
                mime="text/csv"
            )