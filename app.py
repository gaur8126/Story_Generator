import streamlit as st
from PIL import Image
from story_generator import generate_story_from_images, narrate_story

st.title("AI Story Generator From Images")
st.markdown("Upload 1 to 10 images, choose an style and let AI write and narrate an story for you")


# sidebar 
with st.sidebar:
    st.header("Controls")


    # sidebar options to upload images
    uploaded_files = st.file_uploader(
        "Upload your images...",
        type=["png","jpg","jpeg"],
        accept_multiple_files = True
    )


    # Selecting a story style 
    story_style = st.selectbox(
        "Choose a story style",
        ("Comedy","Thriller","Fairy Tale","Sci-Fi","Mystery","Adventure","Morale")
    )


    ## Button to Generate story
    generate_button = st.button("Generate Story and Narration",type= "primary")


# Main Logic

if generate_button:
    if not uploaded_files:
        st.warning("Please upload atleast 1 image.")

    elif len(uploaded_files) > 10:
        st.warning("Please upload an maximum of 10 images.")
    else:
        with st.spinner("The AI is writting and narrating your story... This may take few moments."):
            try:
                pil_images = [Image.open(upload_image) for upload_image in uploaded_files]
                st.subheader("Your visual Inspiration:")
                image_columns = st.columns(len(pil_images))

                for i, image in enumerate(pil_images):
                    with image_columns[i]:
                        st.image(image,use_container_width=True)

                generate_story = generate_story_from_images(pil_images,style=story_style)
                if "Error" in generate_story or "failed" in generate_story or "API key" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"Your {story_style} story: ")
                    st.success(generate_story)

                st.subheader("Listen to your story")
                audio_file = narrate_story(generate_story)
                if audio_file:
                    st.audio(audio_file,format="audio/mp3")
            except Exception as e:
                st.error(f"An application error occured {e}")