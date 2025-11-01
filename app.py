import streamlit as st

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
            st.write("hello")