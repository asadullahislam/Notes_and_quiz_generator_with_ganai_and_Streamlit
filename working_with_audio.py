from gtts import gTTS
import streamlit as st
import io

text="Hello welcome to this course"
speach =gTTS(text,lang="en",slow=False)

audio_buffer = io.BytesIO()
speach.write_to_fp(audio_buffer)
st.audio(audio_buffer)