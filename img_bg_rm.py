import streamlit as st
from PIL import Image
from rembg import remove
import io
import os

#Functions
def process_img(uploaded_image):
    img = Image.open(uploaded_image)
    processed_img = remove_background(img)
    return processed_img

def remove_background(img):
    img_byte = io.BytesIO()
    img.save(img_byte, format="PNG")
    img_byte.seek(0)
    processed_img_bytes = remove(img_byte.read())
    return Image.open(io.BytesIO(processed_img_bytes))

#Frontend
st.set_page_config(page_title="IMG Background Remover", page_icon="✏", layout="centered")
st.image("img/bg_rm.jpeg", use_column_width=True)
st.title("IMG Background Remover")
st.subheader("Upload an image")
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    remove_button = st.button(label="Remove Background")

    if remove_button:
        processed_img = process_img(uploaded_image)
        st.image(processed_img, caption="Background Removed successfully", use_column_width=True)
        processed_img.save("Processed_img.png")
        with open("Processed_img.png", "rb") as f:
            img_data = f.read()
        st.download_button("Download Processed IMG", data=img_data, file_name="Processed_img.png")
        os.remove("Processed_img.png")