import streamlit as st

from api_calling import note_generator,audio_transcription,quiz_generator
## from pillow 
from PIL import Image

 

st.title("Note SUmmary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quizzes")
st.divider()

# we work on image

with st.sidebar:
    st.header("controls")
    images=st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
        )
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            col=st.columns(len(images))

            st.subheader("Your uploaded images")


            for i ,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #difficulty 
    selected_option=st.selectbox(
        "Enter the diffculty of your quiz",
        ("Easy","Medium","Hard"),
        index=None
    )
    pressed =st.button("Click the button to initiate AI",type="primary")

if pressed:
    if not images:
        st.error("you must upload 1 image")
    if not selected_option:
        st.error("you must select a dificulty ")



#container 
    if images and selected_option:

    #note
        with st.container(border=True):
            st.subheader('Your note')
        # this portion is replaced by api call
            with st.spinner("AI is writing notes for you"):
                 generated_notes = note_generator(pil_images)
                 st.markdown(generated_notes)


    #audio transcript
        with st.container(border=True):
            st.subheader("Your Audio Transcript")
        


            with st.spinner("AI is generation audio transcript for you"):
              #clearing the markdown
            
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("`","")
                audio_transcript=audio_transcription(generated_notes)
                st.audio(audio_transcript)



    #quiz
        with st.container(border=True):
            st.subheader(f"Quiz ( {selected_option}) dificullty")
            with st.spinner("AI is gererationg the quizzes"):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)