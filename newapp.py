import streamlit as st
from PIL import Image

# Set up the Streamlit page
st.set_page_config(page_title="Image Upload App", layout="wide")

# Title and description
st.title("Image Upload App")
st.write("Upload an image and click the button to see the response.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Button to process the uploaded image
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Add a button
    if st.button("Submit"):
        st.success("Thanks for uploading the image!")
